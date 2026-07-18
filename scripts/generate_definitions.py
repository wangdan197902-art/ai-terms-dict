#!/usr/bin/env python3
"""生成术语定义。

为指定的种子术语调用AGNES_LLM生成结构化定义。
"""
import sys
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config
from scripts.utils.agnes_client import get_client
from scripts.prompts.definition_prompt import build_messages


def load_target_terms(limit: int = 1) -> list:
    """加载目标术语。"""
    with open(config.paths.pending_terms_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    # 第一个术语总是 prompt-engineering
    terms = data["terms"][:limit]
    # 确保 prompt_engineering 在第一位
    prompt_eng = next((t for t in data["terms"] if t["term_id"] == "prompt_engineering"), None)
    if prompt_eng and prompt_eng not in terms:
        terms.insert(0, prompt_eng)
        terms = terms[:limit]
    return terms


def generate_definition(term: dict) -> dict:
    """为单个术语生成定义。"""
    client = get_client()
    messages = build_messages(
        term_id=term["term_id"],
        term=term["english"],
        category=term["category"],
    )
    print(f"  生成定义: {term['english']} ({term['term_id']})...")
    result = client.chat_json(messages, temperature=0.3)

    # 补充元数据
    result["term_id"] = term["term_id"]
    result["category"] = term.get("category", result.get("category", ""))
    result["source"] = "agnes_llm"
    result["generated_at"] = datetime.utcnow().isoformat() + "Z"
    result["model"] = config.agnes.model

    return result


def main():
    print("=" * 60)
    print("Step 01-01: 单术语定义生成")
    print("=" * 60)

    # 加载术语（Phase 1 只处理1个：prompt-engineering）
    terms = load_target_terms(limit=1)
    print(f"目标术语: {[t['english'] for t in terms]}")

    definitions = []
    for term in terms:
        try:
            definition = generate_definition(term)
            definitions.append(definition)
            print(f"  ✓ {term['english']}: {definition.get('definition_short', '')[:80]}...")
        except Exception as e:
            print(f"  ✗ {term['english']}: 生成失败 - {e}")
            # 兜底：使用golden sample
            golden_path = config.paths.golden_samples_dir / f"{term['term_id']}.json"
            if golden_path.exists():
                print(f"  ⚠ 降级使用黄金样本: {golden_path}")
                with open(golden_path, "r", encoding="utf-8") as f:
                    definition = json.load(f)
                definition["source"] = "golden_sample_fallback"
                definitions.append(definition)

    # 保存
    config.paths.queue_dir.mkdir(parents=True, exist_ok=True)
    output_file = config.paths.queue_dir / "generated_definitions.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(definitions, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 已生成 {len(definitions)} 条定义")
    print(f"  输出: {output_file}")

    # 与黄金样本对比
    if definitions:
        golden_path = config.paths.golden_samples_dir / f"{definitions[0]['term_id']}.json"
        if golden_path.exists():
            with open(golden_path, "r", encoding="utf-8") as f:
                golden = json.load(f)
            print(f"\n黄金样本对比:")
            print(f"  AI生成的短定义: {definitions[0].get('definition_short', '')[:100]}")
            print(f"  黄金样本短定义: {golden.get('definition_short', '')[:100]}")
            # 简单相似度
            ai_short = definitions[0].get('definition_short', '').lower()
            golden_short = golden.get('definition_short', '').lower()
            common_words = set(ai_short.split()) & set(golden_short.split())
            similarity = len(common_words) / max(len(set(ai_short.split()) | set(golden_short.split())), 1)
            print(f"  Jaccard相似度: {similarity:.2%}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
