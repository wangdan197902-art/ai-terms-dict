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
  - /no/terms/transformer/
date: "2026-07-18T15:31:43.209982Z"
lastmod: "2026-07-18T16:38:06.949354Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En dyp læringsarkitektur basert på selvoppmerksomhetsmekanismer som behandler sekvensielle data parallelt i stedet for sekvensielt."
---

## Definition

Introdusert i artikkelen 'Attention Is All You Need', revolusjonerte Transformer-arkitekturen naturlig språkbehandling og mer. Den bruker flerhodet selvoppmerksomhet for å veie betydningen av

### Summary

En dyp læringsarkitektur basert på selvoppmerksomhetsmekanismer som behandler sekvensielle data parallelt i stedet for sekvensielt.

## Key Concepts

- Selvoppmerksomhet
- Flerhodet oppmerksomhet
- Posisjonell koding
- Koder-dekoder-struktur

## Use Cases

- Maskinoversettelse
- Tekstgenerering
- Bilderekognisjon (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (oppmerksomhetsmekanisme)](/en/terms/attention_mechanism-oppmerksomhetsmekanisme/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (selvoppmerksomhet)](/en/terms/self_attention-selvoppmerksomhet/)
