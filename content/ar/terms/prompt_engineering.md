---
title: "هندسة الأوامر"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
date: "2026-07-18T15:22:23.284317Z"
lastmod: "2026-07-18T17:15:08.430569Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "ممارسة تصميم وتحسين نصوص الإدخال لتوجيه نماذج اللغة الكبيرة نحو المخرجات المطلوبة."
---
## Definition

تتضمن هندسة الأوامر صياغة مدخلات محددة، تُعرف بالأوامر، لاستخراج ردود دقيقة وذات صلة وعالية الجودة من نماذج الذكاء الاصطناعي التوليدية. يتطلب الأمر فهم كيفية تفسير النماذج للسياق وتوجيهها بشكل فعال.

### Summary

ممارسة تصميم وتحسين نصوص الإدخال لتوجيه نماذج اللغة الكبيرة نحو المخرجات المطلوبة.

## Key Concepts

- الإطار السياقي
- التعلم بأمثلة قليلة
- ضبط التعليمات
- تحسين الرموز

## Use Cases

- روبوتات الدردشة لخدمة العملاء الآلية
- مساعدي توليد الأكواد البرمجية
- أدوات الكتابة الإبداعية

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (نموذج لغوي كبير)](/en/terms/llm-نموذج-لغوي-كبير/)
- [Chain-of-Thought (سلسلة الأفكار)](/en/terms/chain-of-thought-سلسلة-الأفكار/)
- [RAG (الاسترجاع المعزز للتوليد)](/en/terms/rag-الاسترجاع-المعزز-للتوليد/)
- [Fine-tuning (الضبط الدقيق)](/en/terms/fine-tuning-الضبط-الدقيق/)
