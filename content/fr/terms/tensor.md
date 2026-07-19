---
title: Tenseur
term_id: tensor
category: basic_concepts
subcategory: ''
tags:
- math
- Data Structures
- pytorch
difficulty: 2
weight: 1
slug: tensor
date: '2026-07-18T11:40:38.243086Z'
lastmod: '2026-07-18T11:44:45.343737Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Un tableau multidimensionnel qui sert de structure de données fondamentale
  pour les frameworks d'apprentissage profond.
---
## Definition

En informatique et en apprentissage profond, un tenseur est un objet mathématique qui généralise les scalaires, les vecteurs et les matrices à des dimensions supérieures. Il est caractérisé par son rang (nombre de dimensions) et sa forme.

### Summary

Un tableau multidimensionnel qui sert de structure de données fondamentale pour les frameworks d'apprentissage profond.

## Key Concepts

- Rang
- Forme
- Dimensionnalité
- Diffusion (Broadcasting)

## Use Cases

- Traitement d'images (tenseurs 4D)
- Stockage des poids des réseaux neuronaux
- Entrée de données par lots

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix (Matrice)](/en/terms/matrix-matrice/)
- [Vector (Vecteur)](/en/terms/vector-vecteur/)
- [Deep Learning (Apprentissage profond)](/en/terms/deep-learning-apprentissage-profond/)
- [NumPy (Bibliothèque Python pour le calcul scientifique)](/en/terms/numpy-bibliothèque-python-pour-le-calcul-scientifique/)
