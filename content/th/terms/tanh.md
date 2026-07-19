---
title: Tanh (แทนเจนต์ไฮเพอร์โบลิก)
term_id: tanh
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- mathematics
difficulty: 2
weight: 1
slug: tanh
date: '2026-07-18T16:17:15.132140Z'
lastmod: '2026-07-18T16:38:07.660353Z'
draft: false
source: agnes_llm
status: published
language: th
description: Tanh หรือ hyperbolic tangent เป็นฟังก์ชันกระตุ้นที่แมปค่าอินพุตไปยังช่วงระหว่าง
  -1 ถึง 1
---
## Definition

ฟังก์ชันแทนเจนต์ไฮเพอร์โบลิก (Tanh) เป็นฟังก์ชันกระตุ้นแบบไม่เชิงเส้นที่ใช้ทั่วไปในโครงข่ายประสาทเทียม มันบีบอัดค่าอินพุตให้อยู่ในช่วง (-1, 1) ให้ผลลัพธ์ที่มีศูนย์เป็นศูนย์กลางซึ่งช่วย

### Summary

Tanh หรือ hyperbolic tangent เป็นฟังก์ชันกระตุ้นที่แมปค่าอินพุตไปยังช่วงระหว่าง -1 ถึง 1

## Key Concepts

- ฟังก์ชันกระตุ้น
- ความไม่เชิงเส้น
- ผลลัพธ์ที่มีศูนย์เป็นศูนย์กลาง
- การแพร่ย้อนกลับ

## Use Cases

- โครงข่ายประสาทเทียมแบบวนซ้ำ
- เกตของเซลล์ LSTM
- เลเยอร์ซ่อนใน MLP

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (ซิกมอยด์)](/en/terms/sigmoid-ซ-กมอยด/)
- [relu (รีลู)](/en/terms/relu-ร-ล/)
- [neural_networks (โครงข่ายประสาทเทียม)](/en/terms/neural_networks-โครงข-ายประสาทเท-ยม/)
