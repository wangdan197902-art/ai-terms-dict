---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /he/terms/relu/
date: "2026-07-18T15:38:14.644732Z"
lastmod: "2026-07-18T17:15:09.503608Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "יחידה ליניארית מתוקנת (Rectified Linear Unit) היא פונקציית הפעלה המפיקה את הקלט ישירות אם הוא חיובי, ואחרת מפיקה אפס."
---

## Definition

ReLU נפוץ מאוד ברשתות נוירונים ללמידה עמוקה בשל יעילותו החישובית והיכולת שלו להפחית את בעיית דעיכת הגרדיאנט. מוגדר מתמטית כ-f(x) = max(0, x), הוא מציג אי-ליניאריות פשוטה ויעילה.

### Summary

יחידה ליניארית מתוקנת (Rectified Linear Unit) היא פונקציית הפעלה המפיקה את הקלט ישירות אם הוא חיובי, ואחרת מפיקה אפס.

## Key Concepts

- אי-ליניאריות
- פונקציית הפעלה
- דעיכת גרדיאנט
- ליניאריות מקוטעת

## Use Cases

- שכבות נסתרות ברשתות קונבולוציוניות (CNNs)
- רשתות הזנה קדימה עמוקות
- מודלים לזיהוי תמונות

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (פונקציית סיגמואיד)](/en/terms/sigmoid-פונקציית-סיגמואיד/)
- [Tanh (פונקציית טנגנס היפרבולי)](/en/terms/tanh-פונקציית-טנגנס-היפרבולי/)
- [Leaky ReLU (גרסה משופרת של ReAct)](/en/terms/leaky-relu-גרסה-משופרת-של-react/)
- [Neural Network (רשת נוירונים)](/en/terms/neural-network-רשת-נוירונים/)
