---
title: "Auto-attention"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /fr/terms/self_attention/
date: "2026-07-18T10:54:03.659544Z"
lastmod: "2026-07-18T11:44:45.172557Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Un mécanisme permettant à un réseau de neurones de pondérer l'importance des différentes parties de la séquence d'entrée par rapport aux autres."
---

## Definition

L'auto-attention permet aux modèles de capturer les dépendances entre toutes les positions d'une séquence simultanément, quelle que soit la distance. En calculant les scores d'attention entre chaque paire de jetons, elle permet une prise en compte globale du contexte.

### Summary

Un mécanisme permettant à un réseau de neurones de pondérer l'importance des différentes parties de la séquence d'entrée par rapport aux autres.

## Key Concepts

- Requête-Clé-Valeur
- Scores d'attention
- Pondération contextuelle
- Traitement parallèle

## Use Cases

- Traduction automatique
- Résumé de texte
- Classification d'images via les Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Transformateur)](/en/terms/transformer-transformateur/)
- [Multi-Head Attention (Attention multi-têtes)](/en/terms/multi-head-attention-attention-multi-têtes/)
- [Embeddings (Plongements vectoriels)](/en/terms/embeddings-plongements-vectoriels/)
- [Sequence Modeling (Modélisation de séquences)](/en/terms/sequence-modeling-modélisation-de-séquences/)
