---
title: "הערכת מסווגים דו-ערכיים"
term_id: "evaluation_of_binary_classifiers"
category: "basic_concepts"
subcategory: ""
tags: ["metrics", "classification", "evaluation"]
difficulty: 2
weight: 1
slug: "evaluation_of_binary_classifiers"
aliases:
  - /he/terms/evaluation_of_binary_classifiers/
date: "2026-07-18T15:56:31.062692Z"
lastmod: "2026-07-18T17:15:09.538277Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "תהליך הערכת הביצועים של מודלים למידת מכונה החוזים אחד משני תוצרים אפשריים."
---

## Definition

תחום זה כולל ניתוח מדדים כמו דיוק (Accuracy), ריקוד (Precision), שחזור (Recall), ציון F1 ושטח מתחת לעקומת ROC (AUC-ROC). הוא עוזר לקבוע עד כמה המודל מצטיין בהבחנה בין הקטגוריות השונות.

### Summary

תהליך הערכת הביצועים של מודלים למידת מכונה החוזים אחד משני תוצרים אפשריים.

## Key Concepts

- מטריצת בלבול
- פשרה בין ריקוד לשחזור
- עקומת ROC
- ציון F1

## Use Cases

- סריקה לאיתור מחלות רפואיות
- סינון מיילי ספאם
- הערכת סיכון אשראי

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (מטריצת בלבול)](/en/terms/confusion_matrix-מטריצת-בלבול/)
- [roc_auc (שטח מתחת לעקומת ROC)](/en/terms/roc_auc-שטח-מתחת-לעקומת-roc/)
- [precision_recall (ריקוד ושחזור)](/en/terms/precision_recall-ריקוד-ושחזור/)
- [cross_validation (אימות צולב)](/en/terms/cross_validation-אימות-צולב/)
