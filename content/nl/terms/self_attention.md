---
title: "Zelfattentie"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:29:49.508445Z"
lastmod: "2026-07-18T17:15:08.693555Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een mechanisme waarmee een neurale netwerk het belang van verschillende delen van de invoersequentie ten opzichte van elkaar kan wegen."
---
## Definition

Zelfattentie stelt modellen in staat om afhankelijkheden tussen alle posities in een sequentie tegelijkertijd vast te stellen, ongeacht de afstand. Door attentiescores te berekenen tussen elk paar tokens, maakt het...

### Summary

Een mechanisme waarmee een neurale netwerk het belang van verschillende delen van de invoersequentie ten opzichte van elkaar kan wegen.

## Key Concepts

- Query-Key-Value
- Attentiescores
- Contextuele Weging
- Parallelle Verwerking

## Use Cases

- Maskinevertaling
- Tekstsamenvatting
- Afbeeldingsclassificatie via Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Neuraal netwerkarchitectuur)](/en/terms/transformer-neuraal-netwerkarchitectuur/)
- [Multi-Head Attention (Meervoudige attentiemechanismen)](/en/terms/multi-head-attention-meervoudige-attentiemechanismen/)
- [Embeddings (Vectorrepresentaties)](/en/terms/embeddings-vectorrepresentaties/)
- [Sequencemodelering (Modelleren van opeenvolgende data)](/en/terms/sequencemodelering-modelleren-van-opeenvolgende-data/)
