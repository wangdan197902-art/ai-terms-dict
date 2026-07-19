---
title: ข้อมูลที่มีป้ายกำกับ (Labeled Data)
term_id: labeled_data
category: basic_concepts
subcategory: ''
tags:
- data
- Supervised Learning
- fundamentals
difficulty: 1
weight: 1
slug: labeled_data
date: '2026-07-18T16:01:57.262117Z'
lastmod: '2026-07-18T16:38:07.624218Z'
draft: false
source: agnes_llm
status: published
language: th
description: ข้อมูลที่มีค่าผลลัพธ์หรือเป้าหมายที่ถูกต้องระบุไว้คู่กับคุณลักษณะของข้อมูลนำเข้า
---
## Definition

ข้อมูลที่มีป้ายกำกับประกอบด้วยตัวอย่างข้อมูลนำเข้าที่จับคู่กับป้ายกำกับความจริงพื้นฐาน (ground truth) ที่สอดคล้องกัน ซึ่งเป็นรากฐานของการเรียนรู้ของเครื่องแบบมีผู้ดูแล (supervised machine learning) ข้อมูลนี้ช่วยให้อัลกอริทึมสามารถเรียนรู้การแมปpping ระหว่างข้อมูลนำเข้าและผลลัพธ์ที่ต้องการได้

### Summary

ข้อมูลที่มีค่าผลลัพธ์หรือเป้าหมายที่ถูกต้องระบุไว้คู่กับคุณลักษณะของข้อมูลนำเข้า

## Key Concepts

- การเรียนรู้แบบมีผู้ดูแล (Supervised Learning)
- ความจริงพื้นฐาน (Ground Truth)
- การติดป้ายกำกับ (Annotation)
- ตัวแปรเป้าหมาย (Target Variable)

## Use Cases

- การฝึกฝนตัวจำแนกรูปภาพ (Image Classifiers)
- การสร้างระบบรู้จำเสียงพูด
- การสร้างแบบจำลองการทำนายในภาคการเงิน

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (ข้อมูลไม่มีป้ายกำกับ)](/en/terms/unlabeled_data-ข-อม-ลไม-ม-ป-ายกำก-บ/)
- [supervised_learning (การเรียนรู้แบบมีผู้ดูแล)](/en/terms/supervised_learning-การเร-ยนร-แบบม-ผ-ด-แล/)
- [data_annotation (การติดป้ายกำกับข้อมูล)](/en/terms/data_annotation-การต-ดป-ายกำก-บข-อม-ล/)
- [training_set (ชุดข้อมูลสำหรับการฝึกสอน)](/en/terms/training_set-ช-ดข-อม-ลสำหร-บการฝ-กสอน/)
