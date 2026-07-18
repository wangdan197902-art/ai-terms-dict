---
title: "การตรวจสอบความถูกต้องข้ามแบบปล่อยหนึ่งออก"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /th/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:02:29.260400Z"
lastmod: "2026-07-18T16:38:07.625567Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "เทคนิคการสุ่มตัวอย่างใหม่อย่างเข้มงวด โดยฝึกโมเดลด้วยข้อมูลทั้งหมดยกเว้นหนึ่งตัวอย่าง แล้วทดสอบกับตัวอย่างที่ถูกเก็บไว้เพียงตัวเดียว ทำซ้ำสำหรับทุกจุดข้อมูล"
---

## Definition

การตรวจสอบความถูกต้องข้ามแบบปล่อยหนึ่งออก (LOOCV) เป็นกรณีเฉพาะของการตรวจสอบความถูกต้องข้ามแบบ k-fold โดยที่ k มีค่าเท่ากับจำนวนตัวอย่างในชุดข้อมูล วิธีนี้ให้การประมาณประสิทธิภาพของโมเดลที่เกือบจะเป็นอสมมาตร (unbiased) อย่างมีนัยสำคัญ

### Summary

เทคนิคการสุ่มตัวอย่างใหม่อย่างเข้มงวด โดยฝึกโมเดลด้วยข้อมูลทั้งหมดยกเว้นหนึ่งตัวอย่าง แล้วทดสอบกับตัวอย่างที่ถูกเก็บไว้เพียงตัวเดียว ทำซ้ำสำหรับทุกจุดข้อมูล

## Key Concepts

- การสุ่มตัวอย่างใหม่
- การประเมินโมเดล
- การแลกเปลี่ยนระหว่างอคติและความแปรปรวน
- ต้นทุนในการคำนวณ

## Use Cases

- การประเมินโมเดลบนชุดข้อมูลทางการแพทย์ขนาดเล็ก
- การปรับแต่งไฮเปอร์พารามิเตอร์เมื่อข้อมูลมีจำกัด
- การเปรียบเทียบประสิทธิภาพของอัลกอริทึมอย่างเข้มงวด

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (การตรวจสอบความถูกต้องข้ามแบบ k ส่วน)](/en/terms/k-fold-cross-validation-การตรวจสอบความถ-กต-องข-ามแบบ-k-ส-วน/)
- [train_test_split (การแบ่งข้อมูลการฝึกและการทดสอบ)](/en/terms/train_test_split-การแบ-งข-อม-ลการฝ-กและการทดสอบ/)
- [bootstrap (วิธีการบูตสแตรป)](/en/terms/bootstrap-ว-ธ-การบ-ตสแตรป/)
- [cross_validation_score (คะแนนการตรวจสอบความถูกต้องข้าม)](/en/terms/cross_validation_score-คะแนนการตรวจสอบความถ-กต-องข-าม/)
