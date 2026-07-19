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
date: '2026-07-18T16:20:56.700917Z'
lastmod: '2026-07-18T17:15:09.336024Z'
draft: false
source: agnes_llm
status: published
language: da
description: Tanh, eller hyperbolsk tangens, er en aktiveringsfunktion, der kortlægger
  inputværdier til et interval mellem -1 og 1.
---
## Definition

Funktionen for hyperbolsk tangens (Tanh) er en ikke-lineær aktiveringsfunktion, der almindeligvis bruges i neurale netværk. Den komprimerer inputværdier ind i intervallet (-1, 1) og giver nul-centrerede output, hvilket

### Summary

Tanh, eller hyperbolsk tangens, er en aktiveringsfunktion, der kortlægger inputværdier til et interval mellem -1 og 1.

## Key Concepts

- Aktiveringsfunktion
- Ikke-linearitet
- Nul-centreret output
- Bagudpropagering

## Use Cases

- Rekurrente neurale netværk
- LSTM-celleporte
- Skjulte lag i MLP'er

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (sigmoid-funktion)](/en/terms/sigmoid-sigmoid-funktion/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (neurale netværk)](/en/terms/neural_networks-neurale-netværk/)
