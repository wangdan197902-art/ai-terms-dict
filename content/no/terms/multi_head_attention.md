---
title: Multi-Head Attention
term_id: multi_head_attention
category: basic_concepts
subcategory: ''
tags:
- transformer
- NLP
- Deep Learning
difficulty: 4
weight: 1
slug: multi_head_attention
date: '2026-07-18T15:28:06.893111Z'
lastmod: '2026-07-18T16:38:06.941711Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En mekanisme i transformer-modeller som lar modellen fokusere på informasjon
  fra ulike representasjonsundersrom samtidig.
---
## Definition

Multi-Head Attention utvider den vanlige oppmerksomhetsmekanismen ved å kjøre den flere ganger parallelt med ulike lærte lineære projeksjoner. Dette gjør det mulig for modellen å samtidig fokusere på informasjon fra forskjellige posisjoner i inputsekvensen.

### Summary

En mekanisme i transformer-modeller som lar modellen fokusere på informasjon fra ulike representasjonsundersrom samtidig.

## Key Concepts

- Selvoppmerksomhet
- Lineære projeksjoner
- Konkatenering

## Use Cases

- Naturlig språkbehandling (NLP)
- Maskinomsetning
- Bildklassifisering med Vision Transformers

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

- [Scaled Dot-Product Attention (Skalert prikkprodukt-oppmerksomhet)](/en/terms/scaled-dot-product-attention-skalert-prikkprodukt-oppmerksomhet/)
- [Transformer (Transformer)](/en/terms/transformer-transformer/)
- [Embedding (Innbinding)](/en/terms/embedding-innbinding/)
