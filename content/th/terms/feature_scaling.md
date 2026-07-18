---
title: "การปรับสเกลคุณลักษณะ (Feature Scaling)"
term_id: "feature_scaling"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "statistics", "optimization"]
difficulty: 2
weight: 1
slug: "feature_scaling"
aliases:
  - /th/terms/feature_scaling/
date: "2026-07-18T15:53:39.072088Z"
lastmod: "2026-07-18T16:38:07.606071Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "กระบวนการปรับช่วงของตัวแปรอิสระหรือคุณลักษณะของข้อมูลให้เป็นมาตรฐานเพื่อให้มีขนาดเท่าเทียมกัน"
---

## Definition

การปรับสเกลคุณลักษณะทำให้ช่วงของตัวแปรอินพุตเป็นมาตรฐานเพื่อป้องกันไม่ให้คุณลักษณะที่มีค่ามากเกินกว่าควบคุมกระบวนการเรียนรู้ วิธีการทั่วไปรวมถึงการนอร์มัลไลเซชัน (การปรับสเกลแบบมิน-แม็กซ์) และการทำให้เป็นมาตรฐาน (Standardization) ซึ่งช่วยเร่งความเร็วในการลู่เข้าของอัลกอริทึมการเพิ่มประสิทธิภาพ

### Summary

กระบวนการปรับช่วงของตัวแปรอิสระหรือคุณลักษณะของข้อมูลให้เป็นมาตรฐานเพื่อให้มีขนาดเท่าเทียมกัน

## Key Concepts

- การนอร์มัลไลเซชัน
- การทำให้เป็นมาตรฐาน
- เกรเดียนต์ดีเซนต์
- การเตรียมข้อมูลก่อนประมวลผล

## Use Cases

- การฝึกฝนเครือข่ายประสาทเทียม
- การจัดกลุ่มแบบ K-means
- เครื่องเวกเตอร์สนับสนุน (SVM)

## Code Example

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
```

## Related Terms

- [Min-Max Scaling (การปรับสเกลมิน-แม็กซ์)](/en/terms/min-max-scaling-การปร-บสเกลม-น-แม-กซ/)
- [Z-score Normalization (การนอร์มัลไลเซชันคะแนน Z)](/en/terms/z-score-normalization-การนอร-ม-ลไลเซช-นคะแนน-z/)
- [Data preprocessing (การเตรียมข้อมูลก่อนประมวลผล)](/en/terms/data-preprocessing-การเตร-ยมข-อม-ลก-อนประมวลผล/)
- [Gradient Descent (เกรเดียนต์ดีเซนต์)](/en/terms/gradient-descent-เกรเด-ยนต-ด-เซนต/)
