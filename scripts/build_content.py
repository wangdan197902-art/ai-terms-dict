#!/usr/bin/env python3
"""将JSON术语数据转为Hugo Markdown文件。

输出位置：content/{lang}/terms/{slug}.md
- 英文：content/en/terms/prompt-engineering.md
- 西班牙语：content/es/terminos/prompt-engineering.md
- 德语：content/de/begriffe/prompt-engineering.md
- 日语：content/ja/用語/prompt-engineering.md
- 法语：content/fr/termes/prompt-engineering.md
- 中文：content/zh/术语/prompt-engineering.md

注意：所有语种都使用 term_id (如prompt-engineering) 作为slug，避免CJK编码问题。
"""
import sys
import json
import re
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config


# 语种到内容目录的映射
LANG_TO_CONTENT_DIR = {
    "en": "terms",
    "es": "terminos",
    "de": "begriffe",
    "ja": "用語",
    "fr": "termes",
    "zh": "术语",
}


def slugify(text: str) -> str:
    """将文本转为URL安全的slug。"""
    # 对于term_id，已经是slug格式
    text = text.lower().strip()
    text = re.sub(r'[^\w\-]', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def build_front_matter(term: dict, lang: str) -> str:
    """构建Hugo Front Matter。"""
    # 使用term_id作为slug（统一所有语种）
    slug = term.get("term_id", slugify(term.get("term_name", "unknown")))

    # 将key_concepts转为YAML列表
    key_concepts = term.get("key_concepts", [])
    use_cases = term.get("use_cases", [])
    related_terms = term.get("related_terms", [])
    tags = term.get("tags", [])

    # 代码示例处理
    code_example = term.get("code_example")
    code_block = ""
    if code_example:
        # 检测语言
        lang_label = "python"
        if "import " in code_example or "def " in code_example:
            lang_label = "python"
        elif "const " in code_example or "function " in code_example:
            lang_label = "javascript"
        code_block = f"\n## Code Example\n\n```{lang_label}\n{code_example}\n```\n"

    # Key concepts
    key_concepts_md = "\n".join(f"- {c}" for c in key_concepts) if key_concepts else "- (none)"

    # Use cases
    use_cases_md = "\n".join(f"- {u}" for u in use_cases) if use_cases else "- (none)"

    # Related terms
    related_md = "\n".join(f"- [{r}](/en/terms/{slugify(r)}/)" for r in related_terms) if related_terms else "- (none)"

    # 构建完整的Markdown内容
    title = term.get("term_name", term.get("english", "Unknown"))
    definition_short = term.get("definition_short", "")
    definition_long = term.get("definition_long", "")
    category = term.get("category", "")
    difficulty = term.get("difficulty", 3)
    status = term.get("status", "published")
    source = term.get("source", "agnes_llm")

    # 生成Markdown内容
    content = f"""---
title: "{title}"
term_id: "{term.get('term_id', '')}"
category: "{category}"
subcategory: "{term.get('subcategory', '')}"
tags: {json.dumps(tags, ensure_ascii=False) if tags else '[]'}
difficulty: {difficulty}
weight: 1
slug: "{slug}"
aliases:
  - /{lang}/terms/{slug}/
date: "{term.get('generated_at', datetime.utcnow().isoformat() + 'Z')}"
lastmod: "{datetime.utcnow().isoformat() + 'Z'}"
draft: false
source: "{source}"
status: "{status}"
language: "{lang}"
description: "{definition_short.replace('"', '\\"')[:200]}"
---

## Definition

{definition_long}

### Summary

{definition_short}

## Key Concepts

{key_concepts_md}

## Use Cases

{use_cases_md}
{code_block}
## Related Terms

{related_md}
"""

    return content


def write_markdown(term: dict, lang: str) -> Path:
    """将单个术语写入Markdown文件。"""
    content_dir_name = LANG_TO_CONTENT_DIR.get(lang, "terms")
    content_dir = config.hugo.content_dir / lang / content_dir_name

    # 确保目录存在
    content_dir.mkdir(parents=True, exist_ok=True)

    # 文件名使用 term_id（确保唯一性和URL安全）
    slug = term.get("term_id", slugify(term.get("term_name", "unknown")))
    filename = f"{slug}.md"
    filepath = content_dir / filename

    # 生成内容
    content = build_front_matter(term, lang)

    # 写入文件
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main():
    print("=" * 60)
    print("Step 01-03: 内容Markdown生成")
    print("=" * 60)

    # 加载翻译数据
    with open(config.paths.translated_terms_file, "r", encoding="utf-8") as f:
        translations = json.load(f)

    print(f"加载翻译: {len(translations)} 条")
    print(f"语种: {[t['language'] for t in translations]}")

    # 为每个翻译生成Markdown
    written_files = []
    for term in translations:
        lang = term["language"]
        filepath = write_markdown(term, lang)
        written_files.append(filepath)
        print(f"  ✓ {lang}: {filepath}")

    print(f"\n✓ 已生成 {len(written_files)} 个Markdown文件")

    # 验证文件
    print("\n文件验证:")
    for f in written_files:
        size = f.stat().st_size
        print(f"  {f.name} ({size} bytes)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
