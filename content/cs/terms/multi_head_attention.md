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
date: '2026-07-18T15:27:14.908065Z'
lastmod: '2026-07-18T17:15:09.073558Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Mechanismus v modelech typu transformer, který umožňuje modelu současně
  věnovat pozornost informacím z různých podprostorů reprezentace.
---
## Definition

Multi-Head Attention rozšiřuje standardní mechanismus pozornosti tím, že jej spouští vícekrát paralelně s různými naučenými lineárními projekcemi. To umožňuje modelu společně sledovat informace z různých perspektiv.

### Summary

Mechanismus v modelech typu transformer, který umožňuje modelu současně věnovat pozornost informacím z různých podprostorů reprezentace.

## Key Concepts

- Self-Attention (Vlastní pozornost)
- Lineární projekce
- Konkatenace

## Use Cases

- Zpracování přirozeného jazyka (NLP)
- Strojový překlad
- Klasifikace obrázků pomocí Vision Transformerů

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

- [Scaled Dot-Product Attention (Škálovaná skalární součinová pozornost)](/en/terms/scaled-dot-product-attention-škálovaná-skalární-součinová-pozornost/)
- [Transformer (Transformér)](/en/terms/transformer-transformér/)
- [Embedding (Vložení do prostoru vektorů)](/en/terms/embedding-vložení-do-prostoru-vektorů/)
