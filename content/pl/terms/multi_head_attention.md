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
date: '2026-07-18T15:27:31.236939Z'
lastmod: '2026-07-18T17:15:08.816230Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Mechanizm w modelach transformatorów umożliwiający modelowi jednoczesne
  skupianie uwagi na informacjach z różnych podprzestrzeni reprezentacji.
---
## Definition

Multi-Head Attention rozszerza standardowy mechanizm uwagi, uruchamiając go wielokrotnie równolegle z różnymi nauczanymi projekcjami liniowymi. Umożliwia to modelowi jednoczesne skupianie uwagi na różnych aspektach informacji wejściowej.

### Summary

Mechanizm w modelach transformatorów umożliwiający modelowi jednoczesne skupianie uwagi na informacjach z różnych podprzestrzeni reprezentacji.

## Key Concepts

- Self-Attention (Uwaga własna)
- Projekcje liniowe
- Konkatenacja

## Use Cases

- Przetwarzanie języka naturalnego (NLP)
- Tłumaczenie maszynowe
- Klasyfikacja obrazów z użyciem Vision Transformers

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

- [Scaled Dot-Product Attention (Uwaga skalowanego iloczynu skalarnego)](/en/terms/scaled-dot-product-attention-uwaga-skalowanego-iloczynu-skalarnego/)
- [Transformer (Transformator)](/en/terms/transformer-transformator/)
- [Embedding (Osadzenie/wektorowanie)](/en/terms/embedding-osadzenie-wektorowanie/)
