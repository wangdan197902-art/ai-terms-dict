---
title: "إشرافي"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
date: "2026-07-18T15:31:06.804934Z"
lastmod: "2026-07-18T17:15:08.449669Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "نموذج تعلم آلي يتم فيه تدريب النماذج على أزواج الإدخال والإخراج المصنفة."
---
## Definition

يتضمن التعلم تحت الإشراف تغذية الخوارزمية ببيانات تحتوي على كل من المدخلات والإجابات الصحيحة (التسميات). يتعلم النموذج تعيين المدخلات للمخرجات عن طريق تقليل أخطاء التنبؤ.

### Summary

نموذج تعلم آلي يتم فيه تدريب النماذج على أزواج الإدخال والإخراج المصنفة.

## Key Concepts

- البيانات المصنفة
- التعيين
- تقليل الخسارة

## Use Cases

- تصنيف الصور
- كشف البريد العشوائي
- توقع الأسعار

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [غير إشرافي (Unsupervised)](/en/terms/غير-إشرافي-unsupervised/)
- [تسمية (Label)](/en/terms/تسمية-label/)
- [انحدار (Regression)](/en/terms/انحدار-regression/)
