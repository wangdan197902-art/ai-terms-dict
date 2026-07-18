#!/usr/bin/env python3
"""批量翻译术语定义。

将英文定义批量翻译为目标语种。
支持断点续传：按(term_id, lang)维度去重，已翻译的跳过。
支持错误隔离：单批次失败不影响其他。
"""
import sys
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config
from scripts.utils.agnes_client import get_client


BATCH_TRANSLATE_SIZE = 5  # 每次翻译5个术语到1个语种
PROGRESS_FILE = config.paths.progress_dir / "trans_progress.json"
FAILED_FILE = config.paths.queue_dir / "failed_translations.json"


def load_existing_translations() -> list:
    """加载已存在的翻译（用于断点续传）。

    合并主文件 + 所有语种子文件，确保断点续传完整。
    """
    all_translations = []

    # 主文件（向后兼容）
    trans_file = config.paths.translated_terms_file
    if trans_file.exists():
        with open(trans_file, "r", encoding="utf-8") as f:
            all_translations.extend(json.load(f))

    # 语种子文件（并行模式）
    queue_dir = config.paths.queue_dir
    for lang_file in queue_dir.glob("translated_terms_*.json"):
        with open(lang_file, "r", encoding="utf-8") as f:
            all_translations.extend(json.load(f))

    # 去重（按 term_id + language）
    seen = set()
    unique = []
    for t in all_translations:
        key = (t.get("term_id"), t.get("language"))
        if key not in seen:
            seen.add(key)
            unique.append(t)
    return unique


def get_translated_keys(translations: list) -> set:
    """获取已翻译的(term_id, lang)键集合。"""
    return {(t.get("term_id"), t.get("language")) for t in translations}


def save_lang_translations(translations: list, lang: str):
    """保存单语种翻译到独立文件（避免并行冲突）。"""
    lang_file = config.paths.queue_dir / f"translated_terms_{lang}.json"
    # 只保存该语种的翻译
    lang_translations = [t for t in translations if t.get("language") == lang]
    with open(lang_file, "w", encoding="utf-8") as f:
        json.dump(lang_translations, f, ensure_ascii=False, indent=2)


