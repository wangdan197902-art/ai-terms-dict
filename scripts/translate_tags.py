#!/usr/bin/env python3
"""
P0b-Step2: 标签批量翻译
- 从英文术语提取所有唯一标签（909个）
- 批量翻译到 25 个非英语种（每批 50 个标签 × 1 语种 = 1 次 API 调用）
- 支持断点续传和限流退避
- 输出: data/tag_translations.json

使用方式: python3 scripts/translate_tags.py [--batch-size 50] [--concurrency 3]
"""

import os
import sys
import json
import time
import yaml
import argparse
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config
from scripts.utils.agnes_client import get_client

PROJECT_ROOT = Path(__file__).parent.parent
CONTENT_DIR = PROJECT_ROOT / "content"
OUTPUT_FILE = PROJECT_ROOT / "data" / "tag_translations.json"
PROGRESS_FILE = PROJECT_ROOT / "data" / "tag_translation_progress.json"

# 25 个非英语种
TARGET_LANGS = [
    "es", "de", "ja", "fr", "zh", "pt", "ru", "ko", "ar",
    "it", "nl", "pl", "tr", "vi", "th", "id", "sv", "cs", "da",
    "fi", "no", "he", "ro", "hu", "el"
]

# 语种英文名（用于 prompt）
LANG_NAMES = {
    "es": "Spanish", "de": "German", "ja": "Japanese",
    "fr": "French", "zh": "Chinese (Simplified)",
    "pt": "Portuguese (Brazilian)", "ru": "Russian", "ko": "Korean",
    "ar": "Arabic", "it": "Italian", "nl": "Dutch",
    "pl": "Polish", "tr": "Turkish", "vi": "Vietnamese",
    "th": "Thai", "id": "Indonesian", "sv": "Swedish",
    "cs": "Czech", "da": "Danish", "fi": "Finnish",
    "no": "Norwegian", "he": "Hebrew", "ro": "Romanian",
    "hu": "Hungarian", "el": "Greek",
}


def extract_unique_tags() -> list:
    """从英文术语提取所有唯一标签"""
    all_tags = set()
    for md_file in (CONTENT_DIR / "en" / "terms").glob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    fm = yaml.safe_load(parts[1])
                    if fm and 'tags' in fm and isinstance(fm['tags'], list):
                        for tag in fm['tags']:
                            if tag and isinstance(tag, str):
                                all_tags.add(tag.strip())
        except Exception:
            pass
    return sorted(all_tags)


def load_existing_translations() -> dict:
    """加载已存在的翻译（断点续传）"""
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_translations(translations: dict):
    """保存翻译到文件"""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)


