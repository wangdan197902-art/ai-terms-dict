---
title: "Selvopmærksomhed"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:30:04.276328Z"
lastmod: "2026-07-18T17:15:09.233875Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En mekanisme, der tillader et neuralt netværk at vægte vigtigheden af forskellige dele af inputsekvensen i forhold til hinanden."
---
## Definition

Selvopmærksomhed gør det muligt for modeller at fange afhængigheder mellem alle positioner i en sekvens samtidigt, uanset afstand. Ved at beregne opmærksomhedsscorer mellem hvert par af tokens tillader det...

### Summary

En mekanisme, der tillader et neuralt netværk at vægte vigtigheden af forskellige dele af inputsekvensen i forhold til hinanden.

## Key Concepts

- Query-Key-Value (Forespørgsels-Nøgle-Værdi)
- Opmærksomhedsscorer
- Kontekstuel vægtning
- Parallel behandling

## Use Cases

- Maskinoversættelse
- Tekstsammendrag
- Billedklassificering via Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Transformatormodel)](/en/terms/transformer-transformatormodel/)
- [Multi-Head Attention (Flere hoveders opmærksomhed)](/en/terms/multi-head-attention-flere-hoveders-opmærksomhed/)
- [Embeddings (Indlejringer)](/en/terms/embeddings-indlejringer/)
- [Sequence Modeling (Sekvensmodellering)](/en/terms/sequence-modeling-sekvensmodellering/)
