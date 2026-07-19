---
title: "Mechanizm uwagi własnej (Self-Attention)"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:29:40.620984Z"
lastmod: "2026-07-18T17:15:08.821028Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Mechanizm pozwalający sieci neuronowej na ważenie znaczenia różnych części sekwencji wejściowej względem siebie nawzajem."
---
## Definition

Mechanizm uwagi własnej umożliwia modelom wychwytywanie zależności między wszystkimi pozycjami w sekwencji jednocześnie, niezależnie od odległości między nimi. Obliczając wyniki uwagi dla każdej pary tokenów, pozwala to na budowanie bogatszego kontekstu reprezentacji.

### Summary

Mechanizm pozwalający sieci neuronowej na ważenie znaczenia różnych części sekwencji wejściowej względem siebie nawzajem.

## Key Concepts

- Zapytanie-Klucz-Wartość (Query-Key-Value)
- Wyniki uwagi (Attention Scores)
- Ważenie kontekstowe
- Przetwarzanie równoległe

## Use Cases

- Tłumaczenie maszynowe
- Podsumowywanie tekstu
- Klasyfikacja obrazów przy użyciu Transformerów wizyjnych (Vision Transformers)

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Architektura Transformer)](/en/terms/transformer-architektura-transformer/)
- [Multi-Head Attention (Uwaga wielogłowowa)](/en/terms/multi-head-attention-uwaga-wielogłowowa/)
- [Embeddings (Osadzenia wektorowe)](/en/terms/embeddings-osadzenia-wektorowe/)
- [Sequence Modeling (Modelowanie sekwencji)](/en/terms/sequence-modeling-modelowanie-sekwencji/)
