---
title: "ภายใต้การดูแล"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
aliases:
  - /th/terms/supervised/
date: "2026-07-18T15:30:45.867667Z"
lastmod: "2026-07-18T16:38:07.550107Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "รูปแบบการเรียนรู้ของเครื่องที่แบบจำลองได้รับการฝึกฝนจากคู่ข้อมูลนำเข้าและผลลัพธ์ที่มีป้ายกำกับ"
---

## Definition

การเรียนรู้ภายใต้การดูแลเกี่ยวข้องกับการป้อนข้อมูลอัลกอริทึมด้วยข้อมูลที่มีทั้งข้อมูลนำเข้าและคำตอบที่ถูกต้อง (ป้ายกำกับ) แบบจำลองเรียนรู้ที่จะจับคู่ข้อมูลนำเข้ากับผลลัพธ์โดยการลดข้อผิดพลาดในการทำนาย เทคโนโลยีนี้...

### Summary

รูปแบบการเรียนรู้ของเครื่องที่แบบจำลองได้รับการฝึกฝนจากคู่ข้อมูลนำเข้าและผลลัพธ์ที่มีป้ายกำกับ

## Key Concepts

- ข้อมูลที่มีป้ายกำกับ
- การแมป
- การลดฟังก์ชันสูญเสีย

## Use Cases

- การจำแนกรูปภาพ
- การตรวจจับสแปม
- การทำนายราคา

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (ไร้การดูแล)](/en/terms/unsupervised-ไร-การด-แล/)
- [Label (ป้ายกำกับ)](/en/terms/label-ป-ายกำก-บ/)
- [Regression (การถดถอย)](/en/terms/regression-การถดถอย/)
