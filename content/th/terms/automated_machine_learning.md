---
title: "การเรียนรู้ของเครื่องอัตโนมัติ (Automated machine learning)"
term_id: "automated_machine_learning"
category: "training_techniques"
subcategory: ""
tags: ["automation", "efficiency", "workflow"]
difficulty: 3
weight: 1
slug: "automated_machine_learning"
aliases:
  - /th/terms/automated_machine_learning/
date: "2026-07-18T15:43:09.760744Z"
lastmod: "2026-07-18T16:38:07.576938Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "ระเบียบวิธีที่ทำการอัตโนมัติกระบวนการทั้งหมดของการนำการเรียนรู้ของเครื่องไปแก้ปัญหาในโลกจริง ลดความพยายามในการดำเนินงานด้วยมือ"
---

## Definition

AutoML (Automated Machine Learning) ช่วยให้การพัฒนารูปแบบ ML เป็นไปอย่างราบรื่นโดยการทำให้เป็นอัตโนมัติซึ่งงานต่างๆ เช่น การเตรียมข้อมูลก่อนประมวลผล วิศวกรรมฟีเจอร์ การเลือกแบบจำลอง และการปรับแต่งไฮเปอร์พารามิเตอร์ ทำให้ผู้ใช้ทั่วไปเข้าถึงได้ง่ายขึ้น

### Summary

ระเบียบวิธีที่ทำการอัตโนมัติกระบวนการทั้งหมดของการนำการเรียนรู้ของเครื่องไปแก้ปัญหาในโลกจริง ลดความพยายามในการดำเนินงานด้วยมือ

## Key Concepts

- การปรับแต่งไฮเปอร์พารามิเตอร์ (Hyperparameter Tuning)
- วิศวกรรมฟีเจอร์ (Feature Engineering)
- การเลือกแบบจำลอง (Model Selection)
- การทำให้เป็นประชาธิปไตย (Democratization)

## Use Cases

- การสร้างต้นแบบอย่างรวดเร็วสำหรับผู้วิเคราะห์ธุรกิจ
- การเพิ่มประสิทธิภาพสายการผลิตขนาดใหญ่
- การเปรียบเทียบอัลกอริทึมหลายตัวโดยอัตโนมัติ

## Code Example

```python
from auto_ml import Predictor
predictor = Predictor(type_of_estimator='classifier')
predictor.fit(dataframe, target='label')
```

## Related Terms

- [Hyperparameter Optimization (การเพิ่มประสิทธิภาพไฮเปอร์พารามิเตอร์)](/en/terms/hyperparameter-optimization-การเพ-มประส-ทธ-ภาพไฮเปอร-พาราม-เตอร/)
- [Neural Architecture Search (การค้นหาโครงสร้างประสาทเทียม)](/en/terms/neural-architecture-search-การค-นหาโครงสร-างประสาทเท-ยม/)
- [MLOps (ปฏิบัติการการเรียนรู้ของเครื่อง)](/en/terms/mlops-ปฏ-บ-ต-การการเร-ยนร-ของเคร-อง/)
- [No-Code AI (AI แบบไม่ต้องเขียนโค้ด)](/en/terms/no-code-ai-ai-แบบไม-ต-องเข-ยนโค-ด/)
