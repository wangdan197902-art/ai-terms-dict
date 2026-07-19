---
title: "Atenție Auto"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:29:35.306089Z"
lastmod: "2026-07-18T17:15:09.604037Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Un mecanism care permite unei rețele neuronale să evalueze importanța diferitelor părți ale secvenței de intrare în raport cu celelalte."
---
## Definition

Atenția auto permite modelelor să capteze dependențele dintre toate pozițiile dintr-o secvență simultan, indiferent de distanță. Prin calcularea scorurilor de atenție între fiecare pereche de tokenuri, aceasta permite...

### Summary

Un mecanism care permite unei rețele neuronale să evalueze importanța diferitelor părți ale secvenței de intrare în raport cu celelalte.

## Key Concepts

- Interogare-Chiuvetă-Valoare (Query-Key-Value)
- Scoruri de Atenție
- Agregare Contextuală
- Procesare Parallelă

## Use Cases

- Traducere automată
- Sinteză text
- Clasificare de imagini prin Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Transformator)](/en/terms/transformer-transformator/)
- [Multi-Head Attention (Atenție Multi-Cap)](/en/terms/multi-head-attention-atenție-multi-cap/)
- [Embeddings (Încorporări)](/en/terms/embeddings-încorporări/)
- [Sequence Modeling (Modelare de Secvențe)](/en/terms/sequence-modeling-modelare-de-secvențe/)
