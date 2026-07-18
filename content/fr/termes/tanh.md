---
title: "Tanh"
term_id: "tanh"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "mathematics"]
difficulty: 2
weight: 1
slug: "tanh"
aliases:
  - /fr/terms/tanh/
date: "2026-07-18T11:40:25.127743Z"
lastmod: "2026-07-18T11:44:45.343250Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Tanh, ou tangente hyperbolique, est une fonction d'activation qui mappe les valeurs d'entrée sur une plage comprise entre -1 et 1."
---

## Definition

La fonction tangente hyperbolique (Tanh) est une fonction d'activation non linéaire couramment utilisée dans les réseaux de neurones. Elle comprime les valeurs d'entrée dans l'intervalle (-1, 1), fournissant des sorties centrées sur zéro ce qui

### Summary

Tanh, ou tangente hyperbolique, est une fonction d'activation qui mappe les valeurs d'entrée sur une plage comprise entre -1 et 1.

## Key Concepts

- Fonction d'activation
- Non-linéarité
- Sortie centrée sur zéro
- Rétropropagation

## Use Cases

- Réseaux de neurones récurrents
- Portes des cellules LSTM
- Couches cachées dans les MLP

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (Sigmoïde)](/en/terms/sigmoid-sigmoïde/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (Réseaux de neurones)](/en/terms/neural_networks-réseaux-de-neurones/)
