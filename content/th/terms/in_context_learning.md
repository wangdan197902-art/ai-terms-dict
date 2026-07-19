---
title: "การเรียนรู้ในบริบท (In-Context Learning)"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T15:23:00.632501Z"
lastmod: "2026-07-18T16:38:07.532106Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "เทคนิคที่โมเดลเรียนรู้ที่จะทำงานต่างๆ โดยสังเกตจากตัวอย่างที่ให้ไว้ในพรอมต์"
---
## Definition

การเรียนรู้ในบริบท (ICL) ช่วยให้โมเดลภาษาขนาดใหญ่ปรับตัวกับงานใหม่ได้โดยไม่ต้องอัปเดตน้ำหนักของโมเดล โดยการคู่ข้อมูลนำเข้าและผลลัพธ์ภายในบริบทของพรอมต์ โมเดลจะอนุมานรูปแบบและเรียนรู้ที่จะทำงานนั้นๆ ได้ทันที

### Summary

เทคนิคที่โมเดลเรียนรู้ที่จะทำงานต่างๆ โดยสังเกตจากตัวอย่างที่ให้ไว้ในพรอมต์

## Key Concepts

- การเรียนรู้แบบ Few-Shot (Few-Shot Learning)
- Zero-Shot (การไม่มีตัวอย่าง)
- การออกแบบพรอมต์ (Prompt Design)
- การปรับตัวโดยไม่ใช้น้ำหนัก (Weight-Free Adaptation)

## Use Cases

- การทดสอบความสามารถของโมเดลบนชุดข้อมูลใหม่อย่างรวดเร็ว
- การสลับงานแบบไดนามิกในตัวแทนสนทนา (Conversational Agents)
- การสร้างต้นแบบแอปพลิเคชัน AI โดยไม่ต้องฝึกใหม่

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering (วิศวกรรมพรอมต์)](/en/terms/prompt-engineering-ว-ศวกรรมพรอมต/)
- [Few-Shot (การเรียนรู้จากตัวอย่างจำนวนน้อย)](/en/terms/few-shot-การเร-ยนร-จากต-วอย-างจำนวนน-อย/)
- [Zero-Shot (การเรียนรู้จากไม่มีตัวอย่าง)](/en/terms/zero-shot-การเร-ยนร-จากไม-ม-ต-วอย-าง/)
- [Meta-Learning (การเรียนรู้เพื่อเรียนรู้)](/en/terms/meta-learning-การเร-ยนร-เพ-อเร-ยนร/)
