---
title: "مكتبة المحولات (Transformers)"
term_id: "transformers"
category: "training_techniques"
subcategory: ""
tags: ["library", "tools", "ecosystem"]
difficulty: 2
weight: 1
slug: "transformers"
date: "2026-07-18T15:31:48.544638Z"
lastmod: "2026-07-18T17:15:08.451585Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "في هذا السياق، تشير إلى مكتبة Hugging Face Transformers، وهي أداة مفتوحة المصدر شائعة للنماذج المتطورة في معالجة اللغات الطبيعية متعددة الوسائط."
---
## Definition

غالباً ما يشير مصطلح 'Transformers' إلى مكتبة بايثون واسعة الاستخدام التي تحافظ عليها شركة Hugging Face. توفر واجهات سهلة الاستخدام لتحميل وتدريب ونشر النماذج المدربة مسبقاً بناءً على

### Summary

في هذا السياق، تشير إلى مكتبة Hugging Face Transformers، وهي أداة مفتوحة المصدر شائعة للنماذج المتطورة في معالجة اللغات الطبيعية متعددة الوسائط.

## Key Concepts

- مركز Hugging Face
- واجهة برمجة التطبيقات للأنابيب (Pipeline API)
- بطاقات النماذج
- تكامل المؤقت (Tokenizer)

## Use Cases

- النمذجة السريعة لتطبيقات معالجة اللغات الطبيعية
- الوصول إلى النماذج المدربة مسبقاً من قبل المجتمع
- توحيد سير عمل نشر النماذج

## Code Example

```python
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
```

## Related Terms

- [hugging_face (شركة Hugging Face)](/en/terms/hugging_face-شركة-hugging-face/)
- [pipeline (الأنابيب/خط الأنابيب)](/en/terms/pipeline-الأنابيب-خط-الأنابيب/)
- [tokenizer (المؤقت/المقسم)](/en/terms/tokenizer-المؤقت-المقسم/)
- [pytorch (مكتبة PyTorch)](/en/terms/pytorch-مكتبة-pytorch/)
