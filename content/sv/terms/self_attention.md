---
title: "Självuppmärksamhet"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:31:05.936726Z"
lastmod: "2026-07-18T17:15:08.951885Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "En mekanism som låter ett neuralt nätverk väga vikten av olika delar av insökvensen i förhållande till varandra."
---
## Definition

Självuppmärksamhet gör det möjligt för modeller att fånga beroenden mellan alla positioner i en sekvens samtidigt, oavsett avstånd. Genom att beräkna uppmärksamhetspoäng mellan varje par av token möjliggör det...

### Summary

En mekanism som låter ett neuralt nätverk väga vikten av olika delar av insökvensen i förhållande till varandra.

## Key Concepts

- Fråga-Nyckel-Värde
- Uppmärksamhetspoäng
- Kontextuell viktning
- Parallell bearbetning

## Use Cases

- Maskinöversättning
- Textsammanfattning
- Bildklassificering via Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Transformator)](/en/terms/transformer-transformator/)
- [Multi-Head Attention (Flerhuvuds uppmärksamhet)](/en/terms/multi-head-attention-flerhuvuds-uppmärksamhet/)
- [Embeddings (Inbäddningar)](/en/terms/embeddings-inbäddningar/)
- [Sequence Modeling (Sekvensmodellering)](/en/terms/sequence-modeling-sekvensmodellering/)
