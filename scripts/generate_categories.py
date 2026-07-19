#!/usr/bin/env python3
"""
P0a: 补全 20 个扩展语种的 categories 目录
为每个语种生成 _index.md + 5 个分类子目录（本地化分类名和描述）

使用方式: python3 scripts/generate_categories.py
"""

import os
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
CONTENT_DIR = PROJECT_ROOT / "content"

# 5 个分类的本地化翻译（title + description）
# 格式: {category_id: {lang: (title, description)}}
CATEGORY_TRANSLATIONS = {
    "basic_concepts": {
        "en": ("Basic Concepts", "Foundational AI concepts and terminology"),
        "es": ("Conceptos Básicos", "Conceptos fundamentales de IA y terminología"),
        "de": ("Grundkonzepte", "Grundlegende KI-Konzepte und Terminologie"),
        "ja": ("基本概念", "AIの基本的な概念と用語"),
        "fr": ("Concepts de Base", "Concepts fondamentaux de l'IA et terminologie"),
        "zh": ("基础概念", "AI基础概念与术语"),
        "pt": ("Conceitos Básicos", "Conceitos fundamentais de IA e terminologia"),
        "ru": ("Базовые концепции", "Основные концепции ИИ и терминология"),
        "ko": ("기본 개념", "AI 기본 개념과 용어"),
        "ar": ("المفاهيم الأساسية", "المفاهيم الأساسية للذكاء الاصطناعي والمصطلحات"),
        "it": ("Concetti di Base", "Concetti fondamentali dell'IA e terminologia"),
        "nl": ("Basisconcepten", "Fundamentele AI-concepten en terminologie"),
        "pl": ("Podstawowe Pojęcia", "Podstawowe pojęcia AI i terminologia"),
        "tr": ("Temel Kavramlar", "Temel yapay zeka kavramları ve terminoloji"),
        "vi": ("Khái niệm Cơ bản", "Các khái niệm cơ bản về AI và thuật ngữ"),
        "th": ("แนวคิดพื้นฐาน", "แนวคิดพื้นฐานของ AI และคำศัพท์"),
        "id": ("Konsep Dasar", "Konsep dasar AI dan terminologi"),
        "sv": ("Grundläggande Koncept", "Grundläggande AI-koncept och terminologi"),
        "cs": ("Základní Koncepty", "Základní koncepty umělé inteligence a terminologie"),
        "da": ("Grundlæggende Koncepter", "Grundlæggende AI-koncepter og terminologi"),
        "fi": ("Peruskäsitteet", "Tekoälyn peruskäsitteet ja terminologia"),
        "no": ("Grunnleggende Konsepter", "Grunnleggende AI-konsepter og terminologi"),
        "he": ("מושגי יסוד", "מושגי יסוד של בינה מלאכותית וטרמינולוגיה"),
        "ro": ("Concepte de Bază", "Concepte fundamentale ale IA și terminologie"),
        "hu": ("Alapfogalmak", "AI alapfogalmak és terminológia"),
        "el": ("Βασικές Έννοιες", "Βασικές έννοιες της ΤΝ και ορολογία"),
    },
    "application_paradigms": {
        "en": ("Application Paradigms", "How AI is applied in practice"),
        "es": ("Paradigmas de Aplicación", "Cómo se aplica la IA en la práctica"),
        "de": ("Anwendungsparadigmen", "Wie KI in der Praxis angewendet wird"),
        "ja": ("応用パラダイム", "AIが実践でどのように応用されるか"),
        "fr": ("Paradigmes d'Application", "Comment l'IA est appliquée en pratique"),
        "zh": ("应用范式", "AI在实际中的应用方式"),
        "pt": ("Paradigmas de Aplicação", "Como a IA é aplicada na prática"),
        "ru": ("Парадигмы применения", "Как ИИ применяется на практике"),
        "ko": ("응용 패러다임", "AI가 실무에서 어떻게 적용되는지"),
        "ar": ("نماذج التطبيق", "كيف يُطبق الذكاء الاصطناعي عملياً"),
        "it": ("Paradigmi di Applicazione", "Come l'IA viene applicata in pratica"),
        "nl": ("Toepassingsparadigma's", "Hoe AI in de praktijk wordt toegepast"),
        "pl": ("Paradygmaty Zastosowań", "Jak AI jest stosowane w praktyce"),
        "tr": ("Uygulama Paradigmaları", "Yapay zekanın pratikte nasıl uygulandığı"),
        "vi": ("Mô hình Ứng dụng", "Cách AI được áp dụng trong thực tế"),
        "th": ("กระบวนทัศน์การประยุกต์", "วิธีที่ AI ถูกประยุกต์ใช้ในทางปฏิบัติ"),
        "id": ("Paradigma Aplikasi", "Bagaimana AI diterapkan dalam praktik"),
        "sv": ("Tillämpningsparadigmer", "Hur AI tillämpas i praktiken"),
        "cs": ("Aplikační Paradigmata", "Jak je AI aplikována v praxi"),
        "da": ("Anvendelsesparadigmer", "Hvordan AI anvendes i praksis"),
        "fi": ("Sovellusparadigmat", "Miten tekoälyä sovelletaan käytännössä"),
        "no": ("Anvendelsesparadigmer", "Hvordan AI anvendes i praksis"),
        "he": ("פרדיגמות יישום", "כיצד מוחל בינה מלאכותית בפועל"),
        "ro": ("Paradigme de Aplicare", "Cum este aplicată IA în practică"),
        "hu": ("Alkalmazási Paradigmák", "Hogyan alkalmazzák az AI-t a gyakorlatban"),
        "el": ("Παραδείγματα Εφαρμογής", "Πώς εφαρμόζεται η ΤΝ στην πράξη"),
    },
    "engineering_practice": {
        "en": ("Engineering Practice", "Engineering practices for AI systems"),
        "es": ("Práctica de Ingeniería", "Prácticas de ingeniería para sistemas de IA"),
        "de": ("Ingenieurspraxis", "Ingenieurspraxis für KI-Systeme"),
        "ja": ("エンジニアリング実践", "AIシステムのエンジニアリング実践"),
        "fr": ("Pratique d'Ingénierie", "Pratiques d'ingénierie pour les systèmes d'IA"),
        "zh": ("工程实践", "AI系统的工程实践"),
        "pt": ("Prática de Engenharia", "Práticas de engenharia para sistemas de IA"),
        "ru": ("Инженерная практика", "Инженерная практика для систем ИИ"),
        "ko": ("엔지니어링 실무", "AI 시스템의 엔지니어링 실무"),
        "ar": ("الممارسة الهندسية", "الممارسات الهندسية لأنظمة الذكاء الاصطناعي"),
        "it": ("Pratica di Ingegneria", "Pratiche di ingegneria per sistemi IA"),
        "nl": ("Engineeringpraktijk", "Engineeringpraktijk voor AI-systemen"),
        "pl": ("Praktyka Inżynieryjna", "Praktyki inżynieryjne dla systemów AI"),
        "tr": ("Mühendislik Uygulamaları", "Yapay zeka sistemleri için mühendislik uygulamaları"),
        "vi": ("Thực hành Kỹ thuật", "Thực hành kỹ thuật cho hệ thống AI"),
        "th": ("การปฏิบัติทางวิศวกรรม", "แนวปฏิบัติทางวิศวกรรมสำหรับระบบ AI"),
        "id": ("Praktik Rekayasa", "Praktik rekayasa untuk sistem AI"),
        "sv": ("Ingenjörspraxis", "Ingenjörspraxis för AI-system"),
        "cs": ("Inženýrská Praxe", "Inženýrská praxe pro systémy umělé inteligence"),
        "da": ("Ingeniørpraksis", "Ingeniørpraksis for AI-systemer"),
        "fi": ("Insinöörikäytännöt", "Insinöörikäytännöt tekoälyjärjestelmille"),
        "no": ("Ingeniørpraksis", "Ingeniørpraksis for AI-systemer"),
        "he": ("פרקטיקה הנדסית", "פרקטיקות הנדסיות למערכות בינה מלאכותית"),
        "ro": ("Practică de Inginerie", "Practici de inginerie pentru sisteme IA"),
        "hu": ("Mérnöki Gyakorlat", "Mérnöki gyakorlatok AI rendszerekhez"),
        "el": ("Μηχανική Πρακτική", "Μηχανικές πρακτικές για συστήματα ΤΝ"),
    },
    "ethics_safety": {
        "en": ("Ethics & Safety", "Responsible AI development"),
        "es": ("Ética y Seguridad", "Desarrollo responsable de IA"),
        "de": ("Ethik & Sicherheit", "Verantwortungsvolle KI-Entwicklung"),
        "ja": ("倫理と安全性", "責任あるAI開発"),
        "fr": ("Éthique et Sécurité", "Développement responsable de l'IA"),
        "zh": ("伦理与安全", "负责任的AI开发"),
        "pt": ("Ética e Segurança", "Desenvolvimento responsável de IA"),
        "ru": ("Этика и безопасность", "Ответственная разработка ИИ"),
        "ko": ("윤리와 안전", "책임감 있는 AI 개발"),
        "ar": ("الأخلاق والسلامة", "تطوير مسؤول للذكاء الاصطناعي"),
        "it": ("Etica e Sicurezza", "Sviluppo responsabile dell'IA"),
        "nl": ("Ethiek en Veiligheid", "Verantwoorde AI-ontwikkeling"),
        "pl": ("Etyka i Bezpieczeństwo", "Odpowiedzialny rozwój AI"),
        "tr": ("Etik ve Güvenlik", "Sorumlu yapay zeka geliştirme"),
        "vi": ("Đạo đức và An toàn", "Phát triển AI có trách nhiệm"),
        "th": ("จริยธรรมและความปลอดภัย", "การพัฒนา AI อย่างรับผิดชอบ"),
        "id": ("Etika dan Keamanan", "Pengembangan AI yang bertanggung jawab"),
        "sv": ("Etik och Säkerhet", "Ansvarsfull AI-utveckling"),
        "cs": ("Etika a Bezpečnost", "Odpovědný vývoj umělé inteligence"),
        "da": ("Etik og Sikkerhed", "Ansvarlig AI-udvikling"),
        "fi": ("Etiikka ja Turvallisuus", "Vastuullinen tekoälyn kehitys"),
        "no": ("Etikk og Sikkerhet", "Ansvarlig AI-utvikling"),
        "he": ("אתיקה ובטיחות", "פיתוח אחראי של בינה מלאכותית"),
        "ro": ("Etică și Siguranță", "Dezvoltare responsabilă a IA"),
        "hu": ("Etika és Biztonság", "Felelős AI-fejlesztés"),
        "el": ("Ηθική και Ασφάλεια", "Υπεύθυνη ανάπτυξη ΤΝ"),
    },
    "training_techniques": {
        "en": ("Training Techniques", "Methods for training ML models"),
        "es": ("Técnicas de Entrenamiento", "Métodos para entrenar modelos de ML"),
        "de": ("Trainingstechniken", "Methoden zum Training von ML-Modellen"),
        "ja": ("訓練手法", "MLモデルの訓練手法"),
        "fr": ("Techniques d'Entraînement", "Méthodes d'entraînement des modèles ML"),
        "zh": ("训练技术", "ML模型的训练方法"),
        "pt": ("Técnicas de Treinamento", "Métodos para treinar modelos de ML"),
        "ru": ("Методы обучения", "Методы обучения моделей ML"),
        "ko": ("훈련 기법", "ML 모델 훈련 방법"),
        "ar": ("تقنيات التدريب", "أساليب تدريب نماذج التعلم الآلي"),
        "it": ("Tecniche di Addestramento", "Metodi per addestrare modelli ML"),
        "nl": ("Trainingstechnieken", "Methoden voor het trainen van ML-modellen"),
        "pl": ("Techniki Treningu", "Metody trenowania modeli ML"),
        "tr": ("Eğitim Teknikleri", "ML modellerini eğitme yöntemleri"),
        "vi": ("Kỹ thuật Huấn luyện", "Phương pháp huấn luyện mô hình ML"),
        "th": ("เทคนิคการฝึกอบรม", "วิธีการฝึกอบรมโมเดล ML"),
        "id": ("Teknik Pelatihan", "Metode untuk melatih model ML"),
        "sv": ("Träningstekniker", "Metoder för att träna ML-modeller"),
        "cs": ("Tréninkové Techniky", "Metody trénování ML modelů"),
        "da": ("Træningsteknikker", "Metoder til træning af ML-modeller"),
        "fi": ("Koulutustekniikat", "Menetelmät ML-mallien kouluttamiseen"),
        "no": ("Treningsteknikker", "Metoder for trening av ML-modeller"),
        "he": ("טכניקות אימון", "שיטות לאימון מודלים של למידת מכונה"),
        "ro": ("Tehnici de Antrenare", "Metode de antrenare a modelelor ML"),
        "hu": ("Képzési Technikák", "Módszerek ML modellek képzéséhez"),
        "el": ("Τεχνικές Εκπαίδευσης", "Μέθοδοι εκπαίδευσης μοντέλων ML"),
    },
}

