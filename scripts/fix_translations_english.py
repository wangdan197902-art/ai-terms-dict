#!/usr/bin/env python3
"""修复translated_terms.json中非英文翻译缺english字段的问题。

问题原因：
- 英文版（language=en）条目有english字段
- 其他5语种翻译只有term_name（翻译后名称），缺english字段
- 同样缺category/difficulty/tags/code_example等字段

修复策略：
- 遍历所有翻译条目
- 对非英文条目，从相同term_id的英文条目复制english字段和其他元数据
"""
import json
import sys
from pathlib import Path
from collections import defaultdict


def main():
    project_root = Path(__file__).parent.parent
    trans_file = project_root / "data" / "queue" / "translated_terms.json"

    print(f"加载: {trans_file}")
    with open(trans_file, "r", encoding="utf-8") as f:
        translations = json.load(f)

    print(f"总翻译数: {len(translations)}")

    # 按term_id分组，找到每个term_id的英文版
    by_term = defaultdict(list)
    for t in translations:
        by_term[t.get("term_id")].append(t)

    # 构建english字段查找表
    english_lookup = {}
    for term_id, items in by_term.items():
        for item in items:
            if item.get("language") == "en":
                english_lookup[term_id] = item
                break

    print(f"找到英文基准: {len(english_lookup)} 术语")

    # 修复非英文条目
    fixed_count = 0
    for t in translations:
        if t.get("language") == "en":
            continue  # 英文版跳过

        term_id = t.get("term_id")
        en_base = english_lookup.get(term_id)

        if en_base:
            # 补充缺失字段
            if not t.get("english"):
                t["english"] = en_base.get("english", "")
                fixed_count += 1
            # 补充其他元数据（不覆盖已有值）
            for field in ["category", "subcategory", "difficulty", "tags",
                          "code_example", "source"]:
                if field not in t or not t.get(field):
                    if en_base.get(field):
                        t[field] = en_base[field]

    print(f"✓ 修复english字段: {fixed_count} 条")

    # 保存
    with open(trans_file, "w", encoding="utf-8") as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    print(f"✓ 已保存: {trans_file}")

    # 验证
    with open(trans_file, "r", encoding="utf-8") as f:
        verify = json.load(f)
    no_english = [t for t in verify if not t.get("english")]
    print(f"验证: 缺english字段 = {len(no_english)} 条")

    return 0 if len(no_english) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
