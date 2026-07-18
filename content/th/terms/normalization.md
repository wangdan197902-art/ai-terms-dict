---
title: "การปรับให้เป็นมาตรฐาน"
term_id: "normalization"
category: "basic_concepts"
subcategory: ""
tags: ["data_preprocessing", "mathematics", "ml_basics"]
difficulty: 2
weight: 1
slug: "normalization"
aliases:
  - /th/terms/normalization/
date: "2026-07-18T16:08:08.826290Z"
lastmod: "2026-07-18T16:38:07.636921Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "การปรับให้เป็นมาตรฐานเป็นเทคนิคการเตรียมข้อมูลล่วงหน้าซึ่งปรับสเกลคุณลักษณะเชิงตัวเลขให้อยู่ในช่วงมาตรฐาน มักอยู่ระหว่าง 0 ถึง 1 เพื่อปรับปรุงการลู่เข้าและประสิทธิภาพของโมเดล"
---

## Definition

วิธีการทั่วไปรวมถึงการปรับสเกล Min-Max และการทำให้เป็นมาตรฐานแบบ Z-score กระบวนการนี้มั่นใจว่าคุณลักษณะที่มีขนาดใหญ่มากจะไม่ครอบงำอัลกอริทึมการเรียนรู้ โดยเฉพาะในอัลกอริทึมการหาค่าเหมาะที่สุดแบบไล่ระดับ

### Summary

การปรับให้เป็นมาตรฐานเป็นเทคนิคการเตรียมข้อมูลล่วงหน้าซึ่งปรับสเกลคุณลักษณะเชิงตัวเลขให้อยู่ในช่วงมาตรฐาน มักอยู่ระหว่าง 0 ถึง 1 เพื่อปรับปรุงการลู่เข้าและประสิทธิภาพของโมเดล

## Key Concepts

- การปรับสเกล Min-Max
- การทำให้เป็นมาตรฐานแบบ Z-Score
- การปรับสเกลคุณลักษณะ
- ความเสถียรของการไล่ระดับ

## Use Cases

- การเตรียมข้อมูลพิกเซลภาพ
- การเตรียมข้อมูลตารางสำหรับเครือข่ายประสาท
- การเพิ่มความแม่นยำของโมเดลถดถอย

## Code Example

```python
from sklearn.preprocessing import MinMaxScaler
import numpy as np
data = np.array([[10], [20], [30]])
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)
```

## Related Terms

- [Standardization (การทำให้เป็นมาตรฐาน)](/en/terms/standardization-การทำให-เป-นมาตรฐาน/)
- [Data Preprocessing (การเตรียมข้อมูลล่วงหน้า)](/en/terms/data-preprocessing-การเตร-ยมข-อม-ลล-วงหน-า/)
- [Feature Engineering (วิศวกรรมคุณลักษณะ)](/en/terms/feature-engineering-ว-ศวกรรมค-ณล-กษณะ/)
