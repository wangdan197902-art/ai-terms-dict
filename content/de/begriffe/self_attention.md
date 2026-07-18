---
title: "Selbstaufmerksamkeit"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /de/terms/self_attention/
date: "2026-07-18T10:53:51.234652Z"
lastmod: "2026-07-18T11:44:44.883739Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Ein Mechanismus, der es einem neuronalen Netzwerk ermöglicht, die Bedeutung verschiedener Teile der Eingabesequenz im Verhältnis zueinander zu gewichten."
---

## Definition

Selbstaufmerksamkeit ermöglicht es Modellen, Abhängigkeiten zwischen allen Positionen in einer Sequenz gleichzeitig zu erfassen, unabhängig von deren Entfernung. Durch die Berechnung von Aufmerksamkeitswerten zwischen jedem Token-Paar wird dies ermöglicht.

### Summary

Ein Mechanismus, der es einem neuronalen Netzwerk ermöglicht, die Bedeutung verschiedener Teile der Eingabesequenz im Verhältnis zueinander zu gewichten.

## Key Concepts

- Query-Key-Value
- Aufmerksamkeitswerte
- Kontextuelle Gewichtung
- Parallele Verarbeitung

## Use Cases

- Maschinelle Übersetzung
- Zusammenfassung von Texten
- Bildklassifizierung mittels Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer](/en/terms/transformer/)
- [Multi-Head Attention (Multi-Head-Aufmerksamkeit)](/en/terms/multi-head-attention-multi-head-aufmerksamkeit/)
- [Embeddings (Einbettungen)](/en/terms/embeddings-einbettungen/)
- [Sequence Modeling (Sequenzmodellierung)](/en/terms/sequence-modeling-sequenzmodellierung/)
