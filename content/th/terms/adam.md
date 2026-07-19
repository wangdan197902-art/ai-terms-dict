---
title: "Adam"
term_id: "adam"
category: "basic_concepts"
subcategory: ""
tags: ["Optimization", "Deep Learning", "Algorithms"]
difficulty: 3
weight: 1
slug: "adam"
date: "2026-07-18T15:23:14.000938Z"
lastmod: "2026-07-18T16:38:07.532540Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "อัลกอริทึมการหาค่าเหมาะที่สุด (optimization) ที่คำนวณอัตราการเรียนรู้แบบปรับได้สำหรับแต่ละพารามิเตอร์"
---
## Definition

Adam (Adaptive Moment Estimation) เป็นอัลกอริทึมการหาค่าเหมาะที่สุดอันดับหนึ่ง (first-order) ที่ใช้เกรเดียนต์อย่างแพร่หลายในการฝึกเครือข่ายประสาทเทียมเชิงลึก โดยมันผสานข้อดีของการขยายความก้าวหน้าสองรูปแบบอื่นของกระบวนการสุ่ม

### Summary

อัลกอริทึมการหาค่าเหมาะที่สุด (optimization) ที่คำนวณอัตราการเรียนรู้แบบปรับได้สำหรับแต่ละพารามิเตอร์

## Key Concepts

- การไล่ระดับลง (Gradient Descent)
- อัตราการเรียนรู้ (Learning Rate)
- โมเมนตัม (Momentum)
- การประมาณความแปรปรวน (Variance Estimation)

## Use Cases

- การฝึกเรียนรู้เชิงลึก (Deep Learning Training)
- แบบจำลองการมองเห็นด้วยคอมพิวเตอร์ (Computer Vision Models)
- การประมวลผลภาษาธรรมชาติ (Natural Language Processing)

## Code Example

```python
import torch.optim as optim
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

## Related Terms

- [SGD - Stochastic Gradient Descent](/en/terms/sgd-stochastic-gradient-descent/)
- [RMSProp - อัลกอริทึมการปรับอัตราการเรียนรู้](/en/terms/rmsprop-อ-ลกอร-ท-มการปร-บอ-ตราการเร-ยนร/)
- [Optimizer - ตัวหาค่าเหมาะที่สุด](/en/terms/optimizer-ต-วหาค-าเหมาะท-ส-ด/)
- [Backpropagation - การแพร่ย้อนกลับ](/en/terms/backpropagation-การแพร-ย-อนกล-บ/)
