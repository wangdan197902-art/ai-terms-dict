---
title: شجرة الكرات
term_id: ball_tree
category: basic_concepts
subcategory: ''
tags:
- Data Structures
- algorithms
- Machine Learning
difficulty: 4
weight: 1
slug: ball_tree
date: '2026-07-18T15:46:49.821835Z'
lastmod: '2026-07-18T17:15:08.479993Z'
draft: false
source: agnes_llm
status: published
language: ar
description: هيكل بيانات شجري ثنائي يُستخدم لتنظيم النقاط في الفضاء، لتحسين عمليات
  البحث عن أقرب الجيران في مجموعات البيانات عالية الأبعاد.
---
## Definition

تقوم شجرة الكرات بتقسيم نقاط البيانات إلى كرات فائقة متداخلة بدلاً من متوازيات الأضلاع الفائقة. يسمح هذا الهيكل بالقص الفعال أثناء استعلامات أقرب الجيران من خلال حساب المسافات بين الكرات.

### Summary

هيكل بيانات شجري ثنائي يُستخدم لتنظيم النقاط في الفضاء، لتحسين عمليات البحث عن أقرب الجيران في مجموعات البيانات عالية الأبعاد.

## Key Concepts

- تقسيم الكرة الفائقة
- بحث أقرب الجيران
- بيانات عالية الأبعاد
- استعراض الشجرة

## Use Cases

- أقرب الجيران k (KNN)
- تحليل التجميع
- كشف الشذوذ

## Code Example

```python
from sklearn.neighbors import BallTree
import numpy as np
X = np.random.rand(100, 5)
tree = BallTree(X, metric='euclidean')
```

## Related Terms

- [شجرة KD (KD-tree)](/en/terms/شجرة-kd-kd-tree/)
- [أقرب الجيران k (K-Nearest Neighbors)](/en/terms/أقرب-الجيران-k-k-nearest-neighbors/)
- [لعنة الأبعاد (Curse of Dimensionality)](/en/terms/لعنة-الأبعاد-curse-of-dimensionality/)
