---
title: مصفوفة الارتباك
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
date: '2026-07-18T15:49:44.272603Z'
lastmod: '2026-07-18T17:15:08.487142Z'
draft: false
source: agnes_llm
status: published
language: ar
description: جدول يُستخدم لوصف أداء نموذج التصنيف على مجموعة من بيانات الاختبار.
---
## Definition

مصفوفة الارتباك هي تخطيط جدولي محدد يسمح بتصور أداء الخوارزمية، وغالباً ما تكون خوارزمية تعلم تحت إشراف. وتُظهر أعداد الحالات الإيجابية الحقيقية، والسلبية الحقيقية، والإيجابية الكاذبة، والسلبية الكاذبة.

### Summary

جدول يُستخدم لوصف أداء نموذج التصنيف على مجموعة من بيانات الاختبار.

## Key Concepts

- الإيجابيات الحقيقية
- السلبيات الكاذبة
- الدقة
- الاستدعاء

## Use Cases

- تقييم المصنفات الثنائية
- تحليل أداء التصنيف متعدد الفئات
- تصحيح تحيز النموذج في مجموعات البيانات غير المتوازنة

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (الدقة)](/en/terms/precision-الدقة/)
- [recall (الاستدعاء)](/en/terms/recall-الاستدعاء/)
- [F1 score (مقياس F1)](/en/terms/f1-score-مقياس-f1/)
- [ROC curve (منحنى ROC)](/en/terms/roc-curve-منحنى-roc/)
