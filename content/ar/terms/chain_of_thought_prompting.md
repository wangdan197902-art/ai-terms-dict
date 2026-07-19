---
title: "التوجيه بتسلسل الأفكار"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T15:35:59.726559Z"
lastmod: "2026-07-18T17:15:08.459136Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "التوجيه بتسلسل الأفكار هو تقنية تشجع نماذج اللغة الكبيرة على توليد خطوات استنتاج وسيطة قبل إنتاج الإجابة النهائية."
---
## Definition

يحسن التوجيه بتسلسل الأفكار (CoT) أداء نماذج اللغة الكبيرة في مهام الاستدلال المعقدة من خلال طلب النموذج صراحةً لشرح منطق خطوة بخطوة. بدلاً من القفز مباشرة إلى النتيجة، يقوم النموذج بتحليل المشكلة وتفكيكها، مما يزيد من دقة الإجابات في المهام المنطقية والرياضية.

### Summary

التوجيه بتسلسل الأفكار هو تقنية تشجع نماذج اللغة الكبيرة على توليد خطوات استنتاج وسيطة قبل إنتاج الإجابة النهائية.

## Key Concepts

- الاستدلال خطوة بخطوة
- التعلم بعدد قليل من الأمثلة
- الاستنتاج المنطقي
- الخطوات الوسيطة

## Use Cases

- حل مسائل الرياضيات اللفظية
- مهام الاستدلال المنطقي المعقد
- تصحيح أخطاء توليد الكود

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (التوجيه بدون أمثلة)](/en/terms/zero-shot-prompting-التوجيه-بدون-أمثلة/)
- [Few-Shot Prompting (التوجيه بعدد قليل من الأمثلة)](/en/terms/few-shot-prompting-التوجيه-بعدد-قليل-من-الأمثلة/)
- [Self-Consistency (الاتساق الذاتي)](/en/terms/self-consistency-الاتساق-الذاتي/)
- [Reasoning (الاستدلال)](/en/terms/reasoning-الاستدلال/)
