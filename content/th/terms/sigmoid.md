---
title: "ซิกมอยด์"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:15:04.371234Z"
lastmod: "2026-07-18T16:38:07.653881Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "ฟังก์ชันทางคณิตศาสตร์ที่แมปค่าจริงใดๆ ให้เป็นค่าระหว่างศูนย์ถึงหนึ่ง โดยมีรูปร่างเป็นเส้นโค้งรูปตัว S"
---
## Definition

ฟังก์ชันซิกมอยด์ ซึ่งนิยามโดย σ(z) = 1 / (1 + e^-z) ถูกใช้อย่างแพร่หลายในการเรียนรู้ของเครื่องเพื่อสร้างแบบจำลองความน่าจะเป็น ฟังก์ชันนี้จะบีบอัดค่าอินพุตให้อยู่ในช่วง (0, 1) ทำให้เหมาะสำหรับการจำแนกประเภทแบบไบนารี

### Summary

ฟังก์ชันทางคณิตศาสตร์ที่แมปค่าจริงใดๆ ให้เป็นค่าระหว่างศูนย์ถึงหนึ่ง โดยมีรูปร่างเป็นเส้นโค้งรูปตัว S

## Key Concepts

- ฟังก์ชันลอจิสติก
- การแมปความน่าจะเป็น
- เกรเดียนต์หายไป
- ความไม่เป็นเชิงเส้น

## Use Cases

- เอาต์พุตการจำแนกประเภทแบบไบนารี
- การถดถอยลอจิสติก
- ฟังก์ชันกระตุ้นในเครือข่ายประสาทเทียมชั้นตื้น

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU (Rectified Linear Unit)](/en/terms/relu-rectified-linear-unit/)
- [Softmax (ฟังก์ชันสำหรับหลายคลาส)](/en/terms/softmax-ฟ-งก-ช-นสำหร-บหลายคลาส/)
- [Logistic Regression (การถดถอยลอจิสติก)](/en/terms/logistic-regression-การถดถอยลอจ-สต-ก/)
- [Activation Function (ฟังก์ชันกระตุ้น)](/en/terms/activation-function-ฟ-งก-ช-นกระต-น/)