def save_progress(lang: str, batch_idx: int, total_batches: int):
    """保存进度"""
    progress = {}
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            progress = json.load(f)
    progress[lang] = {
        "last_batch": batch_idx,
        "total_batches": total_batches,
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def build_batch_translate_messages(tags: list, target_lang: str) -> list:
    """构建批量翻译 messages"""
    lang_name = LANG_NAMES[target_lang]

    system_prompt = f"""You are a professional technical translator specializing in AI/ML terminology.

Task: Translate the following English AI/ML tags to {lang_name}.

Rules:
1. Each tag is a short label (1-4 words) related to AI/ML
2. Translate to natural {lang_name} phrasing used by native AI practitioners
3. Keep well-known acronyms in English (NLP, LLM, AI, ML, GPT, BERT, CNN, RNN, GAN, GPU, TPU, API, AGI, RL, SVM, KNN, PCA, SGD, RAG, RLHF, DPO, MLP)
4. For proper nouns (library names like HuggingFace, PyTorch, TensorFlow), keep in English
5. Respond ONLY in valid JSON: {{"translations": [{{"en": "original_tag", "{target_lang}": "translated_tag"}}]}}
6. Translate ALL tags in the input list, no omissions"""

    user_prompt = f"Translate these {len(tags)} English tags to {lang_name}:\n\n"
    for i, tag in enumerate(tags, 1):
        user_prompt += f"{i}. {tag}\n"

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def translate_batch(client, tags: list, target_lang: str, max_retries: int = 3) -> dict:
    """翻译一批标签，返回 {en_tag: translated_tag}"""
    messages = build_batch_translate_messages(tags, target_lang)

    for attempt in range(max_retries):
        try:
            # 使用 chat_json 方法（自动处理 JSON 模式和降级）
            data = client.chat_json(messages=messages, temperature=0.3)

            # 检查是否出错
            if "error" in data:
                print(f"    ⚠ JSON 解析失败: {data.get('error')}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue
                return {}

            translations_list = data.get("translations", [])

            result = {}
            for item in translations_list:
                en_tag = item.get("en", "").strip()
                translated = item.get(target_lang, "").strip()
                if en_tag and translated:
                    result[en_tag] = translated

            # 验证：确保所有标签都被翻译
            if len(result) >= len(tags) * 0.9:  # 允许 10% 丢失
                return result
            else:
                print(f"    ⚠ 翻译不完整: {len(result)}/{len(tags)}，重试 {attempt+1}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue

            return result

        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "rate" in err_str.lower():
                wait_time = 30 * (attempt + 1)
                print(f"    ⚠ API 限流，等待 {wait_time}秒后重试 ({attempt+1}/{max_retries})")
                time.sleep(wait_time)
            else:
                print(f"    ✗ 翻译出错: {e}")
                if attempt < max_retries - 1:
                    time.sleep(10)
                    continue
                return {}

    return {}


def translate_lang_all_tags(client, lang: str, all_tags: list, batch_size: int = 50) -> dict:
    """翻译单个语种的所有标签"""
    print(f"\n[{lang}] 开始翻译 {len(all_tags)} 个标签...")

    # 分批
    batches = [all_tags[i:i+batch_size] for i in range(0, len(all_tags), batch_size)]
    total_batches = len(batches)

    # 加载已有进度
    progress = {}
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            progress = json.load(f)
    last_batch = progress.get(lang, {}).get("last_batch", -1)

    lang_translations = {}
    success_count = 0
    fail_count = 0

    for batch_idx, batch in enumerate(batches):
        if batch_idx <= last_batch:
            print(f"  [{lang}] 批次 {batch_idx+1}/{total_batches} 已完成，跳过")
            continue

        print(f"  [{lang}] 批次 {batch_idx+1}/{total_batches}: 翻译 {len(batch)} 个标签...")

        result = translate_batch(client, batch, lang)
        if result:
            lang_translations.update(result)
            success_count += len(result)
            print(f"    ✓ 成功 {len(result)}/{len(batch)}")
        else:
            fail_count += len(batch)
            print(f"    ✗ 失败 {len(batch)} 个")

        # 保存进度
        save_progress(lang, batch_idx, total_batches)

        # 批次间间隔
        time.sleep(2)

    print(f"[{lang}] 完成: 成功 {success_count}, 失败 {fail_count}")
    return lang_translations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=50, help="每批翻译标签数")
    parser.add_argument("--lang", type=str, help="只翻译指定语种（用于测试）")
    args = parser.parse_args()

    print("=" * 60)
    print("🏷️  标签批量翻译")
    print("=" * 60)

    # 1. 提取唯一标签
    print("\n📋 提取英文唯一标签...")
    all_tags = extract_unique_tags()
    print(f"  唯一标签数: {len(all_tags)}")

    # 2. 加载已有翻译
    print("\n📂 加载已有翻译...")
    translations = load_existing_translations()
    existing_count = sum(len(v) for v in translations.values())
    print(f"  已翻译: {existing_count} 条")

    # 3. 初始化 AGNES 客户端
    print("\n🔌 初始化 AGNES 客户端...")
    try:
        client = get_client()
        print(f"  ✓ 客户端就绪")
    except Exception as e:
        print(f"  ✗ 初始化失败: {e}")
        return

    # 4. 翻译
    target_langs = [args.lang] if args.lang else TARGET_LANGS

    total_api_calls = sum((len(all_tags) + args.batch_size - 1) // args.batch_size for _ in target_langs)
    print(f"\n🚀 开始翻译: {len(target_langs)} 语种 × {len(all_tags)} 标签")
    print(f"  预计 API 调用: {total_api_calls} 次（每批 {args.batch_size} 标签）")
    print(f"  比逐个翻译节省: {len(all_tags) * len(target_langs) - total_api_calls} 次")

    for lang in target_langs:
        if lang not in translations:
            translations[lang] = {}

        # 过滤已翻译的
        existing_for_lang = translations[lang]
        tags_to_translate = [t for t in all_tags if t not in existing_for_lang]

        if not tags_to_translate:
            print(f"\n[{lang}] 所有标签已翻译，跳过")
            continue

        print(f"\n[{lang}] 待翻译: {len(tags_to_translate)}/{len(all_tags)}")

        lang_result = translate_lang_all_tags(client, lang, tags_to_translate, args.batch_size)
        translations[lang].update(lang_result)

        # 保存
        save_translations(translations)
        print(f"[{lang}] 已保存到 {OUTPUT_FILE.name}")

    # 5. 统计
    print("\n" + "=" * 60)
    print("✅ 翻译完成")
    print("=" * 60)
    for lang in target_langs:
        count = len(translations.get(lang, {}))
        print(f"  {lang}: {count}/{len(all_tags)} ({count/len(all_tags)*100:.1f}%)")

    total = sum(len(v) for v in translations.values())
    print(f"\n  总翻译条目: {total}")
    print(f"  输出文件: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
