---
title: التحقق المتقاطع بإزالة عنصر واحد
term_id: leave_one_out_cross_validation
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- evaluation
- statistics
difficulty: 3
weight: 1
slug: leave_one_out_cross_validation
date: '2026-07-18T16:05:49.915133Z'
lastmod: '2026-07-18T17:15:08.522171Z'
draft: false
source: agnes_llm
status: published
language: ar
description: تقنية إعادة أخذ عينات دقيقة يتم فيها تدريب النموذج على جميع العينات باستثناء
  عينة واحدة واختباره على تلك العينة المحتجزة، وتُكرر العملية لكل نقطة بيانات.
---
## Definition

التحقق المتقاطع بإزالة عنصر واحد (LOOCV) هو حالة خاصة من التحقق المتقاطع متعدد الطيات حيث يساوي عدد الطيات (k) عدد العينات في مجموعة البيانات. يوفر تقديراً شبه غير متحيز لأداء النموذج.

### Summary

تقنية إعادة أخذ عينات دقيقة يتم فيها تدريب النموذج على جميع العينات باستثناء عينة واحدة واختباره على تلك العينة المحتجزة، وتُكرر العملية لكل نقطة بيانات.

## Key Concepts

- إعادة أخذ العينات
- تقييم النموذج
- مفاضلة الانحياز والتباين
- التكلفة الحسابية

## Use Cases

- تقييم النماذج على مجموعات بيانات طبية صغيرة
- ضبط المعاملات الفائقة عندما تكون البيانات شحيحة
- مقارنة أداء الخوارزميات بدقة

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (التحقق المتقاطع متعدد الطيات)](/en/terms/k-fold-cross-validation-التحقق-المتقاطع-متعدد-الطيات/)
- [train_test_split (تقسيم التدريب والاختبار)](/en/terms/train_test_split-تقسيم-التدريب-والاختبار/)
- [bootstrap (أخذ العينات الاستبدالية)](/en/terms/bootstrap-أخذ-العينات-الاستبدالية/)
- [cross_validation_score (درجة التحقق المتقاطع)](/en/terms/cross_validation_score-درجة-التحقق-المتقاطع/)