# 分类权重（控制显示顺序）
CATEGORY_WEIGHT = {
    "basic_concepts": 10,
    "training_techniques": 20,
    "application_paradigms": 30,
    "engineering_practice": 40,
    "ethics_safety": 50,
}

# Categories 索引页的本地化（title + description + body）
CATEGORIES_INDEX_TRANSLATIONS = {
    "en": ("Categories", "Browse AI terms by category", "Browse AI terms by category:"),
    "es": ("Categorías", "Explorar términos de IA por categoría", "Explorar términos de IA por categoría:"),
    "de": ("Kategorien", "KI-Begriffe nach Kategorie durchsuchen", "KI-Begriffe nach Kategorie durchsuchen:"),
    "ja": ("カテゴリ", "カテゴリ別にAI用語を閲覧", "カテゴリ別にAI用語を閲覧:"),
    "fr": ("Catégories", "Parcourir les termes d'IA par catégorie", "Parcourir les termes d'IA par catégorie:"),
    "zh": ("分类", "按分类浏览AI术语", "按分类浏览AI术语:"),
    "pt": ("Categorias", "Navegar termos de IA por categoria", "Navegar termos de IA por categoria:"),
    "ru": ("Категории", "Просмотр терминов ИИ по категориям", "Просмотр терминов ИИ по категориям:"),
    "ko": ("카테고리", "카테고리별 AI 용어 탐색", "카테고리별 AI 용어 탐색:"),
    "ar": ("الفئات", "تصفح مصطلحات الذكاء الاصطناعي حسب الفئة", "تصفح مصطلحات الذكاء الاصطناعي حسب الفئة:"),
    "it": ("Categorie", "Sfoglia i termini IA per categoria", "Sfoglia i termini IA per categoria:"),
    "nl": ("Categorieën", "Blader door AI-termen op categorie", "Blader door AI-termen op categorie:"),
    "pl": ("Kategorie", "Przeglądaj terminy AI według kategorii", "Przeglądaj terminy AI według kategorii:"),
    "tr": ("Kategoriler", "Yapay zeka terimlerini kategoriye göre tara", "Yapay zeka terimlerini kategoriye göre tara:"),
    "vi": ("Danh mục", "Duyệt thuật ngữ AI theo danh mục", "Duyệt thuật ngữ AI theo danh mục:"),
    "th": ("หมวดหมู่", "เรียกดูคำศัพท์ AI ตามหมวดหมู่", "เรียกดูคำศัพท์ AI ตามหมวดหมู่:"),
    "id": ("Kategori", "Jelajahi istilah AI berdasarkan kategori", "Jelajahi istilah AI berdasarkan kategori:"),
    "sv": ("Kategorier", "Bläddra AI-termer efter kategori", "Bläddra AI-termer efter kategori:"),
    "cs": ("Kategorie", "Procházet termíny AI podle kategorie", "Procházet termíny AI podle kategorie:"),
    "da": ("Kategorier", "Gennemse AI-termer efter kategori", "Gennemse AI-termer efter kategori:"),
    "fi": ("Kategoriat", "Selaa AI-termejä luokan mukaan", "Selaa AI-termejä luokan mukaan:"),
    "no": ("Kategorier", "Bla gjennom AI-termer etter kategori", "Bla gjennom AI-termer etter kategori:"),
    "he": ("קטגוריות", "עיין במונחי AI לפי קטגוריה", "עיין במונחי AI לפי קטגוריה:"),
    "ro": ("Categorii", "Răsfoiește termenii IA pe categorii", "Răsfoiește termenii IA pe categorii:"),
    "hu": ("Kategóriák", "AI kifejezések böngészése kategória szerint", "AI kifejezések böngészése kategória szerint:"),
    "el": ("Κατηγορίες", "Περιηγηθείτε στους όρους ΤΝ ανά κατηγορία", "Περιηγηθείτε στους όρους ΤΝ ανά κατηγορία:"),
}


