---
title: การกำหนดคำสั่งแบบ Few-Shot
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
date: '2026-07-18T15:35:35.979498Z'
lastmod: '2026-07-18T16:38:07.560730Z'
draft: false
source: agnes_llm
status: published
language: th
description: การกำหนดคำสั่งแบบ Few-Shot คือเทคนิคที่ให้โมเดลภาษาขนาดใหญ่ (LLMs) เห็นตัวอย่างอินพุต-เอาต์พุตจำนวนน้อยภายในคำสั่งเพื่อกำหนดพฤติกรรม
---
## Definition

วิธีการนี้ใช้ประโยชน์จากความสามารถในการเรียนรู้จากบริบท (in-context learning) ของโมเดลภาษาขนาดใหญ่โดยการจัดเตรียมตัวอย่างที่เป็นรูปธรรมไว้ในคำสั่งโดยตรง ซึ่งแตกต่างจากการปรับแต่งโมเดล (fine-tuning) ที่ต้องอัปเดตน้ำหนักของโมเดล วิธีนี้ช่วยให้โมเดลเข้าใจรูปแบบที่ต้องการโดยไม่ต้องฝึกใหม่ทั้งชุด

### Summary

การกำหนดคำสั่งแบบ Few-Shot คือเทคนิคที่ให้โมเดลภาษาขนาดใหญ่ (LLMs) เห็นตัวอย่างอินพุต-เอาต์พุตจำนวนน้อยภายในคำสั่งเพื่อกำหนดพฤติกรรม

## Key Concepts

- การเรียนรู้จากบริบท
- วิศวกรรมคำสั่ง
- การแนะนำด้วยตัวอย่าง
- การเปรียบเทียบกับ Zero-shot

## Use Cases

- การจัดรูปแบบการวิเคราะห์ความรู้สึก
- การปรับสไตล์การเขียนโค้ด
- การดึงข้อมูลโครงสร้าง

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

- [zero_shot (Zero-shot)](/en/terms/zero_shot-zero-shot/)
- [prompt_engineering (วิศวกรรมคำสั่ง)](/en/terms/prompt_engineering-ว-ศวกรรมคำส-ง/)
- [in_context_learning (การเรียนรู้จากบริบท)](/en/terms/in_context_learning-การเร-ยนร-จากบร-บท/)
- [llm (โมเดลภาษาขนาดใหญ่)](/en/terms/llm-โมเดลภาษาขนาดใหญ/)
