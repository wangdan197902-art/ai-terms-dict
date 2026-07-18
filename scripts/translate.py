#!/usr/bin/env python3
"""多语种翻译。

将英文术语定义翻译为目标语种。
"""
import sys
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config
from scripts.utils.agnes_client import get_client
from scripts.prompts.translation_prompt import build_messages


def load_definitions() -> list:
    """加载已生成的定义。"""
    with open(config.paths.generated_definitions_file, "r", encoding="utf-8") as f:
        return json.load(f)


def translate_definition(definition: dict, target_lang: str) -> dict:
    """翻译单个定义到目标语种。"""
    client = get_client()
    messages = build_messages(definition, target_lang)
    print(f"  翻译到 {target_lang}: {definition['english']}...")
    result = client.chat_json(messages, temperature=0.3)

    # 确保关键字段存在
    result["term_id"] = definition["term_id"]
    result["language"] = target_lang
    result["source_language"] = "en"
    result["target_language"] = target_lang
    result["source"] = "agnes_llm"
    result["generated_at"] = datetime.utcnow().isoformat() + "Z"
    result["model"] = config.agnes.model

    return result


def update_glossary(translations: list) -> None:
    """更新术语翻译记忆库。"""
    glossary_path = config.paths.glossary_file
    glossary = {}
    if glossary_path.exists():
        with open(glossary_path, "r", encoding="utf-8") as f:
            glossary = json.load(f)

    for t in translations:
        term_id = t["term_id"]
        lang = t["language"]
        if term_id not in glossary:
            glossary[term_id] = {"en": ""}
        glossary[term_id][lang] = t.get("term_name", "")
        if "en" not in glossary[term_id] or not glossary[term_id]["en"]:
            glossary[term_id]["en"] = t.get("english", "")

    config.paths.translations_dir.mkdir(parents=True, exist_ok=True)
    with open(glossary_path, "w", encoding="utf-8") as f:
        json.dump(glossary, f, ensure_ascii=False, indent=2)
    print(f"  ✓ 术语记忆库已更新: {glossary_path}")


def main():
    print("=" * 60)
    print("Step 01-02: 单术语多语种翻译")
    print("=" * 60)

    definitions = load_definitions()
    target_langs = config.get_target_languages()  # ["es", "de", "ja", "fr", "zh"]
    print(f"目标语种: {target_langs}")
    print(f"待翻译术语: {[d['english'] for d in definitions]}")

    all_translations = []
    for definition in definitions:
        print(f"\n处理术语: {definition['english']}")
        # 添加英文原版到翻译列表
        en_version = definition.copy()
        en_version["language"] = "en"
        en_version["term_name"] = definition["english"]
        en_version["source_language"] = "en"
        en_version["target_language"] = "en"
        all_translations.append(en_version)

        # 翻译到5个目标语种
        for lang in target_langs:
            try:
                translation = translate_definition(definition, lang)
                all_translations.append(translation)
                print(f"    ✓ {lang}: {translation.get('term_name', 'N/A')}")
            except Exception as e:
                print(f"    ✗ {lang}: 翻译失败 - {e}")
                # 兜底：使用Mock
                mock_path = config.paths.mock_dir / f"{definition['term_id']}_{lang}.json"
                if mock_path.exists():
                    print(f"    ⚠ 降级使用Mock: {mock_path}")
                    with open(mock_path, "r", encoding="utf-8") as f:
                        mock = json.load(f)
                    mock["source"] = "mock_fallback"
                    all_translations.append(mock)

    # 保存
    output_file = config.paths.translated_terms_file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 已生成 {len(all_translations)} 条翻译（含英文原版）")
    print(f"  输出: {output_file}")

    # 更新术语记忆库
    update_glossary(all_translations)

    # 翻译完整性校验
    expected = len(definitions) * (len(target_langs) + 1)  # +1 for English
    actual = len(all_translations)
    if actual == expected:
        print(f"\n✓ 翻译完整性: {actual}/{expected}")
    else:
        print(f"\n⚠ 翻译完整性: {actual}/{expected} (部分失败)")

    return 0 if actual == expected else 1


if __name__ == "__main__":
    sys.exit(main())
