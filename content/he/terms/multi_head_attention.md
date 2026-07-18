---
title: "תשומת ראשים מרובה"
term_id: "multi_head_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformer", "nlp", "deep_learning"]
difficulty: 4
weight: 1
slug: "multi_head_attention"
aliases:
  - /he/terms/multi_head_attention/
date: "2026-07-18T15:27:30.401381Z"
lastmod: "2026-07-18T17:15:09.482901Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "מנגנון במודלי טרנספורמר המאפשר למודל להתמקד במידע ממרחבי ייצוג שונים בו-זמנית."
---

## Definition

תשומת ראשים מרובה מרחיבה את מנגנון התשומה הסטנדרטי על ידי הרצאה שלו מספר פעמים במקביל עם הטלות ליניאריות נלמדות שונות. הדבר מאפשר למודל להתמקד יחדיו במידע ממקורות שונים.

### Summary

מנגנון במודלי טרנספורמר המאפשר למודל להתמקד במידע ממרחבי ייצוג שונים בו-זמנית.

## Key Concepts

- תשומה עצמית
- הטלות ליניאריות
- הדבקה (Concatenation)

## Use Cases

- עיבוד שפה טבעית (NLP)
- תרגום מכונה
- סיווג תמונות באמצעות Vision Transformers

## Code Example

```python
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        # Simplified forward pass logic
        pass
```

## Related Terms

- [Scaled Dot-Product Attention (תשומת מכפלה נקודתית מותאמת)](/en/terms/scaled-dot-product-attention-תשומת-מכפלה-נקודתית-מותאמת/)
- [Transformer (טרנספורמר)](/en/terms/transformer-טרנספורמר/)
- [Embedding (טמעת מילים/אובייקטים)](/en/terms/embedding-טמעת-מילים-אובייקטים/)
