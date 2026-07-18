---
title: "Kodowanie pozycyjne"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /pl/terms/positional_encoding/
date: "2026-07-18T15:36:33.646143Z"
lastmod: "2026-07-18T17:15:08.835393Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Technika wstrzykiwania informacji o względnej lub bezwzględnej pozycji tokenów w sekwencji do modeli transformera."
---

## Definition

Ponieważ transformatory przetwarzają wszystkie tokeny równolegle, a nie sekwencyjnie jak sieci RNN, brakuje im wbudowanej wiedzy o kolejności tokenów. Kodowanie pozycyjne dodaje specyficzne wektory do osadzonych wejść (embeddings), aby nadać modelowi informację o porządku elementów w sekwencji.

### Summary

Technika wstrzykiwania informacji o względnej lub bezwzględnej pozycji tokenów w sekwencji do modeli transformera.

## Key Concepts

- Kolejność sekwencji
- Mechanizm samo-uwagi (Self-Attention)
- Funkcje sinusoidalne
- Osadzenia tokenów (Token Embeddings)

## Use Cases

- Tłumaczenie maszynowe
- Podsumowywanie tekstu
- Modelowanie językowe

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

- [Architektura Transformer (Struktura modelu Transformer)](/en/terms/architektura-transformer-struktura-modelu-transformer/)
- [Embedding (Reprezentacja wektorowa słowa)](/en/terms/embedding-reprezentacja-wektorowa-słowa/)
- [Mechanizm uwagi (Attention Mechanism)](/en/terms/mechanizm-uwagi-attention-mechanism/)
- [RoPE (Rotary Positional Embeddings - Rotacyjne osadzenia pozycyjne)](/en/terms/rope-rotary-positional-embeddings-rotacyjne-osadzenia-pozycyjne/)
