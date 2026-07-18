---
title: "Positiecodering"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /nl/terms/positional_encoding/
date: "2026-07-18T15:38:16.596955Z"
lastmod: "2026-07-18T17:15:08.707430Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een techniek die informatie over de relatieve of absolute positie van tokens in een sequentie injecteert in transformermodellen."
---

## Definition

Aangezien transformers alle tokens parallel verwerken in plaats van sequentieel zoals RNN's, ontbreekt hen de inherente kennis van de volgorde van tokens. Positiecodering voegt specifieke vectoren toe aan de invoerembeddings om de positie-informatie te behouden.

### Summary

Een techniek die informatie over de relatieve of absolute positie van tokens in een sequentie injecteert in transformermodellen.

## Key Concepts

- Sequentievolgorde
- Zelf-attention
- Sinusoïdale functies
- Token-embeddings

## Use Cases

- Maskinevertaling
- Tekstsamenvatting
- Taalmodellering

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

- [Transformerarchitectuur (De basisstructuur van het model)](/en/terms/transformerarchitectuur-de-basisstructuur-van-het-model/)
- [Embedding (Vectorrepresentatie van tokens)](/en/terms/embedding-vectorrepresentatie-van-tokens/)
- [Attention-mechanisme (Methode om focus op delen van de invoer te leggen)](/en/terms/attention-mechanisme-methode-om-focus-op-delen-van-de-invoer-te-leggen/)
- [RoPE (Rotatiepositiecodering)](/en/terms/rope-rotatiepositiecodering/)
