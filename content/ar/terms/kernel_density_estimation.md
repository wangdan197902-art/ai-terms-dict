---
title: تقدير كثافة النواة
term_id: kernel_density_estimation
category: basic_concepts
subcategory: ''
tags:
- statistics
- probability
- Data Analysis
difficulty: 3
weight: 1
slug: kernel_density_estimation
date: '2026-07-18T16:04:14.065593Z'
lastmod: '2026-07-18T17:15:08.518384Z'
draft: false
source: agnes_llm
status: published
language: ar
description: طريقة لا معلمية تُستخدم لتقدير دالة الكثافة الاحتمالية لمتغير عشوائي
  بناءً على عينة بيانات محدودة.
---
## Definition

تقدير كثافة النواة (KDE) هو تقنية إحصائية أساسية تقوم بتنعيم نقاط البيانات المنفصلة لإنشاء منحنى توزيع احتمالي مستمر. تضع دالة نواة، عادةً ما تكون غاوسية...

### Summary

طريقة لا معلمية تُستخدم لتقدير دالة الكثافة الاحتمالية لمتغير عشوائي بناءً على عينة بيانات محدودة.

## Key Concepts

- دالة الكثافة الاحتمالية
- الإحصاء غير المعلمي
- التنعيم
- نواة غاوسية

## Use Cases

- تحليل البيانات الاستكشافي (EDA)
- كشف الشذوذ في البيانات أحادية المتغير
- تصور توزيعات الميزات في مجموعات البيانات

## Code Example

```python
from scipy.stats import gaussian_kde
import numpy as np

data = np.random.normal(0, 1, 100)
kde = gaussian_kde(data)
x_vals = np.linspace(-3, 3, 100)
y_vals = kde(x_vals)
```

## Related Terms

- [Histogram (مدرج تكراري)](/en/terms/histogram-مدرج-تكراري/)
- [Parzen Window (نافذة بارزين)](/en/terms/parzen-window-نافذة-بارزين/)
- [Bandwidth Selection (اختيار عرض النطاق الترددي)](/en/terms/bandwidth-selection-اختيار-عرض-النطاق-الترددي/)
- [Scipy Stats (مكتبة الإحصاءات في بايثون Scipy)](/en/terms/scipy-stats-مكتبة-الإحصاءات-في-بايثون-scipy/)
