---
title: Többfejes Figyelem
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
date: '2026-07-18T15:28:34.654556Z'
lastmod: '2026-07-18T17:15:09.725219Z'
draft: false
source: agnes_llm
status: published
language: hu
description: Egy mechanizmus a transformer modellekben, amely lehetővé teszi a modell
  számára, hogy egyszerre figyeljen különböző reprezentációs altérbeli információkra.
---
## Definition

A Többfejes Figyelem kiterjeszti az alapfigyelem mechanizmust azzal, hogy azt többször futtatja párhuzamosan különböző tanult lineáris vetületekkel. Ez lehetővé teszi a modell számára, hogy egyidejűleg többféle információtípust vagy kapcsolatot figyeljen meg.

### Summary

Egy mechanizmus a transformer modellekben, amely lehetővé teszi a modell számára, hogy egyszerre figyeljen különböző reprezentációs altérbeli információkra.

## Key Concepts

- Önfigyelem (Self-Attention)
- Lineáris vetületek
- Konkatenáció (összefűzés)

## Use Cases

- Természetes nyelvfeldolgozás (NLP)
- Gépi fordítás
- Képosztályozás Vision Transformerrel

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

- [Scaled Dot-Product Attention (Skálázott skaláris szorzatú figyelem)](/en/terms/scaled-dot-product-attention-skálázott-skaláris-szorzatú-figyelem/)
- [Transformer (Átalakító)](/en/terms/transformer-átalakító/)
- [Embedding (Beágyazás)](/en/terms/embedding-beágyazás/)
