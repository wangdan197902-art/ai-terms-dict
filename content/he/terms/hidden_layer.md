---
title: "שכבה נסתרת"
term_id: "hidden_layer"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture", "deep_learning"]
difficulty: 3
weight: 1
slug: "hidden_layer"
aliases:
  - /he/terms/hidden_layer/
date: "2026-07-18T16:03:56.591327Z"
lastmod: "2026-07-18T17:15:09.547175Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "שכבה ביניים ברשת נוירונים בין שכבות הקלט והפלט המעבדת תכונות."
---

## Definition

שכבה נסתרת מורכבת מנוירונים המקבלים קלטים משכבות קודמות, מיישמים משקולות והטיות, ומעבירים נתונים מעובדים קדימה דרך פונקציית הפעלה. שכבות אלו מאפשרות לרשתות נוירונים

### Summary

שכבה ביניים ברשת נוירונים בין שכבות הקלט והפלט המעבדת תכונות.

## Key Concepts

- רשתות נוירונים
- חילוץ תכונות
- פונקציות הפעלה
- למידה עמוקה

## Use Cases

- מערכות זיהוי תמונות
- מודלי עיבוד שפה טבעית
- ניתוי חיזוי

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron (נוירון)](/en/terms/neuron-נוירון/)
- [backpropagation (הפצה אחורית)](/en/terms/backpropagation-הפצה-אחורית/)
- [activation_function (פונקציית הפעלה)](/en/terms/activation_function-פונקציית-הפעלה/)
- [deep_learning (למידה עמוקה)](/en/terms/deep_learning-למידה-עמוקה/)
