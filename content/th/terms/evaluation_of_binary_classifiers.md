---
title: การประเมินตัวจำแนกประเภทแบบไบนารี
term_id: evaluation_of_binary_classifiers
category: basic_concepts
subcategory: ''
tags:
- metrics
- Classification
- evaluation
difficulty: 2
weight: 1
slug: evaluation_of_binary_classifiers
date: '2026-07-18T15:52:35.884188Z'
lastmod: '2026-07-18T16:38:07.603690Z'
draft: false
source: agnes_llm
status: published
language: th
description: กระบวนการประเมินประสิทธิภาพของโมเดลแมชชีนเลิร์นนิงที่ทำนายผลลัพธ์ที่เป็นไปได้สองอย่าง
---
## Definition

สาขานี้เกี่ยวข้องกับการวิเคราะห์เมตริกต่างๆ เช่น ความแม่นยำ (Accuracy), ค่าความแม่นยำ (Precision), ค่าความครอบคลุม (Recall), ค่า F1-score และพื้นที่ใต้เส้นโค้ง ROC (AUC-ROC) ช่วยกำหนดว่าโมเดลสามารถแยกแยะข้อมูลได้ดีเพียงใด

### Summary

กระบวนการประเมินประสิทธิภาพของโมเดลแมชชีนเลิร์นนิงที่ทำนายผลลัพธ์ที่เป็นไปได้สองอย่าง

## Key Concepts

- เมทริกซ์ความสับสน (Confusion Matrix)
- การแลกเปลี่ยนระหว่างค่า Precision และ Recall
- เส้นโค้ง ROC
- ค่า F1-Score

## Use Cases

- การคัดกรองโรคทางการแพทย์
- การกรองอีเมลสแปม
- การประเมินความเสี่ยงด้านเครดิต

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (เมทริกซ์ความสับสน)](/en/terms/confusion_matrix-เมทร-กซ-ความส-บสน/)
- [roc_auc (พื้นที่ใต้เส้นโค้ง ROC)](/en/terms/roc_auc-พ-นท-ใต-เส-นโค-ง-roc/)
- [precision_recall (ค่าความแม่นยำและความครอบคลุม)](/en/terms/precision_recall-ค-าความแม-นยำและความครอบคล-ม/)
- [cross_validation (การตรวจสอบข้าม)](/en/terms/cross_validation-การตรวจสอบข-าม/)
