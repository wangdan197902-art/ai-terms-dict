---
title: "Codare Pozițională"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /ro/terms/positional_encoding/
date: "2026-07-18T15:37:35.875036Z"
lastmod: "2026-07-18T17:15:09.617122Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "O tehnică care introduce informații despre poziția relativă sau absolută a tokenurilor într-o secvență în modelele Transformer."
---

## Definition

Deoarece Transformer-urile procesează toate tokenurile în paralel, spre deosebire de RNN-urile care le procesează secvențial, acestea nu au o cunoaștere inerentă a ordinii tokenurilor. Codarea pozițională adaugă vectori specifici la încorporările (embeddings) de intrare pentru a prezerva ordinea.

### Summary

O tehnică care introduce informații despre poziția relativă sau absolută a tokenurilor într-o secvență în modelele Transformer.

## Key Concepts

- Ordinea Secvenței
- Auto-Atenție
- Funcții Sinusoidale
- Încorporări Token

## Use Cases

- Traducere Automatică
- Sinteză Textuală
- Modelare Lingvistică

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

- [Arhitectura Transformer (Arhitectura modelului bazat pe atenție)](/en/terms/arhitectura-transformer-arhitectura-modelului-bazat-pe-atenție/)
- [Încorporare (Reprezentarea vectorială a datelor)](/en/terms/încorporare-reprezentarea-vectorială-a-datelor/)
- [Mecanism de Atenție (Procesul de ponderare a importanței elementelor)](/en/terms/mecanism-de-atenție-procesul-de-ponderare-a-importanței-elementelor/)
- [RoPE (Codare Pozițională Rotativă)](/en/terms/rope-codare-pozițională-rotativă/)
