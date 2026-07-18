#!/usr/bin/env python3
"""批量生成术语定义。

使用批量Prompt，单次调用生成5个术语的定义，降低API调用次数。
支持断点续传：检查已生成的term_id，跳过；进度文件持久化。
支持错误隔离：单个批次失败不影响其他批次。
"""
import sys
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config
from scripts.utils.agnes_client import get_client


BATCH_SIZE = 5  # 每次API调用生成5个术语
PROGRESS_FILE = config.paths.progress_dir / "gen_progress.json"
FAILED_FILE = config.paths.queue_dir / "failed_definitions.json"


BATCH_SYSTEM_PROMPT = """You are an AI terminology expert. Generate comprehensive definitions for multiple AI terms in a single response.

Rules:
1. Each term needs: term_id, english, category, definition_short (1 sentence), definition_long (50-100 words), key_concepts (3-5), use_cases (2-3), related_terms (3-5), difficulty (1-5), tags (2-4)
2. code_example: provide a short Python example if applicable, else null
3. Be accurate and concise - this is a reference dictionary
4. Respond ONLY in valid JSON: {"terms": [{...}, {...}, ...]}"""


def build_batch_messages(terms: list) -> list:
    """构建批量生成的messages。"""
    terms_desc = "\n".join(
        f"{i+1}. term_id: {t['term_id']}, english: {t['english']}, category: {t['category']}"
        for i, t in enumerate(terms)
    )
    user_msg = f"""Generate definitions for the following {len(terms)} AI terms:

{terms_desc}

Output JSON: {{"terms": [{{"term_id": "...", "english": "...", "category": "...", "definition_short": "...", "definition_long": "...", "key_concepts": [...], "use_cases": [...], "related_terms": [...], "code_example": null, "difficulty": 3, "tags": [...]}}, ...]}}

Respond ONLY with valid JSON."""
    return [
        {"role": "system", "content": BATCH_SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]


def load_existing_definitions() -> list:
    """加载已生成的定义（用于断点续传）。"""
    output_file = config.paths.queue_dir / "generated_definitions.json"
    if output_file.exists():
        with open(output_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def load_failed_terms() -> list:
    """加载失败术语列表。"""
    if FAILED_FILE.exists():
        with open(FAILED_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_progress(generated_count: int, total: int, failed_term_ids: list):
    """保存进度到文件。"""
    progress = {
        "generated_count": generated_count,
        "total": total,
        "failed_term_ids": failed_term_ids,
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def main():
    print("=" * 60)
    print("Step 02-01: 批量生成术语定义（支持断点续传）")
    print("=" * 60)

    # 加载种子术语
    with open(config.paths.pending_terms_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_terms = data["terms"]

    # 加载已生成定义（断点续传）
    existing_definitions = load_existing_definitions()
    existing_term_ids = {d["term_id"] for d in existing_definitions}
    print(f"已存在定义: {len(existing_term_ids)} 条")

    # 过滤掉已生成的术语
    target_terms = [t for t in all_terms if t["term_id"] not in existing_term_ids]
    print(f"待生成术语数: {len(target_terms)} (总计 {len(all_terms)})")

    if not target_terms:
        print("✓ 所有术语已生成，无需操作")
        return 0

    print(f"批量大小: {BATCH_SIZE}")
    print(f"预计API调用: {(len(target_terms) + BATCH_SIZE - 1) // BATCH_SIZE} 次")

    client = get_client()
    new_definitions = []
    failed_term_ids = []
    batch_count = 0
    total_batches = (len(target_terms) + BATCH_SIZE - 1) // BATCH_SIZE

    # 分批生成
    for batch_idx in range(0, len(target_terms), BATCH_SIZE):
        batch = target_terms[batch_idx:batch_idx + BATCH_SIZE]
        batch_count += 1
        print(f"\n[批次 {batch_count}/{total_batches}] 生成 {len(batch)} 个术语: {[t['english'] for t in batch]}")

        try:
            messages = build_batch_messages(batch)
            result = client.chat_json(messages, temperature=0.3)

            if "terms" in result:
                batch_defs = result["terms"]
                # 补充元数据
                for i, defn in enumerate(batch_defs):
                    if i < len(batch):
                        defn["term_id"] = batch[i]["term_id"]
                        defn["category"] = batch[i].get("category", defn.get("category", ""))
                        defn["source"] = "agnes_llm"
                        defn["generated_at"] = datetime.utcnow().isoformat() + "Z"
                        defn["model"] = config.agnes.model
                        new_definitions.append(defn)
                        print(f"  ✓ {defn.get('english', 'N/A')}: {defn.get('definition_short', '')[:60]}...")
            else:
                print(f"  ⚠ 响应格式异常，尝试单条生成")
                # 降级为单条生成
                for term in batch:
                    try:
                        from scripts.prompts.definition_prompt import build_messages
                        messages = build_messages(term["term_id"], term["english"], term["category"])
                        defn = client.chat_json(messages, temperature=0.3)
                        defn["term_id"] = term["term_id"]
                        defn["category"] = term.get("category", "")
                        defn["source"] = "agnes_llm"
                        defn["generated_at"] = datetime.utcnow().isoformat() + "Z"
                        defn["model"] = config.agnes.model
                        new_definitions.append(defn)
                        print(f"  ✓ 单条: {defn.get('english', 'N/A')}")
                    except Exception as e:
                        print(f"  ✗ {term['english']}: {e}")
                        failed_term_ids.append(term["term_id"])
        except Exception as e:
            print(f"  ✗ 批次失败: {e}")
            # 降级为单条
            for term in batch:
                try:
                    from scripts.prompts.definition_prompt import build_messages
                    messages = build_messages(term["term_id"], term["english"], term["category"])
                    defn = client.chat_json(messages, temperature=0.3)
                    defn["term_id"] = term["term_id"]
                    defn["category"] = term.get("category", "")
                    defn["source"] = "agnes_llm"
                    defn["generated_at"] = datetime.utcnow().isoformat() + "Z"
                    defn["model"] = config.agnes.model
                    new_definitions.append(defn)
                    print(f"  ✓ 降级单条: {defn.get('english', 'N/A')}")
                except Exception as e2:
                    print(f"  ✗ {term['english']}: {e2}")
                    failed_term_ids.append(term["term_id"])

        # 每10批次保存一次（断点续传）
        if batch_count % 10 == 0:
            all_definitions = existing_definitions + new_definitions
            output_file = config.paths.queue_dir / "generated_definitions.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(all_definitions, f, ensure_ascii=False, indent=2)
            save_progress(len(all_definitions), len(all_terms), failed_term_ids)
            print(f"  💾 已保存进度: {len(all_definitions)}/{len(all_terms)}")

    # 最终保存
    all_definitions = existing_definitions + new_definitions
    output_file = config.paths.queue_dir / "generated_definitions.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_definitions, f, ensure_ascii=False, indent=2)

    # 保存失败列表
    if failed_term_ids:
        with open(FAILED_FILE, "w", encoding="utf-8") as f:
            json.dump(failed_term_ids, f, ensure_ascii=False, indent=2)

    save_progress(len(all_definitions), len(all_terms), failed_term_ids)

    print(f"\n✓ 共生成 {len(new_definitions)} 条新定义（总计 {len(all_definitions)}/{len(all_terms)}）")
    print(f"  失败: {len(failed_term_ids)} 条")
    print(f"  输出: {output_file}")
    if failed_term_ids:
        print(f"  失败列表: {FAILED_FILE}")

    return 0 if len(all_definitions) >= len(all_terms) * 0.8 else 1


if __name__ == "__main__":
    sys.exit(main())
