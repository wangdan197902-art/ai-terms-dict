---
title: เมทริกซ์ความสับสน (Confusion Matrix)
term_id: confusion_matrix
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Classification
- metrics
difficulty: 2
weight: 1
slug: confusion_matrix
date: '2026-07-18T15:46:33.414882Z'
lastmod: '2026-07-18T16:38:07.588372Z'
draft: false
source: agnes_llm
status: published
language: th
description: ตารางที่ใช้สำหรับอธิบายประสิทธิภาพของแบบจำลองการจำแนกประเภทบนชุดข้อมูลทดสอบ
---
## Definition

เมทริกซ์ความสับสนคือรูปแบบตารางเฉพาะที่ช่วยให้สามารถมองเห็นประสิทธิภาพของอัลกอริทึมได้ โดยมักใช้กับอัลกอริทึมการเรียนรู้ภายใต้การดูแล (supervised learning) ตารางนี้จะแสดงจำนวนของผลบวกจริง (true positives), ผลลบจริง (true negatives), ผลบวกปลอม (false positives), และผลลบปลอม (false negatives) เพื่อประเมินความแม่นยำและความคลาดเคลื่อนของแบบจำลอง

### Summary

ตารางที่ใช้สำหรับอธิบายประสิทธิภาพของแบบจำลองการจำแนกประเภทบนชุดข้อมูลทดสอบ

## Key Concepts

- ผลบวกจริง (True Positives)
- ผลลบปลอม (False Negatives)
- ความแม่นยำ (Precision)
- ค่าความครอบคลุม (Recall)

## Use Cases

- การประเมินตัวจำแนกประเภทแบบไบนารี (Binary Classifiers)
- การวิเคราะห์ประสิทธิภาพของการจำแนกประเภทหลายคลาส (Multi-class Classification)
- การแก้ไขอคติของแบบจำลองในชุดข้อมูลที่ไม่สมดุล (Imbalanced Datasets)

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (ความแม่นยำ)](/en/terms/precision-ความแม-นยำ/)
- [recall (ค่าความครอบคลุม)](/en/terms/recall-ค-าความครอบคล-ม/)
- [F1 score (คะแนนเอฟวัน)](/en/terms/f1-score-คะแนนเอฟว-น/)
- [ROC curve (เส้นโค้ง ROC)](/en/terms/roc-curve-เส-นโค-ง-roc/)
