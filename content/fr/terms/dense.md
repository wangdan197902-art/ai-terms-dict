---
title: "Dense"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /fr/terms/dense/
date: "2026-07-18T11:13:22.888286Z"
lastmod: "2026-07-18T11:44:45.241872Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Une couche ou un tenseur où chaque élément est connecté à tous les éléments de la couche ou de la dimension précédente."
---

## Definition

Dans les réseaux de neurones, le terme 'dense' désigne des couches entièrement connectées où chaque neurone reçoit l'entrée de tous les neurones de la couche précédente. Cela contraste avec les connexions clairsemées présentes dans les réseaux convolutifs ou...

### Summary

Une couche ou un tenseur où chaque élément est connecté à tous les éléments de la couche ou de la dimension précédente.

## Key Concepts

- Entièrement connecté
- Matrice de poids
- Fonction d'activation
- Intégration des caractéristiques

## Use Cases

- Couches de classification finale dans les perceptrons multicouches (MLP)
- Fusion de caractéristiques dans les modèles hybrides
- Tâches de régression simples

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Réseau de neurones feedforward (Réseau neuronal à propagation avant)](/en/terms/réseau-de-neurones-feedforward-réseau-neuronal-à-propagation-avant/)
- [Rétropropagation](/en/terms/rétropropagation/)
- [ReLU (Unité linéaire rectifiée)](/en/terms/relu-unité-linéaire-rectifiée/)
- [Terme de biais](/en/terms/terme-de-biais/)
