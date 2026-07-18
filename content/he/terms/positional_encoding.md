---
title: "קידוד מיקומי"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /he/terms/positional_encoding/
date: "2026-07-18T15:37:58.967353Z"
lastmod: "2026-07-18T17:15:09.502660Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "טכניקה המחדירה מידע על המיקום היחסי או המוחלט של אסימונים ברצף לתוך מודלי טרנספורמר."
---

## Definition

מכיוון שטרנספורמרים מעבדים את כל האסימונים במקביל ולא ברצף כמו ב-RNNs, חסר להם ידע מובנה בסדר האסימונים. קידוד מיקומי מוסיף וקטורים ספציפיים להטמעות הקלט כדי לספק מידע זה.

### Summary

טכניקה המחדירה מידע על המיקום היחסי או המוחלט של אסימונים ברצף לתוך מודלי טרנספורמר.

## Key Concepts

- סדר רצפי
- התעניינות עצמית
- פונקציות סינוסואידליות
- הטמעת אסימונים

## Use Cases

- תרגום מכונה
- סיכום טקסט
- מודלי שפה

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Transformer Architecture (ארכיטקטורת טרנספורמר)](/en/terms/transformer-architecture-ארכיטקטורת-טרנספורמר/)
- [Embedding (הטמעה)](/en/terms/embedding-הטמעה/)
- [Attention Mechanism (מנגנון התעניינות)](/en/terms/attention-mechanism-מנגנון-התעניינות/)
- [RoPE (קידוד מיקומי רוטציה)](/en/terms/rope-קידוד-מיקומי-רוטציה/)
