---
title: "Transformátor"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /cs/terms/transformer/
date: "2026-07-18T15:30:50.714575Z"
lastmod: "2026-07-18T17:15:09.080712Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Architektura hlubokého učení založená na mechanismu sebevědomé pozornosti (self-attention), která zpracovává sekvenční data paralelně místo postupně."
---

## Definition

Zavedená v článku 'Attention Is All You Need', architektura Transformátoru revolucionalizovala zpracování přirozeného jazyka a další oblasti. Používá vícebuněčnou sebevědomou pozornost k vážení významu

### Summary

Architektura hlubokého učení založená na mechanismu sebevědomé pozornosti (self-attention), která zpracovává sekvenční data paralelně místo postupně.

## Key Concepts

- Sebevědomá pozornost (Self-Attention)
- Vícebuněčná pozornost (Multi-Head Attention)
- Polohové kódování (Positional Encoding)
- Struktura enkodér-dekodér

## Use Cases

- Strojový překlad
- Generování textu
- Rozpoznávání obrázků (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (Mechanismus pozornosti)](/en/terms/attention_mechanism-mechanismus-pozornosti/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (Sebevědomá pozornost)](/en/terms/self_attention-sebevědomá-pozornost/)
