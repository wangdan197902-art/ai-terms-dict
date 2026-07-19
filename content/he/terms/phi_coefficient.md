---
title: מקדם פאי
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
date: '2026-07-18T16:17:22.515408Z'
lastmod: '2026-07-18T17:15:09.573820Z'
draft: false
source: agnes_llm
status: published
language: he
description: מדד סטטיסטי למדידת הקשר בין שני משתנים בינאריים.
---
## Definition

מקדם פאי (φ) הוא מדד לקשר בין שני משתנים בינאריים, המשמש כמקדם המתאם של פיירסון למשתנים דו-קוטביים. ערכו נע בין -1 ל-1, כאשר 0 מצביע על היעדר קשר.

### Summary

מדד סטטיסטי למדידת הקשר בין שני משתנים בינאריים.

## Key Concepts

- משתנים בינאריים
- מתאם
- טבלת תדירויות
- חוזק הקשר

## Use Cases

- הערכת ביצועים של מסווג בינארי מעבר לדיוק
- ניתוח קשרים בנתוני סקר עם תשובות כן/לא
- בחירת מאפיינים בערכות נתונים עם קלט קטגוריאלי

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

- [Cramer's V (מדד קרמר V)](/en/terms/cramer-s-v-מדד-קרמר-v/)
- [Pearson correlation (מתאם פיירסון)](/en/terms/pearson-correlation-מתאם-פיירסון/)
- [Confusion matrix (מטריצת בלבול)](/en/terms/confusion-matrix-מטריצת-בלבול/)
- [Mutual information (מידע הדדי)](/en/terms/mutual-information-מידע-הדדי/)
