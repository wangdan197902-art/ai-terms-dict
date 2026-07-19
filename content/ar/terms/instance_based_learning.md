---
title: التعلم القائم على العينات
term_id: instance_based_learning
category: training_techniques
subcategory: ''
tags:
- algorithm
- Lazy Learning
- Classification
difficulty: 2
weight: 1
slug: instance_based_learning
date: '2026-07-18T16:03:21.808705Z'
lastmod: '2026-07-18T17:15:08.516551Z'
draft: false
source: agnes_llm
status: published
language: ar
description: نهج تعلم كسول حيث تتم عمليات التنبؤ بمقارنة المدخلات الجديدة بالعينات
  التدريبية المخزنة.
---
## Definition

يُعرف أيضاً بالتعلم القائم على الذاكرة، لا تبني هذه التقنية نموذجاً عاماً أثناء التدريب. بدلاً من ذلك، تخزن مجموعة البيانات التدريبية بأكملها. عند الحاجة للتنبؤ، تبحث عن أكثر العينات...

### Summary

نهج تعلم كسول حيث تتم عمليات التنبؤ بمقارنة المدخلات الجديدة بالعينات التدريبية المخزنة.

## Key Concepts

- التعلم الكسول
- مقياس التشابه
- أقرب الجيران (K-Nearest Neighbors)
- قائم على الذاكرة

## Use Cases

- أنظمة التوصية
- التعرف على الأنماط
- مجموعات البيانات الصغيرة والمتوسطة

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```

## Related Terms

- [KNN (خوارزمية أقرب الجيران)](/en/terms/knn-خوارزمية-أقرب-الجيران/)
- [Similarity search (بحث التشابه)](/en/terms/similarity-search-بحث-التشابه/)
- [Lazy learning (التعلم الكسول)](/en/terms/lazy-learning-التعلم-الكسول/)
- [Kernel methods (طرق النواة)](/en/terms/kernel-methods-طرق-النواة/)
