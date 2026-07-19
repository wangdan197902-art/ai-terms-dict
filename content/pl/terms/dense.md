---
title: Gęsta warstwa
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:51:34.743068Z'
lastmod: '2026-07-18T17:15:08.865791Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Warstwa lub tensor, w którym każdy element jest połączony z każdym elementem
  poprzedniej warstwy lub wymiaru.
---
## Definition

W sieciach neuronowych termin 'gęsty' odnosi się do warstw w pełni połączonych, w których każdy neuron otrzymuje wejście od wszystkich neuronów w poprzedniej warstwie. Stanowi to kontrast względem rzadkich połączeń występujących w sieciach konwolucyjnych lub innych architekturach rozproszonych.

### Summary

Warstwa lub tensor, w którym każdy element jest połączony z każdym elementem poprzedniej warstwy lub wymiaru.

## Key Concepts

- W pełni połączone
- Macierz wag
- Funkcja aktywacji
- Integracja cech

## Use Cases

- Końcowe warstwy klasyfikacyjne w wielowarstwowych perceptronach (MLP)
- Fuzja cech w modelach hybrydowych
- Proste zadania regresji

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Sieć neuronowa feedforward / prosta)](/en/terms/feedforward-neural-network-sieć-neuronowa-feedforward-prosta/)
- [Backpropagation (Algorytm propagacji zwrotnej)](/en/terms/backpropagation-algorytm-propagacji-zwrotnej/)
- [ReLU (Funkcja aktywacji ReLU)](/en/terms/relu-funkcja-aktywacji-relu/)
- [Bias Term (Składnik bias / przesunięcie)](/en/terms/bias-term-składnik-bias-przesunięcie/)
