---
title: "Softmax"
term_id: "softmax"
category: "basic_concepts"
subcategory: ""
tags: ["math", "neural-networks", "classification"]
difficulty: 2
weight: 1
slug: "softmax"
aliases:
  - /th/terms/softmax/
date: "2026-07-18T15:37:44.582137Z"
lastmod: "2026-07-18T16:38:07.565434Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "ฟังก์ชันทางคณิตศาสตร์ที่แปลงเวกเตอร์ของคะแนนค่าจริงใดๆ ให้เป็นการแจกแจงความน่าจะเป็น"
---

## Definition

Softmax ถูกใช้อย่างแพร่หลายในชั้นเอาต์พุตของโครงข่ายประสาทเทียมสำหรับงานจำแนกประเภทหลายคลาส (multi-class classification) โดยจะรับเวกเตอร์ของลอจิตดิบ (raw logits) แล้วทำให้เป็นมาตรฐาน (normalize) เพื่อให้แต่ละองค์ประกอบแทนความน่าจะเป็น

### Summary

ฟังก์ชันทางคณิตศาสตร์ที่แปลงเวกเตอร์ของคะแนนค่าจริงใดๆ ให้เป็นการแจกแจงความน่าจะเป็น

## Key Concepts

- การแจกแจงความน่าจะเป็น
- ลอจิต (Logits)
- การทำให้เป็นมาตรฐาน
- การจำแนกประเภทหลายคลาส

## Use Cases

- ชั้นเอาต์พุตสำหรับการจำแนกรูปภาพ
- การทำนายโทเค็นในโมเดลภาษา
- การจัดหมวดหมู่หลายป้ายกำกับ

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (อาร์กแม็กซ์: ฟังก์ชันที่คืนค่าดัชนีของค่าสูงสุด)](/en/terms/argmax-อาร-กแม-กซ-ฟ-งก-ช-นท-ค-นค-าด-ชน-ของค-าส-งส-ด/)
- [Cross-Entropy Loss (ครอส-เอนโทรปีลอส: ฟังก์ชันการสูญเสียที่ใช้วัดความแตกต่างระหว่างการแจกแจงความน่าจะเป็นสองแบบ)](/en/terms/cross-entropy-loss-ครอส-เอนโทรป-ลอส-ฟ-งก-ช-นการส-ญเส-ยท-ใช-ว-ดความแตกต-างระหว-างการแจกแจงความน-าจะเป-นสองแบบ/)
- [Logits (ลอจิต: ค่าดิบก่อนผ่านฟังก์ชันกระตุ้น)](/en/terms/logits-ลอจ-ต-ค-าด-บก-อนผ-านฟ-งก-ช-นกระต-น/)
- [Neural Network (โครงข่ายประสาทเทียม)](/en/terms/neural-network-โครงข-ายประสาทเท-ยม/)
