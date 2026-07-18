---
title: "נרמול אצווה"
term_id: "batch_normalization"
category: "basic_concepts"
subcategory: ""
tags: ["deep-learning", "optimization", "neural-networks"]
difficulty: 3
weight: 1
slug: "batch_normalization"
aliases:
  - /he/terms/batch_normalization/
date: "2026-07-18T15:45:52.895238Z"
lastmod: "2026-07-18T17:15:09.516085Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "נרמול אצווה הוא טכניקה המנרמלת את קלטים של שכבה לאורך מיני-אצווה (mini-batch) כדי ליצב ולהאיץ את אימון הרשת העצבית."
---

## Definition

שיטה זו מתאימה ומנרמלת את הפעלות הרשת כך שיהיו בעלות תוחלת אפס ושונות אחת בתוך כל מיני-אצווה במהלך האימון. היא מפחיתה את ההעתקה הקו-וריאנטית הפנימית, ומאפשרת קצבי למידה גבוהים יותר ואימון מהיר יותר.

### Summary

נרמול אצווה הוא טכניקה המנרמלת את קלטים של שכבה לאורך מיני-אצווה (mini-batch) כדי ליצב ולהאיץ את אימון הרשת העצבית.

## Key Concepts

- העתקה קו-וריאנטית פנימית
- סטטיסטיקות מיני-אצווה
- ייצוב גרדיאנטים
- אפקט רגולריזציה

## Use Cases

- רשתות עצביות עמוקות
- רשתות עצביות קונבולוציוניות (CNN)
- אופטימיזציה של אימון

## Code Example

```python
import torch.nn as nn
layer = nn.Sequential(
    nn.Linear(10, 20),
    nn.BatchNorm1d(20),
    nn.ReLU()
)
```

## Related Terms

- [Layer Normalization (נרמול שכבה)](/en/terms/layer-normalization-נרמול-שכבה/)
- [Gradient Descent (ירידת גרדיאנט)](/en/terms/gradient-descent-ירידת-גרדיאנט/)
- [Overfitting (התאמת יתר)](/en/terms/overfitting-התאמת-יתר/)
