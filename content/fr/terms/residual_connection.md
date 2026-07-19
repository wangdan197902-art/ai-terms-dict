---
title: Connexion résiduelle
term_id: residual_connection
category: basic_concepts
subcategory: ''
tags:
- architecture
- Optimization
- Deep Learning
difficulty: 3
weight: 1
slug: residual_connection
date: '2026-07-18T11:01:25.132000Z'
lastmod: '2026-07-18T11:44:45.188460Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Un mécanisme qui ajoute l'entrée directement à la sortie d'une couche
  pour faciliter le flux de gradient dans les réseaux profonds.
---
## Definition

Les connexions résiduelles, également appelées connexions saut (skip connections), permettent aux gradients de circuler à travers un réseau en ajoutant directement une entrée à la sortie d'une couche ultérieure. Cette architecture résout le problème du gradient disparaissant (vanishing gradient problem) en préservant l'information tout au long du réseau.

### Summary

Un mécanisme qui ajoute l'entrée directement à la sortie d'une couche pour faciliter le flux de gradient dans les réseaux profonds.

## Key Concepts

- Connexions saut
- Problème du gradient disparaissant
- Apprentissage résiduel profond
- Flux de gradient

## Use Cases

- Entraînement de réseaux de neurones convolutifs profonds
- Architectures de type Transformer
- Modèles de classification d'images

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (connexion saut)](/en/terms/skip_connection-connexion-saut/)
- [vanishing_gradient (gradient disparaissant)](/en/terms/vanishing_gradient-gradient-disparaissant/)
- [deep_learning (apprentissage profond)](/en/terms/deep_learning-apprentissage-profond/)
- [resnet (réseau résiduel)](/en/terms/resnet-réseau-résiduel/)
