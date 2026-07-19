---
title: Transformer
term_id: transformer
category: basic_concepts
subcategory: ''
tags:
- architecture
- NLP
- attention
difficulty: 4
weight: 1
slug: transformer
date: '2026-07-18T15:32:00.875183Z'
lastmod: '2026-07-18T17:15:08.954398Z'
draft: false
source: agnes_llm
status: published
language: sv
description: En djupinlärningsarkitektur baserad på självuppmärksamhetsmekanismer
  som bearbetar sekventiell data parallellt snarare än sekventiellt.
---
## Definition

Introducerad i artikeln 'Attention Is All You Need', revolutionerade Transformer-arkitekturen naturlig språkbehandling och mer. Den använder flerkopplad självuppmärksamhet för att väga betydelsen av olika delar av indata, vilket tillåter effektiv hantering av långa beroenden i data.

### Summary

En djupinlärningsarkitektur baserad på självuppmärksamhetsmekanismer som bearbetar sekventiell data parallellt snarare än sekventiellt.

## Key Concepts

- Självuppmärksamhet
- Flerkoppad uppmärksamhet
- Positionell kodning
- Kodare-dekodare-struktur

## Use Cases

- Maskinöversättning
- Textgenerering
- Bildigenkänning (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (uppmärksamhetsmekanism)](/en/terms/attention_mechanism-uppmärksamhetsmekanism/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (självuppmärksamhet)](/en/terms/self_attention-självuppmärksamhet/)
