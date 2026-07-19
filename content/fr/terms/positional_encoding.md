---
title: Encodage Positionnel
term_id: positional_encoding
category: basic_concepts
subcategory: ''
tags:
- transformers
- NLP
- architecture
difficulty: 3
weight: 1
slug: positional_encoding
date: '2026-07-18T11:00:53.340751Z'
lastmod: '2026-07-18T11:44:45.187197Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Une technique qui injecte des informations sur la position relative ou
  absolue des tokens dans une séquence au sein des modèles de type transformer.
---
## Definition

Étant donné que les transformateurs traitent tous les tokens en parallèle plutôt que séquentiellement comme les RNN, ils dépourvus de connaissance intrinsèque de l'ordre des tokens. L'encodage positionnel ajoute des vecteurs spécifiques aux embeddings d'entrée pour préserver l'ordre séquentiel.

### Summary

Une technique qui injecte des informations sur la position relative ou absolue des tokens dans une séquence au sein des modèles de type transformer.

## Key Concepts

- Ordre de la Séquence
- Auto-attention
- Fonctions Sinusoïdales
- Embeddings de Tokens

## Use Cases

- Traduction Automatique
- Résumé de Texte
- Modélisation du Langage

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Architecture Transformer](/en/terms/architecture-transformer/)
- [Embedding (Représentation vectorielle)](/en/terms/embedding-représentation-vectorielle/)
- [Mécanisme d'Attention](/en/terms/mécanisme-d-attention/)
- [RoPE (Rotary Positional Embedding)](/en/terms/rope-rotary-positional-embedding/)
