---
title: "Attention multi-têtes"
term_id: "multi_head_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformer", "nlp", "deep_learning"]
difficulty: 4
weight: 1
slug: "multi_head_attention"
aliases:
  - /fr/terms/multi_head_attention/
date: "2026-07-18T10:52:00.887805Z"
lastmod: "2026-07-18T11:44:45.167499Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Un mécanisme dans les modèles transformateurs permettant au modèle de prêter attention à des informations provenant de différents sous-espaces de représentation simultanément."
---

## Definition

L'attention multi-têtes étend le mécanisme d'attention standard en l'exécutant plusieurs fois en parallèle avec différentes projections linéaires apprises. Cela permet au modèle de prêter conjointement attention à diverses informations.

### Summary

Un mécanisme dans les modèles transformateurs permettant au modèle de prêter attention à des informations provenant de différents sous-espaces de représentation simultanément.

## Key Concepts

- Auto-attention
- Projections linéaires
- Concaténation

## Use Cases

- Traitement automatique du langage naturel (TALN)
- Traduction automatique
- Classification d'images avec des Transformateurs Visuels (ViT)

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

- [Scaled Dot-Product Attention (Attention produit scalaire mis à l'échelle)](/en/terms/scaled-dot-product-attention-attention-produit-scalaire-mis-à-l-échelle/)
- [Transformer (Transformateur)](/en/terms/transformer-transformateur/)
- [Embedding (Encodage vectoriel / Embedding)](/en/terms/embedding-encodage-vectoriel-embedding/)
