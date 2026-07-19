---
title: אימות צולב
term_id: cross_validation
category: training_techniques
subcategory: ''
tags:
- evaluation
- Machine Learning
- statistics
difficulty: 2
weight: 1
slug: cross_validation
date: '2026-07-18T15:50:45.947744Z'
lastmod: '2026-07-18T17:15:09.524561Z'
draft: false
source: agnes_llm
status: published
language: he
description: הליך דגימה חוזרת המשמש להערכת מודלים למידת מכונה על דגימת נתונים מוגבלת,
  תוך חלוקת הנתונים לתת-קבוצות לאימון ובדיקה.
---
## Definition

אימות צולב הוא שיטה סטטיסטית המשמשת להערכת יכולתם של מודלי למידת מכונה. הצורה הנפוצה ביותר היא אימות צולב בקפלים (k-fold), שבו הנתונים מחולקים ל-k חלקים שווים. המודל מאומן על k-1 קפלים ומבוצע על הקפל הנותר, בתהליך החוזר על עצמו עבור כל קפל.

### Summary

הליך דגימה חוזרת המשמש להערכת מודלים למידת מכונה על דגימת נתונים מוגבלת, תוך חלוקת הנתונים לתת-קבוצות לאימון ובדיקה.

## Key Concepts

- חלוקה לקפלים (K-Fold Split)
- כלליות המודל
- זיהוי התאמה יתר (Overfitting)
- הערכת ביצועים

## Use Cases

- כוונון היפר-פרמטרים
- השוואה בין אלגוריתמים שונים
- אימות יציבות המודל על מערכי נתונים קטנים

## Code Example

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X, y, cv=5)
```

## Related Terms

- [Train-Test Split (פילול אימון-בדיקה)](/en/terms/train-test-split-פילול-אימון-בדיקה/)
- [Leave-One-Out (השאר אחד בחוץ)](/en/terms/leave-one-out-השאר-אחד-בחוץ/)
- [Bootstrap (דגימת בוטסטראפ)](/en/terms/bootstrap-דגימת-בוטסטראפ/)
