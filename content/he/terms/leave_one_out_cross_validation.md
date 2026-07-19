---
title: אימות צולב של השארת אחד בחוץ
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
date: '2026-07-18T16:09:54.497497Z'
lastmod: '2026-07-18T17:15:09.557801Z'
draft: false
source: agnes_llm
status: published
language: he
description: טכניקת דגימה חוזרת קפדנית שבה המודל מאומן על כל הדגמים למעט אחד, ומבוצע
  בדיקה על אותו דגם בודד שהושאר בחוץ, בתהליך החוזר עבור כל נקודת נתונים.
---
## Definition

אימות צולב של השארת אחד בחוץ (LOOCV) הוא מקרה פרטי של אימות צולב בקפלים (k-fold), כאשר מספר הקפלים (k) שווה למספר הדגמים במערך הנתונים. שיטה זו מספקת הערכה כמעט ללא הטיה של ביצועי המודל.

### Summary

טכניקת דגימה חוזרת קפדנית שבה המודל מאומן על כל הדגמים למעט אחד, ומבוצע בדיקה על אותו דגם בודד שהושאר בחוץ, בתהליך החוזר עבור כל נקודת נתונים.

## Key Concepts

- דגימה חוזרת
- הערכת מודל
- פשרת סטייה-שונות
- עלות חישובית

## Use Cases

- הערכת מודלים על מערכי נתונים רפואיים קטנים
- כוונון היפר-פרמטרים כאשר הנתונים מועטים
- השוואה קפדנית של ביצועי אלגוריתמים

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

- [k-fold cross-validation (אימות צולב בקפלים)](/en/terms/k-fold-cross-validation-אימות-צולב-בקפלים/)
- [train_test_split (חלוקת נתוני אימון ובדיקה)](/en/terms/train_test_split-חלוקת-נתוני-אימון-ובדיקה/)
- [bootstrap (בוטסטראפ/דגימת משנה)](/en/terms/bootstrap-בוטסטראפ-דגימת-משנה/)
- [cross_validation_score (ציון אימות צולב)](/en/terms/cross_validation_score-ציון-אימות-צולב/)
