---
title: "Multi-Head Attention"
term_id: "multi_head_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformer", "nlp", "deep_learning"]
difficulty: 4
weight: 1
slug: "multi_head_attention"
aliases:
  - /da/terms/multi_head_attention/
date: "2026-07-18T15:27:33.940335Z"
lastmod: "2026-07-18T17:15:09.229255Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En mekanisme i transformer-modeller, der giver modellen mulighed for at fokusere på information fra forskellige repræsentationsundersystemer samtidigt."
---

## Definition

Multi-Head Attention udvider den standard opmærksomhedsmechanisme ved at køre den flere gange parallelt med forskellige lærte lineære projektioner. Dette gør det muligt for modellen samtidig at fokusere på information fra forskellige positioner.

### Summary

En mekanisme i transformer-modeller, der giver modellen mulighed for at fokusere på information fra forskellige repræsentationsundersystemer samtidigt.

## Key Concepts

- Selvopmærksomhed
- Lineære projektioner
- Konkatenation

## Use Cases

- Naturlig sprogbehandling (NLP)
- Maskinoversættelse
- Billedklassificering med Vision Transformers

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

- [Scaled Dot-Product Attention (Skaleret prikprodukt-opmærksomhed)](/en/terms/scaled-dot-product-attention-skaleret-prikprodukt-opmærksomhed/)
- [Transformer (Transformer)](/en/terms/transformer-transformer/)
- [Embedding (Indlejring)](/en/terms/embedding-indlejring/)
