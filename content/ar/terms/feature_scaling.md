---
title: "قياس الميزات"
term_id: "feature_scaling"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "statistics", "optimization"]
difficulty: 2
weight: 1
slug: "feature_scaling"
aliases:
  - /ar/terms/feature_scaling/
date: "2026-07-18T15:57:51.470896Z"
lastmod: "2026-07-18T17:15:08.504217Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "عملية تطبيع نطاق المتغيرات المستقلة أو ميزات البيانات لضمان التجانس في المقدار."
---

## Definition

يقوم قياس الميزات بتوحيد نطاق المتغيرات المدخلة لمنع الميزات ذات المقادير الأكبر من هيمنة عملية التعلم. تشمل الطرق الشائعة التطبيع (قياس الحد الأدنى والحد الأقصى) والتوحيد القياسي (تحويل القيم لتصبح ذات متوسط صفر وانحراف معياري واحد)، مما يسرع تقارب خوارزميات التحسين.

### Summary

عملية تطبيع نطاق المتغيرات المستقلة أو ميزات البيانات لضمان التجانس في المقدار.

## Key Concepts

- التطبيع
- التوحيد القياسي
- نزول التدرج
- معالجة البيانات الأولية

## Use Cases

- تدريب الشبكات العصبية
- التجميع باستخدام خوارزمية K-means
- آلات ناقلات الدعم (SVM)

## Code Example

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
```

## Related Terms

- [Min-Max Scaling (قياس الحد الأدنى والحد الأقصى)](/en/terms/min-max-scaling-قياس-الحد-الأدنى-والحد-الأقصى/)
- [Z-score Normalization (تطبيع درجة Z)](/en/terms/z-score-normalization-تطبيع-درجة-z/)
- [Data preprocessing (معالجة البيانات الأولية)](/en/terms/data-preprocessing-معالجة-البيانات-الأولية/)
- [Gradient Descent (نزول التدرج)](/en/terms/gradient-descent-نزول-التدرج/)
