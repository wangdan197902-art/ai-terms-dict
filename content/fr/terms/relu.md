---
title: ReLU
term_id: relu
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Activation Functions
- Deep Learning
difficulty: 3
weight: 1
slug: relu
date: '2026-07-18T11:01:10.305795Z'
lastmod: '2026-07-18T11:44:45.188091Z'
draft: false
source: agnes_llm
status: published
language: fr
description: L'unité linéaire rectifiée (ReLU) est une fonction d'activation qui renvoie
  l'entrée directement si elle est positive, sinon zéro.
---
## Definition

La ReLU est largement utilisée dans les réseaux neuronaux profonds en raison de son efficacité computationnelle et de sa capacité à atténuer le problème du gradient disparaissant. Définie mathématiquement par f(x) = max(0, x), elle introduit de la non-linéarité tout en restant simple à calculer.

### Summary

L'unité linéaire rectifiée (ReLU) est une fonction d'activation qui renvoie l'entrée directement si elle est positive, sinon zéro.

## Key Concepts

- Non-linéarité
- Fonction d'activation
- Gradient disparaissant
- Pièce linéaire

## Use Cases

- Couches cachées dans les CNN
- Réseaux feedforward profonds
- Modèles de reconnaissance d'images

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid](/en/terms/sigmoid/)
- [Tanh](/en/terms/tanh/)
- [Leaky ReLU](/en/terms/leaky-relu/)
- [Réseau neuronal](/en/terms/réseau-neuronal/)
