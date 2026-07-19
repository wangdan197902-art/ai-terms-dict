#!/usr/bin/env python3
"""
P2a: 为 26 个语种创建 tags/_index.md
- 自定义标签索引页的标题和描述（本地化）
- URL: /{lang}/tags/

使用方式: python3 scripts/generate_tags_index.py
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CONTENT_DIR = PROJECT_ROOT / "content"

# 26 个语种的标签索引页本地化
TAGS_INDEX_TRANSLATIONS = {
    "en": ("Tags", "Browse all AI/ML tags"),
    "es": ("Etiquetas", "Explorar todas las etiquetas de IA/ML"),
    "de": ("Tags", "Alle KI/ML-Tags durchsuchen"),
    "ja": ("タグ", "すべてのAI/MLタグを閲覧"),
    "fr": ("Étiquettes", "Parcourir toutes les étiquettes IA/ML"),
    "zh": ("标签", "浏览所有 AI/ML 标签"),
    "pt": ("Tags", "Navegar todas as tags de IA/ML"),
    "ru": ("Теги", "Просмотр всех тегов ИИ/ML"),
    "ko": ("태그", "모든 AI/ML 태그 탐색"),
    "ar": ("الوسوم", "تصفح جميع وسوم الذكاء الاصطناعي/تعلم الآلة"),
    "it": ("Tag", "Sfoglia tutti i tag IA/ML"),
    "nl": ("Tags", "Blader door alle AI/ML-tags"),
    "pl": ("Tagi", "Przeglądaj wszystkie tagi AI/ML"),
    "tr": ("Etiketler", "Tüm yapay zeka/ML etiketlerini tara"),
    "vi": ("Thẻ", "Duyệt tất cả thẻ AI/ML"),
    "th": ("แท็ก", "เรียกดูแท็ก AI/ML ทั้งหมด"),
    "id": ("Tag", "Jelajahi semua tag AI/ML"),
    "sv": ("Taggar", "Bläddra alla AI/ML-taggar"),
    "cs": ("Štítky", "Procházet všechny štítky AI/ML"),
    "da": ("Tags", "Gennemse alle AI/ML-tags"),
    "fi": ("Tunnisteet", "Selaa kaikkia tekoäly/ML-tunnisteita"),
    "no": ("Tags", "Bla gjennom alle AI/ML-tagger"),
    "he": ("תגים", "עיין בכל תגי הבינה המלאכותית/למידת מכונה"),
    "ro": ("Etichete", "Răsfoiește toate etichetele IA/ML"),
    "hu": ("Címkék", "Minden AI/ML címke böngészése"),
    "el": ("Ετικέτες", "Περιηγηθείτε σε όλες τις ετικέτες ΤΝ/ML"),
}


def main():
    created_count = 0

    for lang, (title, desc) in TAGS_INDEX_TRANSLATIONS.items():
        lang_tags_dir = CONTENT_DIR / lang / "tags"
        lang_tags_dir.mkdir(parents=True, exist_ok=True)

        index_file = lang_tags_dir / "_index.md"
        if index_file.exists():
            print(f"  {lang}: tags/_index.md 已存在，跳过")
            continue

        content = f"""+++
title = "{title}"
description = "{desc}"
layout = "tags"
weight = 80
+++
"""
        index_file.write_text(content, encoding="utf-8")
        created_count += 1
        print(f"  {lang}: 创建 tags/_index.md")

    print(f"\n✅ 完成！创建 {created_count} 个 tags/_index.md 文件")


if __name__ == "__main__":
    main()
