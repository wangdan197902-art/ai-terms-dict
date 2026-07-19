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
date: '2026-07-18T15:30:57.836790Z'
lastmod: '2026-07-18T17:15:08.823501Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Architektura głębokiego uczenia oparta na mechanizmach samouważania (self-attention),
  która przetwarza dane sekwencyjne równolegle, a nie sekwencyjnie.
---
## Definition

Przedstawiona w artykule „Attention Is All You Need”, architektura Transformer zrewolucjonizowała przetwarzanie języka naturalnego i inne dziedziny. Wykorzystuje wielogłowicowe samouważanie do ważenia znaczenia poszczególnych elementów wejściowych, umożliwiając efektywne modelowanie długich zależności.

### Summary

Architektura głębokiego uczenia oparta na mechanizmach samouważania (self-attention), która przetwarza dane sekwencyjne równolegle, a nie sekwencyjnie.

## Key Concepts

- Samouważanie (Self-Attention)
- Wielogłowicowe uwaga (Multi-Head Attention)
- Kodowanie pozycyjne (Positional Encoding)
- Struktura enkoder-dekodera

## Use Cases

- Tłumaczenie maszynowe
- Generowanie tekstu
- Rozpoznawanie obrazów (np. ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (mechanizm uwagi)](/en/terms/attention_mechanism-mechanizm-uwagi/)
- [bert (architektura modelu BERT)](/en/terms/bert-architektura-modelu-bert/)
- [gpt (rodzina modeli GPT)](/en/terms/gpt-rodzina-modeli-gpt/)
- [self_attention (samouważanie)](/en/terms/self_attention-samouważanie/)
