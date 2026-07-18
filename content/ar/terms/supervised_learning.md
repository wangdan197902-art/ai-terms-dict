---
title: "التعلم الخاضع للإشراف"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /ar/terms/supervised_learning/
date: "2026-07-18T15:38:49.559243Z"
lastmod: "2026-07-18T17:15:08.467082Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "نموذج تعلم آلي يتعلم فيه النموذج تعيين المدخلات إلى المخرجات بناءً على أمثلة تدريبية موسومة."
---

## Definition

في التعلم الخاضع للإشراف، يتم تدريب الخوارزمية على مجموعة بيانات موسومة، مما يعني أن كل مثال إدخال مقترن بالإخراج الصحيح. الهدف هو أن يتعلم النموذج العلاقة الكامنة بين المدخلات والمخرجات.

### Summary

نموذج تعلم آلي يتعلم فيه النموذج تعيين المدخلات إلى المخرجات بناءً على أمثلة تدريبية موسومة.

## Key Concepts

- البيانات الموسومة
- تعيين المدخلات والمخرجات
- التصنيف
- الانحدار

## Use Cases

- كشف البريد العشوائي
- توقع أسعار المنازل
- التعرف على الصور

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (التعلم غير الخاضع للإشراف)](/en/terms/unsupervised-learning-التعلم-غير-الخاضع-للإشراف/)
- [Training Set (مجموعة التدريب)](/en/terms/training-set-مجموعة-التدريب/)
- [Validation Set (مجموعة التحقق)](/en/terms/validation-set-مجموعة-التحقق/)
- [Model Accuracy (دقة النموذج)](/en/terms/model-accuracy-دقة-النموذج/)
