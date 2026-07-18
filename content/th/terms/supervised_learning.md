---
title: "การเรียนรู้ด้วยข้อมูลที่มีผู้สอน"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /th/terms/supervised_learning/
date: "2026-07-18T15:37:44.582195Z"
lastmod: "2026-07-18T16:38:07.565810Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "รูปแบบการเรียนรู้ของเครื่องที่โมเดลเรียนรู้ที่จะจับคู่ข้อมูลนำเข้ากับผลลัพธ์โดยอาศัยตัวอย่างการฝึกที่มีป้ายกำกับ"
---

## Definition

ในการเรียนรู้ด้วยข้อมูลที่มีผู้สอน อัลกอริทึมจะถูกฝึกฝนบนชุดข้อมูลที่มีป้ายกำกับ ซึ่งหมายความว่าตัวอย่างข้อมูลนำเข้าแต่ละตัวจะจับคู่กับผลลัพธ์ที่ถูกต้อง เป้าหมายคือเพื่อให้โมเดลเรียนรู้ความสัมพันธ์พื้นฐานระหว่างข้อมูลนำเข้าและผลลัพธ์

### Summary

รูปแบบการเรียนรู้ของเครื่องที่โมเดลเรียนรู้ที่จะจับคู่ข้อมูลนำเข้ากับผลลัพธ์โดยอาศัยตัวอย่างการฝึกที่มีป้ายกำกับ

## Key Concepts

- ข้อมูลที่มีป้ายกำกับ
- การจับคู่ข้อมูลเข้า-ออก
- การจำแนกประเภท
- การถดถอย

## Use Cases

- การตรวจจับอีเมลสแปม
- การทำนายราคาบ้าน
- การจดจำรูปภาพ

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (การเรียนรู้ด้วยข้อมูลไม่มีผู้สอน)](/en/terms/unsupervised-learning-การเร-ยนร-ด-วยข-อม-ลไม-ม-ผ-สอน/)
- [Training Set (ชุดข้อมูลฝึกฝน)](/en/terms/training-set-ช-ดข-อม-ลฝ-กฝน/)
- [Validation Set (ชุดข้อมูลตรวจสอบ)](/en/terms/validation-set-ช-ดข-อม-ลตรวจสอบ/)
- [Model Accuracy (ความแม่นยำของโมเดล)](/en/terms/model-accuracy-ความแม-นยำของโมเดล/)
