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
date: '2026-07-18T11:35:22.958123Z'
lastmod: '2026-07-18T11:44:44.991384Z'
draft: false
source: agnes_llm
status: published
language: de
description: Tanh, oder Hyperbolischer Tangens, ist eine Aktivierungsfunktion, die
  Eingabewerte auf einen Bereich zwischen -1 und 1 abbildet.
---
## Definition

Die hyperbolische Tangens-Funktion (Tanh) ist eine nichtlineare Aktivierungsfunktion, die häufig in neuronalen Netzen verwendet wird. Sie komprimiert Eingabewerte in das Intervall (-1, 1) und bietet nullzentrierte Ausgaben, was...

### Summary

Tanh, oder Hyperbolischer Tangens, ist eine Aktivierungsfunktion, die Eingabewerte auf einen Bereich zwischen -1 und 1 abbildet.

## Key Concepts

- Aktivierungsfunktion
- Nichtlinearität
- Nullzentrierte Ausgabe
- Backpropagation

## Use Cases

- Rekurrente neuronale Netze
- LSTM-Zellgatter
- Versteckte Schichten in MLPs

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (Sigmoid-Funktion)](/en/terms/sigmoid-sigmoid-funktion/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (Neuronale Netze)](/en/terms/neural_networks-neuronale-netze/)
