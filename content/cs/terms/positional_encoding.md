---
title: "Poziciální kódování"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /cs/terms/positional_encoding/
date: "2026-07-18T15:37:59.146672Z"
lastmod: "2026-07-18T17:15:09.092035Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Technika, která vkládá informace o relativní nebo absolutní poloze tokenů v sekvenci do modelů typu transformer."
---

## Definition

Protože modely transformer zpracovávají všechny tokeny paralelně, nikoli sekvenčně jako rekurentní neuronové sítě (RNN), postrádají vrozenou znalost pořadí tokenů. Poziciální kódování přidává specifické vektory k vstupním vektorům embeddingů, aby zachovalo informaci o pořadí.

### Summary

Technika, která vkládá informace o relativní nebo absolutní poloze tokenů v sekvenci do modelů typu transformer.

## Key Concepts

- Pořadí sekvence
- Vlastní pozornost (Self-Attention)
- Sinusoidální funkce
- Vektory embeddingů tokenů

## Use Cases

- Strojový překlad
- Shrnování textu
- Jazykové modelování

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

- [Architektura Transformer (typ architektury neuronové sítě)](/en/terms/architektura-transformer-typ-architektury-neuronové-sítě/)
- [Embedding (reprezentace slov jako vektorů)](/en/terms/embedding-reprezentace-slov-jako-vektorů/)
- [Mechanismus pozornosti (způsob vážení důležitosti vstupů)](/en/terms/mechanismus-pozornosti-způsob-vážení-důležitosti-vstupů/)
- [RoPE (Rotary Positional Embedding, rotující poziciální kódování)](/en/terms/rope-rotary-positional-embedding-rotující-poziciální-kódování/)
