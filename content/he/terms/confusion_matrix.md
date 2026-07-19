---
title: מטריצת בלבול
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
date: '2026-07-18T15:49:46.501173Z'
lastmod: '2026-07-18T17:15:09.522529Z'
draft: false
source: agnes_llm
status: published
language: he
description: טבלה המשמשת לתיאור ביצועיו של מודל סיווג על קבוצת נתוני בדיקה.
---
## Definition

מטריצת בלבול היא פריסת טבלה ספציפית המאפשרת ויזואליזציה של הביצועים של אלגוריתם, בדרך כלל למידה מפוקחת. היא מציגה את מספרי ההצלחות האמיתיות (True Positives), הכישלונות האמיתיים (True Negatives), ההצלחות השגויות (False Positives) והכישלונות השגויים (False Negatives).

### Summary

טבלה המשמשת לתיאור ביצועיו של מודל סיווג על קבוצת נתוני בדיקה.

## Key Concepts

- הצלחות אמיתיות
- כישלונות שגויים
- דיוק
- שחזור

## Use Cases

- הערכת מתארים דו-סעיפיים
- ניתוח ביצועי סיווג רב-סעיפי
- ניפוי באגים של הטיית מודל בקבוצות נתונים לא מאוזנות

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (דיוק)](/en/terms/precision-דיוק/)
- [recall (שחזור)](/en/terms/recall-שחזור/)
- [F1 score (מדד F1)](/en/terms/f1-score-מדד-f1/)
- [ROC curve (עקומת ROC)](/en/terms/roc-curve-עקומת-roc/)
