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
  - /nl/terms/transformer/
date: "2026-07-18T15:30:54.679673Z"
lastmod: "2026-07-18T17:15:08.695685Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een diepe leerarchitectuur gebaseerd op zelfattentie-mechanismen die sequentiële gegevens parallel verwerkt in plaats van sequentieel."
---

## Definition

Geïntroduceerd in het artikel 'Attention Is All You Need', heeft de Transformer-architectuur de natuurlijke taalverwerking en daarbuiten revolutionair veranderd. Het gebruikt multi-head zelfattentie om het belang van

### Summary

Een diepe leerarchitectuur gebaseerd op zelfattentie-mechanismen die sequentiële gegevens parallel verwerkt in plaats van sequentieel.

## Key Concepts

- Zelfattentie
- Multi-Head Attentie
- Positievecodering
- Encoder-Decoder Structuur

## Use Cases

- Maskinevertaling
- Tekstgeneratie
- Beeldherkenning (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (attentie-mechanisme)](/en/terms/attention_mechanism-attentie-mechanisme/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (zelfattentie)](/en/terms/self_attention-zelfattentie/)
