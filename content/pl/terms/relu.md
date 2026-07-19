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
date: '2026-07-18T15:36:47.657496Z'
lastmod: '2026-07-18T17:15:08.836238Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Funkcja Rectified Linear Unit (ReLU) to funkcja aktywacji, która zwraca
  wartość wejściową bezpośrednio, jeśli jest dodatnia, w przeciwnym razie zwraca zero.
---
## Definition

ReLU jest szeroko stosowana w sieciach neuronowych uczenia głębokiego ze względu na swoją efektywność obliczeniową oraz zdolność do łagodzenia problemu zanikającego gradientu. Zdefiniowana matematycznie jako f(x) = max(0, x), wprowadza nieliniowość, pozwalając sieciom na naukę złożonych wzorców.

### Summary

Funkcja Rectified Linear Unit (ReLU) to funkcja aktywacji, która zwraca wartość wejściową bezpośrednio, jeśli jest dodatnia, w przeciwnym razie zwraca zero.

## Key Concepts

- Nieliniowość
- Funkcja aktywacji
- Problem zanikającego gradientu
- Liniowość kawałkami

## Use Cases

- Warstwy ukryte w sieciach CNN
- Głębokie sieci feedforward
- Modele rozpoznawania obrazu

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (funkcja aktywacji)](/en/terms/sigmoid-funkcja-aktywacji/)
- [Tanh (funkcja hiperboliczna)](/en/terms/tanh-funkcja-hiperboliczna/)
- [Leaky ReLU (wariacja ReLU)](/en/terms/leaky-relu-wariacja-relu/)
- [Sieć neuronowa (model uczenia maszynowego)](/en/terms/sieć-neuronowa-model-uczenia-maszynowego/)
