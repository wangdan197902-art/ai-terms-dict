---
title: "Transformer"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /da/terms/transformer/
date: "2026-07-18T15:31:03.895235Z"
lastmod: "2026-07-18T17:15:09.236087Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En dyb læringsarkitektur baseret på selvaftemekanismer, der behandler sekventielle data parallelt i stedet for sekventielt."
---

## Definition

Introduceret i artiklen 'Attention Is All You Need', revolutionerede Transformer-arkitekturen naturlig sprogbehandling og mere. Den bruger multi-head selvaftemekanismer til at veje betydningen af

### Summary

En dyb læringsarkitektur baseret på selvaftemekanismer, der behandler sekventielle data parallelt i stedet for sekventielt.

## Key Concepts

- Selvopmærksomhed
- Multi-head opmærksomhed
- Positionel kodning
- Encoder-Decoder struktur

## Use Cases

- Maskinoversættelse
- Tekstgenerering
- Anerkendelse af billeder (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (opmærksomhedsmekanisme)](/en/terms/attention_mechanism-opmærksomhedsmekanisme/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (selvopmærksomhed)](/en/terms/self_attention-selvopmærksomhed/)
