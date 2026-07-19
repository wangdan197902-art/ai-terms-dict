---
title: צפוף
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:53:44.629209Z'
lastmod: '2026-07-18T17:15:09.532479Z'
draft: false
source: agnes_llm
status: published
language: he
description: שכבה או טנזור שבהם כל אלמנט מחובר לכל אלמנט בשכבה הקודמת או בממד.
---
## Definition

ברשתות עצביות, המונח 'צפוף' מתייחס לשכבות מקומות לחלוטין (Fully Connected), שבהן כל נוירון מקבל קלט מכל הנוירונים בשכבה שקדמה לו. זה מנוגד לחיבורים דלילים הנמצאים ברשתות קונבולוציוניות או אחרות.

### Summary

שכבה או טנזור שבהם כל אלמנט מחובר לכל אלמנט בשכבה הקודמת או בממד.

## Key Concepts

- מקומויות מלאה
- מטריצת משקולות
- פונקציית הפעלה
- שילוב תכונות

## Use Cases

- שכבות סיווג סופיות ב-MLPs
- מיזוג תכונות במודלים היברידיים
- משימות רגרסיה פשוטות

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (רשת עצבית קדימית)](/en/terms/feedforward-neural-network-רשת-עצבית-קדימית/)
- [Backpropagation (הפצת אחורה)](/en/terms/backpropagation-הפצת-אחורה/)
- [ReLU (פונקציית פעלה ליניארית חלקית)](/en/terms/relu-פונקציית-פעלה-ליניארית-חלקית/)
- [Bias Term (איבר הסטייה)](/en/terms/bias-term-איבר-הסטייה/)
