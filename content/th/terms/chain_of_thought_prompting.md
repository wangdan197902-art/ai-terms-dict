---
title: "Chain-of-Thought Prompting"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T15:34:56.358222Z"
lastmod: "2026-07-18T16:38:07.558955Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "การให้คำแนะนำแบบโซ่ความคิดเป็นเทคนิคที่กระตุ้นให้โมเดลภาษาขนาดใหญ่ (LLMs) สร้างขั้นตอนการให้เหตุผลขั้นกลางก่อนที่จะผลิตคำตอบสุดท้าย"
---
## Definition

การให้คำแนะนำแบบโซ่ความคิด (Chain-of-Thought หรือ CoT) ช่วยปรับปรุงประสิทธิภาพของโมเดลภาษาขนาดใหญ่ในงานให้เหตุผลที่ซับซ้อน โดยการขอให้โมเดลแสดงตรรกะทีละขั้นตอนอย่างชัดเจน แทนที่จะกระโดดไปสู่คำตอบทันที ซึ่งช่วยให้โมเดลสามารถติดตามลำดับความคิดได้อย่างมีเหตุผลมากขึ้น

### Summary

การให้คำแนะนำแบบโซ่ความคิดเป็นเทคนิคที่กระตุ้นให้โมเดลภาษาขนาดใหญ่ (LLMs) สร้างขั้นตอนการให้เหตุผลขั้นกลางก่อนที่จะผลิตคำตอบสุดท้าย

## Key Concepts

- การให้เหตุผลทีละขั้นตอน (Step-by-Step Reasoning)
- การเรียนรู้แบบ Few-Shot (Few-Shot Learning)
- การอนุมานเชิงตรรกะ (Logical Deduction)
- ขั้นตอนขั้นกลาง (Intermediate Steps)

## Use Cases

- การแก้โจทย์คณิตศาสตร์ในรูปแบบข้อความ
- งานให้เหตุผลเชิงตรรกะที่ซับซ้อน
- การแก้ไขข้อผิดพลาดจากการสร้างโค้ด

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (การให้คำแนะนำแบบไม่มีตัวอย่าง)](/en/terms/zero-shot-prompting-การให-คำแนะนำแบบไม-ม-ต-วอย-าง/)
- [Few-Shot Prompting (การให้คำแนะนำแบบมีตัวอย่างน้อย)](/en/terms/few-shot-prompting-การให-คำแนะนำแบบม-ต-วอย-างน-อย/)
- [Self-Consistency (ความสอดคล้องในตัวเอง)](/en/terms/self-consistency-ความสอดคล-องในต-วเอง/)
- [Reasoning (การให้เหตุผล)](/en/terms/reasoning-การให-เหต-ผล/)
