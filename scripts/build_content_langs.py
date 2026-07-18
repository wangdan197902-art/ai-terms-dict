#!/usr/bin/env python3
"""批量为多个语种生成Hugo Markdown内容。

从 data/queue/translated_terms_{lang}.json 读取翻译，
生成 content/{lang}/terms/*.md 文件。

支持断点续传：已存在的markdown文件跳过（除非--force）。
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.config import config
from scripts.build_content import write_markdown, slugify


# 语种到搜索页目录名的映射（部分语种有本地化的搜索页目录名）
SEARCH_DIR = {
    "en": "search", "es": "buscar", "de": "suche", "ja": "検索",
    "fr": "recherche", "zh": "搜索", "pt": "busca",
    # 扩展语种默认用 "search"
}

# 语种到首页标题和描述的映射
LANG_META = {
    "pt": ("Dicionário de Termos de IA", "Dicionário abrangente multilíngue de termos de Inteligência Artificial"),
    "ru": ("Словарь ИИ терминов", "Комплексный многоязычный словарь терминов ИИ"),
    "ko": ("AI 용어 사전", "포괄적인 다국어 AI 용어 사전"),
    "ar": ("قاموس مصطلحات الذكاء الاصطناعي", "قاموس شامل متعدد اللغات لمصطلحات الذكاء الاصطناعي"),
    "it": ("Dizionario dei Termini AI", "Dizionario multilingue completo dei termini AI"),
    "nl": ("AI-termen Woordenboek", "Uitgebreid meertalig woordenboek van AI-termen"),
    "pl": ("Słownik terminów AI", "Kompleksowy wielojęzyczny słownik terminów AI"),
    "tr": ("AI Terimleri Sözlüğü", "Kapsamlı çok dilli AI terimleri sözlüğü"),
    "vi": ("Từ điển Thuật ngữ AI", "Từ điển đa ngôn ngữ toàn diện về thuật ngữ AI"),
    "th": ("พจนานุกรมคำศัพท์ AI", "พจนานุกรมหลายภาษาที่ครอบคลุมคำศัพท์ AI"),
    "id": ("Kamus Istilah AI", "Kamus multibahasa yang komprehensif untuk istilah AI"),
    "sv": ("AI-termer Ordbok", "Omfattande flerspråkig ordbok över AI-termer"),
    "cs": ("Slovník AI termínů", "Komplexní vícejazyčný slovník AI termínů"),
    "da": ("AI-ordbog", "Omfattende flersproget ordbog over AI-termer"),
    "fi": ("AI-termien Sanakirja", "Kattava monikielinen sanakirja AI-termeistä"),
    "no": ("AI-ordbok", "Omfattende flerspråkig ordbok over AI-termer"),
    "he": ("מילון מונחי בינה מלאכותית", "מילון רב-לשוני מקיף למונחי בינה מלאכותית"),
    "ro": ("Dicționar de Termeni AI", "Dicționar multilingv cuprinzător de termeni AI"),
    "hu": ("AI Kifejezések Szótára", "Átfogó többnyelvű AI kifejezések szótára"),
    "el": ("Λεξικό Όρων ΤΝ", "Πλήρες πολύγλωσσο λεξικό όρων Τεχνητής Νοημοσύνης"),
}


def create_index_page(lang: str):
    """创建语种首页 content/{lang}/_index.md"""
    title, desc = LANG_META.get(lang, (f"AI Terms Dictionary ({lang})", "Multilingual AI terminology dictionary"))
    content_dir = config.hugo.content_dir / lang
    content_dir.mkdir(parents=True, exist_ok=True)

    index_file = content_dir / "_index.md"
    if index_file.exists():
        return False  # 已存在，跳过

    content = f"""+++
title = "{title}"
description = "{desc}"
weight = 1
+++

# {title}

{desc}

## Categories

- Fundamental Concepts
- Learning Methods
- Application Paradigms
- Engineering Practices
- Ethics and Safety

## Recent Terms

