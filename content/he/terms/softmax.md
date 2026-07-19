---
title: סופטמקס
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T15:38:47.796155Z'
lastmod: '2026-07-18T17:15:09.504546Z'
draft: false
source: agnes_llm
status: published
language: he
description: פונקציה מתמטית הממירה וקטור של ציונים ממשיים שרירותיים להתפלגות הסתברותית.
---
## Definition

סופטמקס נפוץ מאוד בשכבה החיצונית של רשתות נוירונים למשימות מיון רב-מחלקתי. הפונקציה לוקחת וקטור של לוגיטים גולמיים ומנרמלת אותם כך שכל איבר מייצג הסתברות.

### Summary

פונקציה מתמטית הממירה וקטור של ציונים ממשיים שרירותיים להתפלגות הסתברותית.

## Key Concepts

- התפלגות הסתברותית
- לוגיטים
- נרמול
- מיון רב-מחלקתי

## Use Cases

- שכבות פלט במיון תמונות
- חיזוי אסימונים במודלי שפה
- סיווג רב-תוויתי

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (מקסימום ארגומנט)](/en/terms/argmax-מקסימום-ארגומנט/)
- [Cross-Entropy Loss (פונקציית הפסד קרוס-אנטרופיה)](/en/terms/cross-entropy-loss-פונקציית-הפסד-קרוס-אנטרופיה/)
- [Logits (לוגיטים/ציונים גולמיים)](/en/terms/logits-לוגיטים-ציונים-גולמיים/)
- [Neural Network (רשת נוירונים)](/en/terms/neural-network-רשת-נוירונים/)
