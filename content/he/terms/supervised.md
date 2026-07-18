---
title: "מפוקח"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
aliases:
  - /he/terms/supervised/
date: "2026-07-18T15:30:49.302306Z"
lastmod: "2026-07-18T17:15:09.488420Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "פרדיגמה בלמידת מכונה שבה מודלים מאומנים על זוגות קלט-פלט מסומנים."
---

## Definition

למידה מפוקחת כרוכה בהזנת אלגוריתם עם נתונים הכוללים גם קלטים וגם תשובות נכונות (תוויות). המודל לומד למפות קלטים לפלטים על ידי מזעור שגיאות חיזוי.

### Summary

פרדיגמה בלמידת מכונה שבה מודלים מאומנים על זוגות קלט-פלט מסומנים.

## Key Concepts

- נתונים מסומנים
- מיפוי
- מזעור אובדן

## Use Cases

- מיון תמונות
- זיהוי דואר זבל
- חיזוי מחירים

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (ללא פיקוח)](/en/terms/unsupervised-ללא-פיקוח/)
- [Label (תווית)](/en/terms/label-תווית/)
- [Regression (ריגורסיה/התאמת עקומה)](/en/terms/regression-ריגורסיה-התאמת-עקומה/)
