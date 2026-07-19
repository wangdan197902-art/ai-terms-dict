---
title: Tanh
term_id: tanh
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- mathematics
difficulty: 2
weight: 1
slug: tanh
date: '2026-07-18T16:19:51.743829Z'
lastmod: '2026-07-18T17:15:08.922809Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Tanh, czyli tangens hiperboliczny, to funkcja aktywacji mapująca wartości
  wejściowe na zakres między -1 a 1.
---
## Definition

Funkcja tangensa hiperbolicznego (Tanh) to nieliniowa funkcja aktywacji powszechnie stosowana w sieciach neuronowych. Obcina wartości wejściowe do przedziału (-1, 1), zapewniając wyjścia wycentrowane wokół zera, co sprzyja...

### Summary

Tanh, czyli tangens hiperboliczny, to funkcja aktywacji mapująca wartości wejściowe na zakres między -1 a 1.

## Key Concepts

- Funkcja aktywacji
- Nieliniowość
- Wyjście wycentrowane wokół zera
- Backpropagation (propagacja zwrotna)

## Use Cases

- Rekurencyjne sieci neuronowe
- Bramki komórek LSTM
- Warstwy ukryte w perceptronach wielowarstwowych (MLP)

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (funkcja sigmoidalna)](/en/terms/sigmoid-funkcja-sigmoidalna/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (sieci neuronowe)](/en/terms/neural_networks-sieci-neuronowe/)