def generate_category_index(lang: str) -> str:
    """生成 categories/_index.md 内容"""
    title, desc, body = CATEGORIES_INDEX_TRANSLATIONS[lang]
    return f"""+++
title = "{title}"
description = "{desc}"
weight = 90
layout = "categories-list"
+++

# {title}

{body}

{{{{< categories-list >}}}}
"""


def generate_category_subindex(lang: str, category_id: str) -> str:
    """生成 categories/{category_id}/_index.md 内容"""
    title, desc = CATEGORY_TRANSLATIONS[category_id][lang]
    weight = CATEGORY_WEIGHT[category_id]
    return f"""+++
title = "{title}"
description = "{desc}"
category = "{category_id}"
layout = "category-list"
weight = {weight}
+++
"""


def main():
    # 20 个需要补全 categories 的语种
    target_langs = [
        "pt", "ru", "ko", "ar", "it", "nl", "pl", "tr", "vi", "th",
        "id", "sv", "cs", "da", "fi", "no", "he", "ro", "hu", "el"
    ]

    # 5 个分类
    categories = [
        "basic_concepts", "training_techniques", "application_paradigms",
        "engineering_practice", "ethics_safety"
    ]

    created_count = 0
    skipped_count = 0

    for lang in target_langs:
        lang_content_dir = CONTENT_DIR / lang
        if not lang_content_dir.exists():
            print(f"⚠ 跳过 {lang}: content/{lang} 目录不存在")
            skipped_count += 1
            continue

        # 创建 categories 目录
        categories_dir = lang_content_dir / "categories"
        categories_dir.mkdir(exist_ok=True)

        # 生成 _index.md
        index_file = categories_dir / "_index.md"
        if index_file.exists():
            print(f"  {lang}: _index.md 已存在，跳过")
        else:
            index_file.write_text(generate_category_index(lang), encoding="utf-8")
            created_count += 1
            print(f"  {lang}: 创建 categories/_index.md")

        # 生成 5 个分类子目录
        for category_id in categories:
            category_dir = categories_dir / category_id
            category_dir.mkdir(exist_ok=True)
            cat_file = category_dir / "_index.md"
            if cat_file.exists():
                print(f"  {lang}: categories/{category_id}/_index.md 已存在，跳过")
            else:
                cat_file.write_text(generate_category_subindex(lang, category_id), encoding="utf-8")
                created_count += 1
                print(f"  {lang}: 创建 categories/{category_id}/_index.md")

    print(f"\n✅ 完成！")
    print(f"  创建文件数: {created_count}")
    print(f"  跳过语种数: {skipped_count}")
    print(f"  预期创建: 20 语种 × (1 + 5) = 120 个文件")


if __name__ == "__main__":
    main()
