---
title: معامل فاي
term_id: phi_coefficient
category: basic_concepts
subcategory: ''
tags:
- statistics
- Evaluation Metrics
- Binary Classification
difficulty: 3
weight: 1
slug: phi_coefficient
date: '2026-07-18T16:16:32.312116Z'
lastmod: '2026-07-18T17:15:08.537123Z'
draft: false
source: agnes_llm
status: published
language: ar
description: مقياس إحصائي لمدى الارتباط بين متغيرين ثنائيي القيمة.
---
## Definition

معامل فاي (φ) هو مقياس للارتباط بين متغيرين ثنائيي القيمة، ويعمل كمعامل ارتباط بيرسون للمتغيرات الثنائية (الثنائية). يتراوح قيمته من -1 إلى +1، حيث يشير الصفر إلى عدم وجود ارتباط، بينما تشير القيم القصوى إلى ارتباط كامل.

### Summary

مقياس إحصائي لمدى الارتباط بين متغيرين ثنائيي القيمة.

## Key Concepts

- المتغيرات الثنائية
- الارتباط
- جدول التكرار المشترك
- قوة الارتباط

## Use Cases

- تقييم أداء المصنفات الثنائية بما يتجاوز دقة التصنيف
- تحليل العلاقات في بيانات الاستبيانات ذات الإجابات بنعم/لا
- اختيار الميزات في مجموعات البيانات ذات المدخلات الفئوية

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [Cramer's V (معامل كرامر في)](/en/terms/cramer-s-v-معامل-كرامر-في/)
- [Pearson correlation (معامل ارتباط بيرسون)](/en/terms/pearson-correlation-معامل-ارتباط-بيرسون/)
- [Confusion matrix (مصفوفة الارتباك)](/en/terms/confusion-matrix-مصفوفة-الارتباك/)
- [Mutual information (المعلومات المتبادلة)](/en/terms/mutual-information-المعلومات-المتبادلة/)
