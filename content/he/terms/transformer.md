---
title: טרנספורמר
term_id: transformer
category: basic_concepts
subcategory: ''
tags:
- architecture
- NLP
- attention
difficulty: 4
weight: 1
slug: transformer
date: '2026-07-18T15:31:37.468711Z'
lastmod: '2026-07-18T17:15:09.489969Z'
draft: false
source: agnes_llm
status: published
language: he
description: ארכיטקטורה של למידה עמוקה המבוססת על מנגנוני קשב עצמי (Self-Attention)
  ומעבדת נתונים רציפים במקביל ולא ברצף.
---
## Definition

הארכיטקטורה הטרנספורמר, שהוצגה במאמר 'Attention Is All You Need', שינתה פנים בתחום העיבוד השפה הטבעית ומעבר לו. היא משתמשת בקשב עצמי רב-ראשי כדי לתת משקל חשיבות שונה לחלקים שונים בקלט, מה שמאפשר הבנה עמוקה של הקשר.

### Summary

ארכיטקטורה של למידה עמוקה המבוססת על מנגנוני קשב עצמי (Self-Attention) ומעבדת נתונים רציפים במקביל ולא ברצף.

## Key Concepts

- קשב עצמי
- קשב רב-ראשי
- קידוד מיקום
- מבנה מקדם-מפענח

## Use Cases

- תרגום מכונה
- יצירת טקסט
- זיהוי תמונות (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (מנגנון קשב)](/en/terms/attention_mechanism-מנגנון-קשב/)
- [bert (מודל שפה)](/en/terms/bert-מודל-שפה/)
- [gpt (מודל שפה)](/en/terms/gpt-מודל-שפה/)
- [self_attention (קשב עצמי)](/en/terms/self_attention-קשב-עצמי/)
