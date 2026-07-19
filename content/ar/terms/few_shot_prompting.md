---
title: الإرشاد بأمثلة قليلة
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T15:37:00.219981Z'
lastmod: '2026-07-18T17:15:08.461410Z'
draft: false
source: agnes_llm
status: published
language: ar
description: الإرشاد بأمثلة قليلة هو تقنية تُقدم فيها نماذج اللغة الكبيرة عدداً صغيراً
  من أمثلة المدخلات والمخرجات ضمن الإرشاد لتوجيه سلوكها.
---
## Definition

تعتمد هذه الطريقة على قدرات التعلم السياقي للنماذج اللغوية الكبيرة من خلال تقديم عدد قليل من الأمثلة التوضيحية مباشرة داخل الإرشاد. وعلى عكس ضبط النموذج الدقيق الذي يتطلب تحديث أوزان النموذج، فإن هذا النهج يعتمد على السياق الحالي.

### Summary

الإرشاد بأمثلة قليلة هو تقنية تُقدم فيها نماذج اللغة الكبيرة عدداً صغيراً من أمثلة المدخلات والمخرجات ضمن الإرشاد لتوجيه سلوكها.

## Key Concepts

- التعلم السياقي
- هندسة الإرشاد
- التوجيه القائم على الأمثلة
- مقارنة الصفرية

## Use Cases

- تنسيق تحليل المشاعر
- تكييف أسلوب البرمجة
- استخراج البيانات المهيكلة

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (الصفرية)](/en/terms/zero_shot-الصفرية/)
- [prompt_engineering (هندسة الإرشاد)](/en/terms/prompt_engineering-هندسة-الإرشاد/)
- [in_context_learning (التعلم السياقي)](/en/terms/in_context_learning-التعلم-السياقي/)
- [llm (نموذج لغوي كبير)](/en/terms/llm-نموذج-لغوي-كبير/)
