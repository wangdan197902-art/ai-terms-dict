---
title: "רשת קדימה"
term_id: "feed_forward_network"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "architecture", "fundamentals"]
difficulty: 2
weight: 1
slug: "feed_forward_network"
aliases:
  - /he/terms/feed_forward_network/
date: "2026-07-18T15:57:27.420527Z"
lastmod: "2026-07-18T17:15:09.540619Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "סוג של רשת נוירונים מלאכותית שבה החיבורים בין הצמתים אינם יוצרים מעגלים, והמידע מועבר בכיוון אחד בלבד."
---

## Definition

רשתות קדימה (FFN), הידועות גם כמפרקים רב-שכבתיים (MLP), מעבדות נתונים ברצף דרך שכבות של נוירונים מהקלט לפלט ללא לולאות משוב. כל נוירון מקבל קלטים, מחשב סכום משוקלל שלהם, ומפעיל עליהם פונקציית אקטיבציה לפני העברת הפלט לשכבה הבאה. ארכיטקטורה זו מהווה את הבסיס הרב-תכליתי ביותר לרשתות נוירונים עמוקות.

### Summary

סוג של רשת נוירונים מלאכותית שבה החיבורים בין הצמתים אינם יוצרים מעגלים, והמידע מועבר בכיוון אחד בלבד.

## Key Concepts

- ללא מעגלים
- שכבות (קלט, נסתר, פלט)
- פונקציות אקטיבציה
- סכומים משוקללים

## Use Cases

- משימות רגרסיה פשוטות
- בעיות מיון עם נתונים טבלאיים
- אבני בניין לארכיטקטורות עמוקות יותר

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron (מפרק רב-שכבתי)](/en/terms/multi-layer-perceptron-מפרק-רב-שכבתי/)
- [Backpropagation (הפצת לאחור)](/en/terms/backpropagation-הפצת-לאחור/)
- [Activation Function (פונקציית אקטיבציה)](/en/terms/activation-function-פונקציית-אקטיבציה/)
- [Neural Network (רשת נוירונים)](/en/terms/neural-network-רשת-נוירונים/)
