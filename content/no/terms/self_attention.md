---
title: "Selvoppmerksomhet"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /no/terms/self_attention/
date: "2026-07-18T15:30:06.305309Z"
lastmod: "2026-07-18T16:38:06.946658Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En mekanisme som lar et nevralt nettverk veie viktigheten av ulike deler av inndatasekvensen i forhold til hverandre."
---

## Definition

Selvoppmerksomhet gjør det mulig for modeller å fange opp avhengigheter mellom alle posisjoner i en sekvens samtidig, uavhengig av avstand. Ved å beregne oppmerksomhetspoeng mellom hvert par av tokens, lar det...

### Summary

En mekanisme som lar et nevralt nettverk veie viktigheten av ulike deler av inndatasekvensen i forhold til hverandre.

## Key Concepts

- Spørsmål-Nøkkel-Verdi
- Oppmerksomhetspoeng
- Kontekstuell vekting
- Parallellprosessering

## Use Cases

- Maskinoversettelse
- Tekstsammendrag
- Bildeklassifisering via Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Transformer)](/en/terms/transformer-transformer/)
- [Multi-Head Attention (Flere hoder oppmerksomhet)](/en/terms/multi-head-attention-flere-hoder-oppmerksomhet/)
- [Embeddings (Innbindinger)](/en/terms/embeddings-innbindinger/)
- [Sequence Modeling (Sekvensmodellering)](/en/terms/sequence-modeling-sekvensmodellering/)
