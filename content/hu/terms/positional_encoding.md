---
title: Pozíciós kódolás
term_id: positional_encoding
category: basic_concepts
subcategory: ''
tags:
- transformers
- NLP
- architecture
difficulty: 3
weight: 1
slug: positional_encoding
date: '2026-07-18T15:39:10.836914Z'
lastmod: '2026-07-18T17:15:09.743437Z'
draft: false
source: agnes_llm
status: published
language: hu
description: Egy technika, amely információkat juttat el a tokenek relatív vagy abszolút
  pozíciójáról egy szekvenciában a transzformátor modellekbe.
---
## Definition

Mivel a transzformátorok párhuzamosan dolgozzák fel az összes tokent, szemben a szekvenciális feldolgozással, mint az RNN-eknél, hiányzik belőlük a tokenek sorrendjére vonatkozó veleszületett tudás. A pozíciós kódolás specifikus vektorokat ad hozzá a bemeneti beágyazásokhoz (embeddings), hogy biztosítsa a modell számára a sorrendi információt.

### Summary

Egy technika, amely információkat juttat el a tokenek relatív vagy abszolút pozíciójáról egy szekvenciában a transzformátor modellekbe.

## Key Concepts

- Szekvencia sorrendje
- Önfigyelem (Self-Attention)
- Szinuszos függvények
- Token beágyazások

## Use Cases

- Gépi fordítás
- Szövegösszefoglalás
- Nyelvi modellezés

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

- [Transformer architektúra](/en/terms/transformer-architektúra/)
- [Beágyazás (Embedding)](/en/terms/beágyazás-embedding/)
- [Figyelem mechanizmus (Attention Mechanism)](/en/terms/figyelem-mechanizmus-attention-mechanism/)
- [RoPE (Rotary Positional Embeddings)](/en/terms/rope-rotary-positional-embeddings/)
