#!/usr/bin/env python3
"""为剩余术语生成Mock Markdown内容。"""
import sys
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config
from scripts.build_content import write_markdown, LANG_TO_CONTENT_DIR


def main():
    print("=" * 60)
    print("为剩余术语生成Mock内容")
    print("=" * 60)

    # 加载已生成的真实翻译（避免重复）
    with open(config.paths.translated_terms_file, "r", encoding="utf-8") as f:
        real_translations = json.load(f)
    real_term_ids = set(t["term_id"] for t in real_translations if t["language"] == "en")
    print(f"已有真实内容术语: {len(real_term_ids)} 个")

    # 加载全部种子
    with open(config.paths.seed_file, "r", encoding="utf-8") as f:
        seeds = json.load(f)

    # 找出需要Mock的术语
    mock_terms = [s for s in seeds if s["term_id"] not in real_term_ids]
    print(f"需要Mock的术语: {len(mock_terms)} 个")

    # 为每个语种生成Mock
    langs = config.get_supported_languages()
    written = 0
    for term in mock_terms:
        for lang in langs:
            # 构造Mock数据
            mock = {
                "term_id": term["term_id"],
                "language": lang,
                "term_name": term["english"],  # Mock保留英文术语名
                "definition_short": f"[Preview] {term['english']} - AI term in {term['category']} category.",
                "definition_long": f"[Machine Translation Preview] This is a placeholder definition for {term['english']}. The full AI-generated definition will be available soon. Category: {term['category']}. Importance: {term.get('importance', 3)}/5.",
                "key_concepts": ["Concept 1", "Concept 2", "Concept 3"],
                "use_cases": ["Use case 1", "Use case 2"],
                "related_terms": [],
                "code_example": None,
                "category": term["category"],
                "subcategory": "",
                "difficulty": 3,
                "tags": [term["category"], "preview"],
                "source": "mock",
                "status": "preview",
                "generated_at": datetime.utcnow().isoformat() + "Z",
            }
            try:
                filepath = write_markdown(mock, lang)
                written += 1
            except Exception as e:
                print(f"  ✗ {term['term_id']}_{lang}: {e}")

    print(f"\n✓ 已生成 {written} 个Mock Markdown文件")
    print(f"  总计内容: {len(real_term_ids)} 真实 + {len(mock_terms)} Mock = {len(real_term_ids) + len(mock_terms)} 术语 × {len(langs)} 语种")

if __name__ == "__main__":
    main()
