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
date: '2026-07-18T15:29:10.733260Z'
lastmod: '2026-07-18T17:15:08.947138Z'
draft: false
source: agnes_llm
status: published
language: sv
description: En mekanism i transformer-modeller som gör att modellen kan uppmärksamma
  information från olika representationsunderutrymmen samtidigt.
---
## Definition

Multi-Head Attention utvidgar den standardiserade uppmärksamhetsmekanismen genom att köra den flera gånger parallellt med olika inlärd linjära projektioner. Detta gör att modellen gemensamt kan uppmärksamma information från olika positioner i sekvensen.

### Summary

En mekanism i transformer-modeller som gör att modellen kan uppmärksamma information från olika representationsunderutrymmen samtidigt.

## Key Concepts

- Self-Attention (Självuppmärksamhet)
- Linjära projektioner
- Konkatenering

## Use Cases

- Bearbetning av naturligt språk (NLP)
- Maskinöversättning
- Bildklassificering med Vision Transformers

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

- [Scaled Dot-Product Attention (Skalad punktproduktuppmärksamhet)](/en/terms/scaled-dot-product-attention-skalad-punktproduktuppmärksamhet/)
- [Transformer (Transformer)](/en/terms/transformer-transformer/)
- [Embedding (Inbäddning)](/en/terms/embedding-inbäddning/)
