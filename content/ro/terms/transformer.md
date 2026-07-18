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
  - /ro/terms/transformer/
date: "2026-07-18T15:31:06.936939Z"
lastmod: "2026-07-18T17:15:09.606182Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "O arhitectură de învățare profundă bazată pe mecanisme de auto-atenție care procesează datele secvențiale în paralel, nu secvențial."
---

## Definition

Introdus în lucrarea 'Attention Is All You Need', arhitectura Transformer a revoluționat procesarea limbajului natural și nu numai. Aceasta utilizează auto-atenția multi-cap pentru a pondera semnificația

### Summary

O arhitectură de învățare profundă bazată pe mecanisme de auto-atenție care procesează datele secvențiale în paralel, nu secvențial.

## Key Concepts

- Auto-atenție
- Atenție multi-cap
- Codificare pozițională
- Structură encoder-decoder

## Use Cases

- Traducere automată
- Generare de text
- Recunoaștere de imagini (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (mecanism de atenție)](/en/terms/attention_mechanism-mecanism-de-atenție/)
- [bert (model de limbaj bidirecțional)](/en/terms/bert-model-de-limbaj-bidirecțional/)
- [gpt (model generativ de tip transformer)](/en/terms/gpt-model-generativ-de-tip-transformer/)
- [self_attention (auto-atenție)](/en/terms/self_attention-auto-atenție/)
