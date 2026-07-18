---
title: "Posisjonskoding"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /no/terms/positional_encoding/
date: "2026-07-18T15:38:08.069269Z"
lastmod: "2026-07-18T16:38:06.961101Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En teknikk som injiserer informasjon om den relative eller absolutte posisjonen til tokens i en sekvens inn i transformer-modeller."
---

## Definition

Siden transformers behandler alle tokens parallelt i stedet for sekvensielt som RNN-er, mangler de innebygd kunnskap om tokenrekkefølgen. Posisjonskoding legger til spesifikke vektorer til input-embeddings for å gi modellen informasjon om rekkefølgen.

### Summary

En teknikk som injiserer informasjon om den relative eller absolutte posisjonen til tokens i en sekvens inn i transformer-modeller.

## Key Concepts

- Sekvensrekkefølge
- Selv-oppmerksomhet (Self-Attention)
- Sinusoide funksjoner
- Token-embeddings

## Use Cases

- Maskinoversettelse
- Tekstsammendrag
- Språkmodellering

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

- [Transformer-arkitektur (Transformer Architecture)](/en/terms/transformer-arkitektur-transformer-architecture/)
- [Embedding](/en/terms/embedding/)
- [Oppmerksomhetsmekanisme (Attention Mechanism)](/en/terms/oppmerksomhetsmekanisme-attention-mechanism/)
- [RoPE (Rotary Positional Embeddings)](/en/terms/rope-rotary-positional-embeddings/)
