---
title: "هجين الوجه (Hugging Face)"
term_id: "hugging_face"
category: "basic_concepts"
subcategory: ""
tags: ["platform", "open-source", "community"]
difficulty: 2
weight: 1
slug: "hugging_face"
aliases:
  - /ar/terms/hugging_face/
date: "2026-07-18T16:01:18.601406Z"
lastmod: "2026-07-18T17:15:08.512624Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "منصة ومجتمع رائدان يوفران أدوات ونماذج ومجموعات بيانات مفتوحة المصدر لتطوير التعلم الآلي."
---

## Definition

هجين الوجه هي شركة ومنصة عبر الإنترنت بارزة أصبحت محورية في النظام البيئي للذكاء الاصطناعي مفتوح المصدر. فهي تقدم مستودعاً ضخماً للنماذج المدربة مسبقاً، ومجموعات البيانات، وتطبيقات العرض التوضيحي.

### Summary

منصة ومجتمع رائدان يوفران أدوات ونماذج ومجموعات بيانات مفتوحة المصدر لتطوير التعلم الآلي.

## Key Concepts

- مفتوح المصدر
- مركز النماذج
- مكتبة المحولات (Transformers)
- التعاون المجتمعي

## Use Cases

- الوصول إلى نماذج معالجة اللغة الطبيعية (NLP) المدربة مسبقاً لتصنيف النصوص
- مشاركة نماذج التعلم الآلي المخصصة مع المجتمع
- بناء تطبيقات عرض توضيحي باستخدام تكاملات غراديو (Gradio) أو ستريمليت (Streamlit)

## Code Example

```python
from transformers import pipeline

# Load a pre-trained sentiment analysis model from Hugging Face
classifier = pipeline('sentiment-analysis')
result = classifier('I love using Hugging Face!')
print(result)
```

## Related Terms

- [المحولات (Transformers)](/en/terms/المحولات-transformers/)
- [مستودع النماذج (Model Repository)](/en/terms/مستودع-النماذج-model-repository/)
- [الذكاء الاصطناعي مفتوح المصدر (Open Source AI)](/en/terms/الذكاء-الاصطناعي-مفتوح-المصدر-open-source-ai/)
- [مركز مجموعات البيانات (Dataset Hub)](/en/terms/مركز-مجموعات-البيانات-dataset-hub/)
