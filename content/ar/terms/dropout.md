---
title: "الإسقاط (Dropout)"
term_id: "dropout"
category: "basic_concepts"
subcategory: ""
tags: ["Deep Learning", "Regularization", "Model Training"]
difficulty: 3
weight: 1
slug: "dropout"
aliases:
  - /ar/terms/dropout/
date: "2026-07-18T15:36:46.347153Z"
lastmod: "2026-07-18T17:15:08.460576Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "الإسقاط هو تقنية تنظيم عشوائية تتجاهل عشوائياً بعض الخلايا العصبية أثناء التدريب لمنع الإفراط في التخصيص."
---

## Definition

في الشبكات العصبية، يمنع الإسقاط الإفراط في التخصيص عن طريق إزالة مجموعة عشوائية مؤقتة من الخلايا العصبية خلال كل خطوة تدريب. هذا يجبر الشبكة على تعلم ميزات قوية تكون مفيدة في سياقات متنوعة.

### Summary

الإسقاط هو تقنية تنظيم عشوائية تتجاهل عشوائياً بعض الخلايا العصبية أثناء التدريب لمنع الإفراط في التخصيص.

## Key Concepts

- التنظيم (Regularization)
- منع الإفراط في التخصيص (Overfitting Prevention)
- الشبكات العصبية (Neural Networks)
- الكبت العشوائي (Random Suppression)

## Use Cases

- تدريب الشبكات العصبية العميقة ذات التغذية الأمامية
- تحسين التعميم في نماذج اللغات الكبيرة
- تقليل الاعتماد الحسابي على مسارات خلايا عصبية محددة

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(100, 50),
    nn.Dropout(0.5),
    nn.ReLU(),
    nn.Linear(50, 10)
)
```

## Related Terms

- [تنظيم L2 (L2 Regularization)](/en/terms/تنظيم-l2-l2-regularization/)
- [التطبيع الدفعي (Batch Normalization)](/en/terms/التطبيع-الدفعي-batch-normalization/)
- [الإفراط في التخصيص (Overfitting)](/en/terms/الإفراط-في-التخصيص-overfitting/)
- [التعميم (Generalization)](/en/terms/التعميم-generalization/)
