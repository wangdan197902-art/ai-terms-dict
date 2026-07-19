---
title: למידה פיקוחית
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T15:38:47.796222Z'
lastmod: '2026-07-18T17:15:09.504892Z'
draft: false
source: agnes_llm
status: published
language: he
description: פרדיגמה בלמידת מכונה שבה מודל לומד למפות קלטים לפלטטים בהתבסס על דוגמאות
  אימון מסומנות.
---
## Definition

בלמידה פיקוחית, האלגוריתם מאומן על ערכת נתונים מסומנת, כלומר כל דוגמת קלט מזווגת עם הפלט הנכון. המטרה היא שהמודל ילמד את הקשר הבסיסי בין הקלט לפלט.

### Summary

פרדיגמה בלמידת מכונה שבה מודל לומד למפות קלטים לפלטטים בהתבסס על דוגמאות אימון מסומנות.

## Key Concepts

- נתונים מסומנים
- מיפוי קלט-פלט
- מיון
- ריגרסיה

## Use Cases

- זיהוי דואר זבל
- ניבוי מחירי דיור
- זיהוי תמונות

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (למידה ללא פיקוח)](/en/terms/unsupervised-learning-למידה-ללא-פיקוח/)
- [Training Set (ערכת אימון)](/en/terms/training-set-ערכת-אימון/)
- [Validation Set (ערכת אימות)](/en/terms/validation-set-ערכת-אימות/)
- [Model Accuracy (דיוק המודל)](/en/terms/model-accuracy-דיוק-המודל/)
