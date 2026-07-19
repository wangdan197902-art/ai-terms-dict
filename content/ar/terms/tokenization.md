---
title: "تجزئة الرموز (Tokenization)"
term_id: "tokenization"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "preprocessing"]
difficulty: 3
weight: 1
slug: "tokenization"
date: "2026-07-18T15:31:35.360988Z"
lastmod: "2026-07-18T17:15:08.450917Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "تجزئة الرموز هي عملية تقسيم النص الخام إلى وحدات أصغر تسمى الرموز، والتي يمكن معالجتها بواسطة خوارزميات التعلم الآلي."
---
## Definition

تُعد تجزئة الرموز خطوة حاسمة في المعالجة المسبقة لمعالجة اللغات الطبيعية (NLP)، حيث تحول النص غير المهيكلة إلى بيانات مهيكلة مناسبة لإدخالها في النموذج. تتضمن هذه العملية تفكيك الجمل والفقرات إلى مكوناتها الأساسية من الرموز.

### Summary

تجزئة الرموز هي عملية تقسيم النص الخام إلى وحدات أصغر تسمى الرموز، والتي يمكن معالجتها بواسطة خوارزميات التعلم الآلي.

## Key Concepts

- تقسيم النص
- المعالجة المسبقة
- WordPiece (نمط تجزئة)
- ترميز زوج البايت (BPE)

## Use Cases

- إعداد مجموعات البيانات لتدريب نموذج BERT
- تنسيق المدخلات لنماذج GPT
- تنظيف البيانات لتحليل المشاعر

## Code Example

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('Hello world!')
```

## Related Terms

- [Tokenizer (جهاز التجزئة)](/en/terms/tokenizer-جهاز-التجزئة/)
- [Vocabulary (المفردات)](/en/terms/vocabulary-المفردات/)
- [Embedding (التضمين)](/en/terms/embedding-التضمين/)
- [Preprocessing (المعالجة المسبقة)](/en/terms/preprocessing-المعالجة-المسبقة/)
