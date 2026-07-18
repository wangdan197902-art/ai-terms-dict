#!/usr/bin/env python3
"""校验种子数据完整性。

校验项：
- term_id 唯一性
- 必填字段（term_id, english, category, importance）
- importance 范围 1-5
- category 在5大分类内
"""
import json
import sys
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent.parent
SEED_FILE = BASE / "data" / "seeds" / "seed_terms.json"

VALID_CATEGORIES = {
    "basic_concepts",
    "training_techniques",
    "application_paradigms",
    "engineering_practice",
    "ethics_safety",
}
REQUIRED_FIELDS = ["term_id", "english", "category", "importance"]


def main():
    if not SEED_FILE.exists():
        print(f"❌ 校验失败：种子文件不存在 {SEED_FILE}")
        sys.exit(1)

    with open(SEED_FILE, "r", encoding="utf-8") as f:
        seeds = json.load(f)

    errors = []
    warnings = []

    # 1. 总数检查
    total = len(seeds)
    if total != 200:
        errors.append(f"术语总数应为 200，实际为 {total}")

    # 2. term_id 唯一性
    term_ids = [s.get("term_id") for s in seeds if isinstance(s, dict)]
    id_counts = Counter(term_ids)
    duplicates = [tid for tid, cnt in id_counts.items() if cnt > 1]
    if duplicates:
        errors.append(f"term_id 重复：{duplicates}")

    # 3. 逐条校验
    for idx, s in enumerate(seeds):
        if not isinstance(s, dict):
            errors.append(f"第 {idx} 条记录不是对象")
            continue
        # 必填字段
        for field in REQUIRED_FIELDS:
            if field not in s or s[field] is None or s[field] == "":
                errors.append(f"第 {idx} 条记录缺失必填字段：{field}")
        # importance 范围
        if "importance" in s:
            imp = s["importance"]
            if not isinstance(imp, int) or imp < 1 or imp > 5:
                errors.append(f"第 {idx} 条记录 importance 超出范围 1-5：{imp}")
        # category 合法性
        if "category" in s and s["category"] not in VALID_CATEGORIES:
            errors.append(f"第 {idx} 条记录 category 非法：{s['category']}")
        # term_id 格式（小写下划线）
        if "term_id" in s:
            tid = s["term_id"]
            if not isinstance(tid, str) or not tid:
                errors.append(f"第 {idx} 条记录 term_id 为空")
            elif tid != tid.lower() or " " in tid:
                warnings.append(f"第 {idx} 条 term_id 非小写下划线格式：{tid}")

    # 4. 分类统计
    cat_counts = Counter(s.get("category") for s in seeds if isinstance(s, dict))
    print("=" * 50)
    print("种子数据校验报告")
    print("=" * 50)
    print(f"总术语数: {total}")
    print("\n分类统计:")
    for cat in VALID_CATEGORIES:
        print(f"  {cat}: {cat_counts.get(cat, 0)}")
    other_cats = set(cat_counts.keys()) - VALID_CATEGORIES
    if other_cats:
        for cat in other_cats:
            print(f"  [未知] {cat}: {cat_counts.get(cat, 0)}")

    print("\n校验结果:")
    if warnings:
        print(f"  ⚠️ 警告 {len(warnings)} 条:")
        for w in warnings[:10]:
            print(f"    - {w}")
    if errors:
        print(f"  ❌ 错误 {len(errors)} 条:")
        for e in errors[:20]:
            print(f"    - {e}")
        print("\n❌ 校验失败")
        sys.exit(1)
    else:
        print("  ✅ 校验通过")
        sys.exit(0)


if __name__ == "__main__":
    main()
