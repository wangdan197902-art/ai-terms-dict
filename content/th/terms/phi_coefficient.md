---
title: สัมประสิทธิ์ฟี
term_id: phi_coefficient
category: basic_concepts
subcategory: ''
tags:
- statistics
- Evaluation Metrics
- Binary Classification
difficulty: 3
weight: 1
slug: phi_coefficient
date: '2026-07-18T16:11:02.648497Z'
lastmod: '2026-07-18T16:38:07.642175Z'
draft: false
source: agnes_llm
status: published
language: th
description: มาตรการทางสถิติที่ใช้วัดความสัมพันธ์ระหว่างตัวแปรไบนารีสองตัว
---
## Definition

สัมประสิทธิ์ฟี (φ) เป็นมาตรการวัดความสัมพันธ์ระหว่างตัวแปรไบนารีสองตัว โดยทำหน้าที่เป็นสัมประสิทธิ์สหสัมพันธ์ของเพียร์สันสำหรับตัวแปรทวิภาค มีค่าอยู่ในช่วง -1 ถึง +1 โดยที่ 0 บ่งชี้ว่าไม่มีความสัมพันธ์

### Summary

มาตรการทางสถิติที่ใช้วัดความสัมพันธ์ระหว่างตัวแปรไบนารีสองตัว

## Key Concepts

- ตัวแปรไบนารี
- สหสัมพันธ์
- ตารางฉุกเฉิน
- ความแข็งแกร่งของความสัมพันธ์

## Use Cases

- ประเมินประสิทธิภาพของตัวจำแนกประเภทไบนารีเพิ่มเติมจากความแม่นยำ
- วิเคราะห์ความสัมพันธ์ในข้อมูลสำรวจที่มีคำตอบใช่/ไม่ใช่
- การเลือกคุณลักษณะในชุดข้อมูลที่มีข้อมูลป้อนเข้าแบบหมวดหมู่

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [Cramer's V (ค่าวีของคราเมอร์)](/en/terms/cramer-s-v-ค-าว-ของคราเมอร/)
- [Pearson correlation (สหสัมพันธ์ของเพียร์สัน)](/en/terms/pearson-correlation-สหส-มพ-นธ-ของเพ-ยร-ส-น/)
- [Confusion matrix (เมทริกซ์ความสับสน)](/en/terms/confusion-matrix-เมทร-กซ-ความส-บสน/)
- [Mutual information (ข้อมูลร่วม)](/en/terms/mutual-information-ข-อม-ลร-วม/)
