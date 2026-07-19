---
title: Atenție Multi-Cap
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
date: '2026-07-18T15:27:33.695223Z'
lastmod: '2026-07-18T17:15:09.599170Z'
draft: false
source: agnes_llm
status: published
language: ro
description: Un mecanism în modelele transformator care permite modelului să acorde
  atenție informațiilor din diferite subspații de reprezentare simultan.
---
## Definition

Atenția Multi-Cap extinde mecanismul standard de atenție rulându-l de mai multe ori în paralel cu proiecții liniare diferite învățate. Acest lucru permite modelului să acorde atenție simultan informațiilor din diverse perspective.

### Summary

Un mecanism în modelele transformator care permite modelului să acorde atenție informațiilor din diferite subspații de reprezentare simultan.

## Key Concepts

- Auto-Atenție
- Proiecții Liniare
- Concatenare

## Use Cases

- Procesarea Limbajului Natural (NLP)
- Traducere Automată
- Clasificarea Imaginilor cu Transformatori Vizuali (ViT)

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

- [Scaled Dot-Product Attention (Atenție Produnt Scalată)](/en/terms/scaled-dot-product-attention-atenție-produnt-scalată/)
- [Transformer (Transformator)](/en/terms/transformer-transformator/)
- [Embedding (Încapsulare/Embedding)](/en/terms/embedding-încapsulare-embedding/)
