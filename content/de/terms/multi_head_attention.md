---
title: Multi-Head Attention
term_id: multi_head_attention
category: basic_concepts
subcategory: ''
tags:
- transformer
- NLP
- Deep Learning
difficulty: 4
weight: 1
slug: multi_head_attention
date: '2026-07-18T10:52:05.398473Z'
lastmod: '2026-07-18T11:44:44.879056Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein Mechanismus in Transformer-Modellen, der es dem Modell ermöglicht,
  gleichzeitig Informationen aus verschiedenen Repräsentations-Subräumen zu beachten.
---
## Definition

Multi-Head Attention erweitert den Standard-Aufmerksamkeitsmechanismus, indem er mehrere Male parallel mit unterschiedlichen gelernten linearen Projektionen ausgeführt wird. Dies ermöglicht es dem Modell, Informationen aus verschiedenen Perspektiven gemeinsam zu berücksichtigen.

### Summary

Ein Mechanismus in Transformer-Modellen, der es dem Modell ermöglicht, gleichzeitig Informationen aus verschiedenen Repräsentations-Subräumen zu beachten.

## Key Concepts

- Selbst-Aufmerksamkeit
- Lineare Projektionen
- Verkettung

## Use Cases

- Natural Language Processing (NLP)
- Maschinelle Übersetzung
- Bildklassifizierung mit Vision Transformern

## Code Example

```python
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        # Simplified forward pass logic
        pass
```

## Related Terms

- [Scaled Dot-Product Attention (Skalierte Punktprodukt-Aufmerksamkeit)](/en/terms/scaled-dot-product-attention-skalierte-punktprodukt-aufmerksamkeit/)
- [Transformer (Transformer)](/en/terms/transformer-transformer/)
- [Embedding (Einbettung)](/en/terms/embedding-einbettung/)
