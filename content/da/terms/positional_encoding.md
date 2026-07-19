---
title: Positional Encoding
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
date: '2026-07-18T15:37:15.359716Z'
lastmod: '2026-07-18T17:15:09.247722Z'
draft: false
source: agnes_llm
status: published
language: da
description: En teknik, der indsprøjter oplysninger om de relative eller absolutte
  positioner af tokens i en sekvens ind i transformer-modeller.
---
## Definition

Da transformer-modeller behandler alle tokens parallelt i stedet for sekventielt som RNN'er, mangler de en iboende viden om token-rækkefølgen. Positional encoding tilføjer specifikke vektorer til input-embeddings for at bevare rækkefølgeinformationen.

### Summary

En teknik, der indsprøjter oplysninger om de relative eller absolutte positioner af tokens i en sekvens ind i transformer-modeller.

## Key Concepts

- Sekvensrækkefølge
- Selvopmærksomhed (Self-Attention)
- Sinusoide funktioner
- Token-embeddings

## Use Cases

- Maskinoversættelse
- Tekstsammendrag
- Sprogmodellering

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

- [Transformer-arkitektur (Den underliggende modelstruktur)](/en/terms/transformer-arkitektur-den-underliggende-modelstruktur/)
- [Embedding (Vektorgengivelse af ord)](/en/terms/embedding-vektorgengivelse-af-ord/)
- [Attention-mekanisme (Måden modellen fokuserer på input)](/en/terms/attention-mekanisme-måden-modellen-fokuserer-på-input/)
- [RoPE (Rotary Positional Encoding)](/en/terms/rope-rotary-positional-encoding/)
