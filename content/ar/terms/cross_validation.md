---
title: "التحقق المتبادل"
term_id: "cross_validation"
category: "training_techniques"
subcategory: ""
tags: ["evaluation", "machine-learning", "statistics"]
difficulty: 2
weight: 1
slug: "cross_validation"
aliases:
  - /ar/terms/cross_validation/
date: "2026-07-18T15:50:36.050413Z"
lastmod: "2026-07-18T17:15:08.489018Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "إجراء إعادة أخذ العينات المستخدم لتقييم نماذج تعلم الآلة على عينة بيانات محدودة من خلال تقسيم البيانات إلى مجموعات للتدريب والاختبار."
---

## Definition

التحقق المتبادل هو أسلوب إحصائي يُستخدم لتقدير كفاءة نماذج تعلم الآلة. الشكل الأكثر شيوعاً هو التحقق المتبادل ذو الطيات k، حيث يتم تقسيم البيانات إلى k أجزاء متساوية.

### Summary

إجراء إعادة أخذ العينات المستخدم لتقييم نماذج تعلم الآلة على عينة بيانات محدودة من خلال تقسيم البيانات إلى مجموعات للتدريب والاختبار.

## Key Concepts

- التقسيم إلى k طية
- تعميم النموذج
- كشف الإفراط في التخصيص
- تقدير الأداء

## Use Cases

- ضبط المعلمات الفائقة
- مقارنة الخوارزميات المختلفة
- التحقق من استقرار النموذج على مجموعات البيانات الصغيرة

## Code Example

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X, y, cv=5)
```

## Related Terms

- [Train-Test Split (تقسيم التدريب والاختبار)](/en/terms/train-test-split-تقسيم-التدريب-والاختبار/)
- [Leave-One-Out (ترك واحد للخارج)](/en/terms/leave-one-out-ترك-واحد-للخارج/)
- [Bootstrap (الإعادة أخذ العينات)](/en/terms/bootstrap-الإعادة-أخذ-العينات/)