{{{{< latest-terms count="10" >}}}}
"""
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def create_search_page(lang: str):
    """创建搜索页 content/{lang}/{search_dir}/_index.md"""
    search_dir_name = SEARCH_DIR.get(lang, "search")
    title, desc = LANG_META.get(lang, (f"AI Terms ({lang})", "Search AI terms"))
    search_dir = config.hugo.content_dir / lang / search_dir_name
    search_dir.mkdir(parents=True, exist_ok=True)

    search_file = search_dir / "_index.md"
    if search_file.exists():
        return False

    content = f"""+++
title = "Search"
description = "Search AI terms"
layout = "search"
slug = "{search_dir_name}"
weight = 100
+++

# Search AI Terms

Use the search box below to find any AI term in all supported languages.
"""
    with open(search_file, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def build_lang_content(lang: str, force: bool = False) -> dict:
    """为单个语种生成所有Hugo内容。"""
    stats = {"lang": lang, "total": 0, "generated": 0, "skipped": 0, "failed": 0, "errors": []}

    # 读取翻译文件
    trans_file = config.paths.queue_dir / f"translated_terms_{lang}.json"
    if not trans_file.exists():
        stats["errors"].append(f"翻译文件不存在: {trans_file}")
        return stats

    with open(trans_file, "r", encoding="utf-8") as f:
        translations = json.load(f)

    stats["total"] = len(translations)
    print(f"\n[{lang}] 加载翻译: {len(translations)} 条")

    # 创建首页和搜索页
    if create_index_page(lang):
        print(f"  ✓ 创建首页 content/{lang}/_index.md")
    if create_search_page(lang):
        print(f"  ✓ 创建搜索页 content/{lang}/{SEARCH_DIR.get(lang, 'search')}/_index.md")

    # 生成术语页
    terms_dir = config.hugo.content_dir / lang / "terms"
    terms_dir.mkdir(parents=True, exist_ok=True)

    for term in translations:
        try:
            slug = term.get("term_id", slugify(term.get("term_name", "unknown")))
            filepath = terms_dir / f"{slug}.md"

            if filepath.exists() and not force:
                stats["skipped"] += 1
                continue

            write_markdown(term, lang)
            stats["generated"] += 1
        except Exception as e:
            stats["failed"] += 1
            if len(stats["errors"]) < 3:
                stats["errors"].append(f"{term.get('term_id', 'unknown')}: {e}")

    print(f"  ✓ 生成: {stats['generated']} | 跳过: {stats['skipped']} | 失败: {stats['failed']}")
    return stats


def main():
    parser = argparse.ArgumentParser(description="批量为多个语种生成Hugo内容")
    parser.add_argument(
        "--langs",
        type=str,
        default="",
        help="目标语种，逗号分隔（如 pt,it,nl）。默认所有扩展语种。",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新生成已存在的markdown文件",
    )
    args = parser.parse_args()

    if args.langs:
        langs = [l.strip() for l in args.langs.split(",") if l.strip()]
    else:
        # 默认20个扩展语种
        langs = ["pt", "it", "nl", "ko", "sv", "he", "da", "no", "fi",
                 "ru", "pl", "tr", "cs", "el", "ar", "id", "th", "vi", "ro", "hu"]

    print("=" * 60)
    print(f"批量生成Hugo内容")
    print(f"  语种: {langs}")
    print(f"  强制重新生成: {args.force}")
    print("=" * 60)

    all_stats = []
    for lang in langs:
        stats = build_lang_content(lang, force=args.force)
        all_stats.append(stats)

    # 汇总
    print("\n" + "=" * 60)
    print("汇总")
    print("=" * 60)
    total_generated = sum(s["generated"] for s in all_stats)
    total_skipped = sum(s["skipped"] for s in all_stats)
    total_failed = sum(s["failed"] for s in all_stats)
    print(f"  总生成: {total_generated}")
    print(f"  总跳过: {total_skipped}")
    print(f"  总失败: {total_failed}")

    print("\n各语种详情:")
    for s in all_stats:
        status = "✓" if s["failed"] == 0 else "⚠"
        print(f"  {status} {s['lang']}: {s['generated']}/{s['total']} 生成, {s['skipped']} 跳过, {s['failed']} 失败")
        for err in s["errors"]:
            print(f"      - {err}")

    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
