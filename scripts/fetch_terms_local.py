#!/usr/bin/env python3
"""从本地种子库读取术语，输出待处理队列。"""
import json
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent.parent
SEED_FILE = BASE / "data" / "seeds" / "seed_terms.json"
OUTPUT_FILE = BASE / "data" / "queue" / "pending_terms.json"


def main():
    with open(SEED_FILE, "r", encoding="utf-8") as f:
        seeds = json.load(f)
    # 按importance降序，同分按字母升序
    seeds_sorted = sorted(seeds, key=lambda x: (-x["importance"], x["english"]))
    # 统计
    stats = defaultdict(int)
    for s in seeds_sorted:
        stats[s["category"]] += 1
    output = {
        "total": len(seeds_sorted),
        "stats_by_category": dict(stats),
        "terms": seeds_sorted,
    }
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"已输出 {len(seeds_sorted)} 条术语到 {OUTPUT_FILE}")
    print("分类统计:")
    for cat, cnt in stats.items():
        print(f"  {cat}: {cnt}")


if __name__ == "__main__":
    main()