def save_progress(translated_count: int, total: int, failed_keys: list, lang: str = ""):
    """保存翻译进度。"""
    progress_file = PROGRESS_FILE if not lang else (
        config.paths.progress_dir / f"trans_progress_{lang}.json"
    )
    progress = {
        "translated_count": translated_count,
        "total": total,
        "failed_keys": failed_keys,
        "lang": lang,
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    progress_file.parent.mkdir(parents=True, exist_ok=True)
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


BATCH_TRANSLATE_SYSTEM = """You are a professional technical translator for AI/ML content.

Rules:
1. Translate term_name, definition_short, definition_long, key_concepts, use_cases
2. Keep code_example, term_id, related_terms in English (add native explanation in parentheses for related_terms)
3. Use natural, native-speaker phrasing
4. Respond ONLY in valid JSON: {"translations": [{"term_id": "...", "term_name": "...", "definition_short": "...", "definition_long": "...", "key_concepts": [...], "use_cases": [...], "related_terms": [...]}]}"""


def build_batch_translate_messages(definitions: list, target_lang: str) -> list:
    """构建批量翻译messages。"""
    lang_names = {
        "es": "Spanish", "de": "German", "ja": "Japanese",
        "fr": "French", "zh": "Chinese (Simplified)",
        "pt": "Portuguese (Brazilian)", "ru": "Russian", "ko": "Korean",
        "ar": "Arabic", "hi": "Hindi", "it": "Italian", "nl": "Dutch",
        "pl": "Polish", "tr": "Turkish", "vi": "Vietnamese", "th": "Thai",
        "id": "Indonesian", "uk": "Ukrainian", "sv": "Swedish",
        "cs": "Czech", "da": "Danish", "fi": "Finnish", "no": "Norwegian",
        "he": "Hebrew", "ro": "Romanian", "hu": "Hungarian",
        "el": "Greek", "bg": "Bulgarian", "hr": "Croatian",
    }
    defs_summary = json.dumps([
        {
            "term_id": d["term_id"],
            "term_name": d.get("english", ""),
            "definition_short": d.get("definition_short", ""),
            "definition_long": d.get("definition_long", "")[:200],  # 截断以节省token
            "key_concepts": d.get("key_concepts", []),
            "use_cases": d.get("use_cases", []),
            "related_terms": d.get("related_terms", []),
        }
        for d in definitions
    ], ensure_ascii=False, indent=2)

    user_msg = f"""Translate the following {len(definitions)} AI term definitions to {lang_names.get(target_lang, target_lang)} ({target_lang}).

Source definitions:
{defs_summary}

Output JSON: {{"translations": [{{"term_id": "...", "term_name": "translated name", "definition_short": "translated short", "definition_long": "translated long (full translation)", "key_concepts": ["translated concept"], "use_cases": ["translated use case"], "related_terms": ["English term (native explanation)"]}}]}}

Respond ONLY with valid JSON."""

    return [
        {"role": "system", "content": BATCH_TRANSLATE_SYSTEM},
        {"role": "user", "content": user_msg},
    ]


def parse_args():
    """解析命令行参数。"""
    import argparse
    parser = argparse.ArgumentParser(description="批量翻译术语定义")
    parser.add_argument(
        "--langs",
        type=str,
        default="",
        help="目标语种，逗号分隔（如 es,de）。默认全部目标语种。",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=BATCH_TRANSLATE_SIZE,
        help=f"批量大小，默认{BATCH_TRANSLATE_SIZE}",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # 解析目标语种
    if args.langs:
        target_langs = [l.strip() for l in args.langs.split(",") if l.strip()]
    else:
        target_langs = config.get_target_languages()  # es, de, ja, fr, zh

    # 全局批量大小
    global BATCH_TRANSLATE_SIZE
    BATCH_TRANSLATE_SIZE = args.batch_size

    print("=" * 60)
    print(f"Step 02-01b: 批量翻译（支持断点续传）")
    print(f"  目标语种: {target_langs}")
    print(f"  批量大小: {BATCH_TRANSLATE_SIZE}")
    print("=" * 60)

    # 加载已生成的定义
    with open(config.paths.generated_definitions_file, "r", encoding="utf-8") as f:
        definitions = json.load(f)

    # 加载已有翻译（断点续传）
    existing_translations = load_existing_translations()
    existing_keys = get_translated_keys(existing_translations)
    print(f"已存在翻译: {len(existing_keys)} 条")
    print(f"待翻译定义: {len(definitions)} 条")
    print(f"目标语种: {target_langs}")

    client = get_client()
    new_translations = []
    failed_keys = []
    batch_count = 0
    expected_total = len(definitions) * (1 + len(target_langs))  # en + 5翻译
    total_batches = len(target_langs) * ((len(definitions) + BATCH_TRANSLATE_SIZE - 1) // BATCH_TRANSLATE_SIZE)
    print(f"预计API调用: {total_batches} 次（已存在 {len(existing_keys)} 条将跳过）")

    # 添加英文原版（如果不存在）—— 仅当目标语种包含 en 时
    if "en" in target_langs or not target_langs:
        for defn in definitions:
            key = (defn["term_id"], "en")
            if key in existing_keys:
                continue
            en_version = defn.copy()
            en_version["language"] = "en"
            en_version["term_name"] = defn.get("english", "")
            en_version["source_language"] = "en"
            en_version["target_language"] = "en"
            en_version["source"] = "agnes_llm"
            new_translations.append(en_version)
            existing_keys.add(key)
        # 保存英文到独立文件
        if new_translations:
            en_new = [t for t in new_translations if t.get("language") == "en"]
            if en_new:
                en_file = config.paths.queue_dir / "translated_terms_en.json"
                # 合并已有英文翻译
                en_existing = [t for t in existing_translations if t.get("language") == "en"]
                all_en = en_existing + en_new
                # 去重
                seen_ids = set()
                unique_en = []
                for t in all_en:
                    if t["term_id"] not in seen_ids:
                        seen_ids.add(t["term_id"])
                        unique_en.append(t)
                with open(en_file, "w", encoding="utf-8") as f:
                    json.dump(unique_en, f, ensure_ascii=False, indent=2)
                print(f"  ✓ 英文翻译保存: {len(unique_en)} 条")

    # 批量翻译到每个语种
    for lang in target_langs:
        if lang == "en":
            continue  # en已处理
        print(f"\n[翻译到 {lang}]")
        # 过滤掉已翻译的
        pending = [d for d in definitions if (d["term_id"], lang) not in existing_keys]
        if not pending:
            print(f"  ✓ {lang} 已全部翻译，跳过")
            continue

        # 该语种的进度统计
        lang_new = []
        lang_failed = []
        lang_total = len(pending)
        lang_batches = (lang_total + BATCH_TRANSLATE_SIZE - 1) // BATCH_TRANSLATE_SIZE
        print(f"  待翻译: {lang_total} 条，预计 {lang_batches} 批次")

        for batch_idx in range(0, len(pending), BATCH_TRANSLATE_SIZE):
            batch = pending[batch_idx:batch_idx + BATCH_TRANSLATE_SIZE]
            batch_count += 1
            current_batch = batch_idx // BATCH_TRANSLATE_SIZE + 1
            print(f"  [{lang}] 批次 {current_batch}/{lang_batches}: {[d.get('english', 'N/A') for d in batch]}", flush=True)

            try:
                messages = build_batch_translate_messages(batch, lang)
                result = client.chat_json(messages, temperature=0.3)

                if "translations" in result:
                    for i, trans in enumerate(result["translations"]):
                        if i < len(batch):
                            trans["term_id"] = batch[i]["term_id"]
                            trans["language"] = lang
                            trans["source_language"] = "en"
                            trans["target_language"] = lang
                            trans["source"] = "agnes_llm"
                            trans["generated_at"] = datetime.utcnow().isoformat() + "Z"
                            trans["model"] = config.agnes.model
                            trans["category"] = batch[i].get("category", "")
                            trans["difficulty"] = batch[i].get("difficulty", 3)
                            trans["tags"] = batch[i].get("tags", [])
                            trans["code_example"] = batch[i].get("code_example")
                            trans["english"] = batch[i].get("english", "")  # 保留原英文
                            new_translations.append(trans)
                            lang_new.append(trans)
                            existing_keys.add((trans["term_id"], lang))
                else:
                    print(f"    ⚠ 响应格式异常", flush=True)
                    for term in batch:
                        failed_keys.append({"term_id": term["term_id"], "lang": lang})
                        lang_failed.append({"term_id": term["term_id"], "lang": lang})
            except Exception as e:
                print(f"    ✗ 批次失败: {e}", flush=True)
                for term in batch:
                    failed_keys.append({"term_id": term["term_id"], "lang": lang})
                    lang_failed.append({"term_id": term["term_id"], "lang": lang})

            # 每10批次保存一次（语种独立文件，无冲突）
            if current_batch % 10 == 0:
                # 加载该语种已有翻译
                lang_file = config.paths.queue_dir / f"translated_terms_{lang}.json"
                lang_existing = []
                if lang_file.exists():
                    with open(lang_file, "r", encoding="utf-8") as f:
                        lang_existing = json.load(f)
                # 合并去重
                all_lang = lang_existing + lang_new
                seen = set()
                unique = []
                for t in all_lang:
                    k = (t.get("term_id"), t.get("language"))
                    if k not in seen:
                        seen.add(k)
                        unique.append(t)
                with open(lang_file, "w", encoding="utf-8") as f:
                    json.dump(unique, f, ensure_ascii=False, indent=2)
                save_progress(len(unique), lang_total, lang_failed, lang=lang)
                print(f"    💾 [{lang}] 进度: {len(unique)}/{lang_total}", flush=True)

        # 该语种最终保存
        lang_file = config.paths.queue_dir / f"translated_terms_{lang}.json"
        lang_existing = []
        if lang_file.exists():
            with open(lang_file, "r", encoding="utf-8") as f:
                lang_existing = json.load(f)
        all_lang = lang_existing + lang_new
        seen = set()
        unique = []
        for t in all_lang:
            k = (t.get("term_id"), t.get("language"))
            if k not in seen:
                seen.add(k)
                unique.append(t)
        with open(lang_file, "w", encoding="utf-8") as f:
            json.dump(unique, f, ensure_ascii=False, indent=2)
        save_progress(len(unique), lang_total, lang_failed, lang=lang)
        print(f"  ✓ [{lang}] 完成: {len(unique)} 条（失败 {len(lang_failed)}）", flush=True)

    # 合并所有语种到主文件（仅当未指定 --langs 时）
    if not args.langs:
        all_translations = load_existing_translations()
        output_file = config.paths.translated_terms_file
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_translations, f, ensure_ascii=False, indent=2)

    # 保存失败列表
    if failed_keys:
        with open(FAILED_FILE, "w", encoding="utf-8") as f:
            json.dump(failed_keys, f, ensure_ascii=False, indent=2)

    # 统计
    all_translations = load_existing_translations()
    actual = len(all_translations)
    print(f"\n✓ 共新增 {len(new_translations)} 条翻译（总计 {actual}/{expected_total}）")
    print(f"  失败: {len(failed_keys)} 条")

    # 按语种统计
    from collections import Counter
    lang_counts = Counter(t["language"] for t in all_translations)
    print(f"  语种分布: {dict(lang_counts)}")

    # 更新术语记忆库（仅当未指定 --langs 时）
    if not args.langs:
        glossary_path = config.paths.glossary_file
        glossary = {}
        if glossary_path.exists():
            with open(glossary_path, "r", encoding="utf-8") as f:
                glossary = json.load(f)
        for t in all_translations:
            term_id = t["term_id"]
            lang = t["language"]
            if term_id not in glossary:
                glossary[term_id] = {}
            glossary[term_id][lang] = t.get("term_name", "")
        with open(glossary_path, "w", encoding="utf-8") as f:
            json.dump(glossary, f, ensure_ascii=False, indent=2)
        print(f"  术语记忆库: {glossary_path}")

    return 0 if actual >= expected_total * 0.8 else 1


if __name__ == "__main__":
    sys.exit(main())
