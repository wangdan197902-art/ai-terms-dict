---
title: "Self-Attention"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:29:09.463065Z"
lastmod: "2026-07-18T17:15:09.078200Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Mechanismus umožňující neuronové síti vážit významnost různých částí vstupní sekvence vůči sobě navzájem."
---
## Definition

Self-attention umožňuje modelům zachytit závislosti mezi všemi pozicemi v sekvenci současně, bez ohledu na vzdálenost. Výpočtem skóre pozornosti mezi každou dvojici tokenů umožňuje...

### Summary

Mechanismus umožňující neuronové síti vážit významnost různých částí vstupní sekvence vůči sobě navzájem.

## Key Concepts

- Dotaz-Hodnota-Klíč (Query-Key-Value)
- Skóre pozornosti
- Kontextové vážení
- Paralelní zpracování

## Use Cases

- Strojový překlad
- Shrnování textu
- Klasifikace obrázků pomocí Vision Transformerů

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Transformátor)](/en/terms/transformer-transformátor/)
- [Multi-Head Attention (Vícenásobná pozornost)](/en/terms/multi-head-attention-vícenásobná-pozornost/)
- [Embeddings (Vektorová reprezentace)](/en/terms/embeddings-vektorová-reprezentace/)
- [Sequence Modeling (Modelování sekvencí)](/en/terms/sequence-modeling-modelování-sekvencí/)
