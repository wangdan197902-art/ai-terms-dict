---
title: "التعلم ضمن السياق"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T15:22:59.170217Z"
lastmod: "2026-07-18T17:15:08.433035Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "تقنية يتعلم فيها النماذج أداء المهام من خلال مراقبة الأمثلة المقدمة في الأمر (Prompt)."
---
## Definition

يتيح التعلم ضمن السياق (ICL) لنماذج اللغات الكبيرة التكيف مع مهام جديدة دون تحديث أوزانها. من خلال توفير أزواج الإدخال والإخراج داخل سياق الأمر، يستنتج النموذج النمط ويؤدي المهمة المطلوبة.

### Summary

تقنية يتعلم فيها النماذج أداء المهام من خلال مراقبة الأمثلة المقدمة في الأمر (Prompt).

## Key Concepts

- التعلم بعدد قليل من الأمثلة
- صفر أمثلة (Zero-Shot)
- تصميم الأمر
- التكيف بدون أوزان

## Use Cases

- اختبار قدرات النموذج بسرعة على مجموعات بيانات جديدة
- تبديل المهام الديناميكي في الوكلاء المحادثين
- إنشاء النماذج الأولية لتطبيقات الذكاء الاصطناعي دون إعادة التدريب

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering (هندسة الأوامر)](/en/terms/prompt-engineering-هندسة-الأوامر/)
- [Few-Shot (عدد قليل من الأمثلة)](/en/terms/few-shot-عدد-قليل-من-الأمثلة/)
- [Zero-Shot (صفر أمثلة)](/en/terms/zero-shot-صفر-أمثلة/)
- [Meta-Learning (التعلم الفائق)](/en/terms/meta-learning-التعلم-الفائق/)
