---
title: โมเดลตัวแทน
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T16:17:00.925240Z'
lastmod: '2026-07-18T16:38:07.659544Z'
draft: false
source: agnes_llm
status: published
language: th
description: โมเดลทางคณิตศาสตร์แบบง่ายที่ใช้ประมาณพฤติกรรมของโมเดลกล่องดำที่ซับซ้อน
  ใช้ทรัพยากรคำนวณสูง หรือเข้าถึงได้ยาก
---
## Definition

ในแมชชีนเลิร์นนิงและการเพิ่มประสิทธิภาพ โมเดลตัวแทนจะทำหน้าที่เป็นตัวแทนของฟังก์ชันเป้าหมายที่ประเมินโดยตรงได้ยาก โดยจะถูกฝึกฝนจากคู่ข้อมูลอินพุต-เอาต์พุตของโมเดลเดิมเพื่อให้ได้ผลลัพธ์ที่ใกล้เคียง

### Summary

โมเดลทางคณิตศาสตร์แบบง่ายที่ใช้ประมาณพฤติกรรมของโมเดลกล่องดำที่ซับซ้อน ใช้ทรัพยากรคำนวณสูง หรือเข้าถึงได้ยาก

## Key Concepts

- การประมาณค่าโมเดล
- การเพิ่มประสิทธิภาพกล่องดำ
- ประสิทธิภาพด้านการคำนวณ
- โมเดลตัวแทน

## Use Cases

- การปรับแต่งไฮเปอร์พารามิเตอร์
- การเร่งความเร็วการจำลองการออกแบบทางวิศวกรรม
- การวิเคราะห์ความไวของระบบที่ซับซ้อน

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Bayesian Optimization (การเพิ่มประสิทธิภาพแบบเบย์)](/en/terms/bayesian-optimization-การเพ-มประส-ทธ-ภาพแบบเบย/)
- [Gaussian Process (กระบวนการเกาส์เซียน)](/en/terms/gaussian-process-กระบวนการเกาส-เซ-ยน/)
- [Black-Box Function (ฟังก์ชันกล่องดำ)](/en/terms/black-box-function-ฟ-งก-ช-นกล-องดำ/)
- [Emulator (โปรแกรมจำลอง)](/en/terms/emulator-โปรแกรมจำลอง/)
