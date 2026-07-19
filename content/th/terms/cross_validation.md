---
title: การตรวจสอบไขว้ (Cross-validation)
term_id: cross_validation
category: training_techniques
subcategory: ''
tags:
- evaluation
- Machine Learning
- statistics
difficulty: 2
weight: 1
slug: cross_validation
date: '2026-07-18T15:47:18.454439Z'
lastmod: '2026-07-18T16:38:07.590813Z'
draft: false
source: agnes_llm
status: published
language: th
description: ขั้นตอนการสุ่มตัวอย่างใหม่เพื่อประเมินสมรรถนะของแบบจำลองแมชชีนเลิร์นนิงบนชุดข้อมูลจำกัด
  โดยการแบ่งข้อมูลออกเป็นกลุ่มย่อยสำหรับการฝึกและทดสอบ
---
## Definition

การตรวจสอบไขว้เป็นวิธีการทางสถิติที่ใช้ประมาณการสมรรถนะของแบบจำลองแมชชีนเลิร์นนิง รูปแบบที่พบบ่อยที่สุดคือ k-fold cross-validation ซึ่งแบ่งข้อมูลออกเป็น k ส่วนเท่าๆ กัน จากนั้นจะทำการฝึกแบบจำลอง k ครั้ง โดยในแต่ละครั้งจะใช้ข้อมูล k-1 ส่วนสำหรับการฝึก และอีก 1 ส่วนที่เหลือสำหรับการทดสอบ เพื่อประเมินความแม่นยำและความสามารถในการสรุปผลของแบบจำลอง

### Summary

ขั้นตอนการสุ่มตัวอย่างใหม่เพื่อประเมินสมรรถนะของแบบจำลองแมชชีนเลิร์นนิงบนชุดข้อมูลจำกัด โดยการแบ่งข้อมูลออกเป็นกลุ่มย่อยสำหรับการฝึกและทดสอบ

## Key Concepts

- การแบ่งแบบ K-Fold
- ความสามารถในการสรุปผลของแบบจำลอง
- การตรวจจับการฟิตเกิน (Overfitting)
- การประมาณค่าสมรรถนะ

## Use Cases

- การปรับแต่งไฮเปอร์พารามิเตอร์
- การเปรียบเทียบอัลกอริทึมต่างๆ
- การตรวจสอบความเสถียรของแบบจำลองบนชุดข้อมูลขนาดเล็ก

## Code Example

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X, y, cv=5)
```

## Related Terms

- [Train-Test Split (การแบ่งข้อมูลฝึกและทดสอบ)](/en/terms/train-test-split-การแบ-งข-อม-ลฝ-กและทดสอบ/)
- [Leave-One-Out (การทิ้งหนึ่งออก)](/en/terms/leave-one-out-การท-งหน-งออก/)
- [Bootstrap (บู้ตสแตรป)](/en/terms/bootstrap-บ-ตสแตรป/)
