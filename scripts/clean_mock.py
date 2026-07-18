#!/usr/bin/env python3
"""清理Mock内容。

清理：
1. data/mock/ 目录下的所有Mock JSON文件
2. content/{lang}/{terms_dir}/ 目录下的所有Mock Markdown文件（保留_index.md）
3. data/queue/ 中的mock相关文件

保留：
- content/{lang}/_index.md
- content/{lang}/categories/_index.md
- content/{lang}/search/_index.md (或对应语种的搜索目录)
- content/{lang}/terms/_index.md 等
"""
import sys
import json
import shutil
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent


# 各语种的术语目录名
LANG_TERM_DIRS = {
    "en": "terms",
    "es": "terminos",
    "de": "begriffe",
    "ja": "用語",
    "fr": "termes",
    "zh": "术语",
}

# 各语种的列表页目录（保留_index.md）
LIST_DIRS = ["categories", "search", "buscar", "categorias", "kategorien", "suche", "categorie"]


def clean_mock_data():
    """清理data/mock/目录。"""
    mock_dir = PROJECT_ROOT / "data" / "mock"
    if mock_dir.exists():
        file_count = len(list(mock_dir.glob("*.json")))
        shutil.rmtree(mock_dir)
        print(f"  ✓ 清理 data/mock/: {file_count} 个文件")
        # 重新创建空目录
        mock_dir.mkdir(parents=True, exist_ok=True)
    else:
        print(f"  ℹ data/mock/ 不存在")


def clean_mock_markdown():
    """清理content/{lang}/{terms_dir}/下的Mock Markdown。

    保留：
    - _index.md
    - 真实AI生成的Markdown（term_id在translated_terms.json中）
    """
    # 加载真实翻译的term_id集合
    trans_file = PROJECT_ROOT / "data" / "queue" / "translated_terms.json"
    real_term_ids = set()
    if trans_file.exists():
        with open(trans_file, "r", encoding="utf-8") as f:
            translations = json.load(f)
        real_term_ids = {t["term_id"] for t in translations}
        print(f"  真实术语数: {len(real_term_ids)}")

    total_removed = 0
    content_dir = PROJECT_ROOT / "content"

    for lang, term_dir_name in LANG_TERM_DIRS.items():
        term_dir = content_dir / lang / term_dir_name
        if not term_dir.exists():
            continue

        removed = 0
        kept = 0
        for md_file in term_dir.glob("*.md"):
            if md_file.name == "_index.md":
                kept += 1
                continue

            # 提取term_id（文件名去掉.md）
            term_id = md_file.stem

            # 如果不在真实翻译中，删除
            if term_id not in real_term_ids:
                md_file.unlink()
                removed += 1
            else:
                kept += 1

        print(f"  {lang}/{term_dir_name}/: 删除 {removed} 个Mock，保留 {kept} 个真实")
        total_removed += removed

    print(f"  ✓ 总共清理Mock Markdown: {total_removed} 个")
    return total_removed


def clean_mock_queue():
    """清理queue中的mock文件。"""
    queue_dir = PROJECT_ROOT / "data" / "queue"
    mock_queue_files = [
        "mock_terms.json",
        "mock_definitions.json",
    ]
    for fname in mock_queue_files:
        fpath = queue_dir / fname
        if fpath.exists():
            fpath.unlink()
            print(f"  ✓ 清理 {fpath}")


def main():
    print("=" * 60)
    print("清理Mock内容")
    print("=" * 60)

    print("\n[1] 清理 data/mock/")
    clean_mock_data()

    print("\n[2] 清理 content/{lang}/{terms_dir}/ Mock Markdown")
    clean_mock_markdown()

    print("\n[3] 清理 data/queue/ mock文件")
    clean_mock_queue()

    print("\n✓ Mock清理完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
