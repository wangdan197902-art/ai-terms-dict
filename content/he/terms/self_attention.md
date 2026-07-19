---
title: "תשומת לב עצמית"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:30:34.569324Z"
lastmod: "2026-07-18T17:15:09.487589Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "מנגנון המאפשר לרשת נוירונים לשקול את חשיבותם של חלקים שונים ברצף הקלט ביחס זה לזה."
---
## Definition

תשומת לב עצמית מאפשרת למודלים לתפוס תלות בין כל המיקומים ברצף בו זמנית, ללא קשר למרחק. על ידי חישוב ציוני תשומת לב בין כל זוג טוקנים, היא מאפשרת הבחנה בהקשר.

### Summary

מנגנון המאפשר לרשת נוירונים לשקול את חשיבותם של חלקים שונים ברצף הקלט ביחס זה לזה.

## Key Concepts

- שאילתה-מפתח-ערך (Query-Key-Value)
- ציוני תשומת לב
- משקל הקשרי
- עיבוד מקבילי

## Use Cases

- תרגום מכונה
- סיכום טקסט
- מיון תמונות באמצעות Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (טרנספורמר)](/en/terms/transformer-טרנספורמר/)
- [Multi-Head Attention (תשומת לב רב-ראשית)](/en/terms/multi-head-attention-תשומת-לב-רב-ראשית/)
- [Embeddings (טמעת וקטורים)](/en/terms/embeddings-טמעת-וקטורים/)
- [Sequence Modeling (מודלי רצפים)](/en/terms/sequence-modeling-מודלי-רצפים/)
