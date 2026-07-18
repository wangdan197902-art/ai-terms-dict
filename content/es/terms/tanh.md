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
  - /es/terms/tanh/
date: "2026-07-18T11:09:37.070983Z"
lastmod: "2026-07-18T11:44:44.859394Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Tanh, o tangente hiperbólica, es una función de activación que mapea los valores de entrada a un rango entre -1 y 1."
---

## Definition

La función tangente hiperbólica (Tanh) es una función de activación no lineal comúnmente utilizada en redes neuronales. Comprime los valores de entrada en el intervalo (-1, 1), proporcionando salidas centradas en cero que

### Summary

Tanh, o tangente hiperbólica, es una función de activación que mapea los valores de entrada a un rango entre -1 y 1.

## Key Concepts

- Función de activación
- No linealidad
- Salida centrada en cero
- Propagación hacia atrás

## Use Cases

- Redes neuronales recurrentes
- Compuertas de celdas LSTM
- Capas ocultas en MLPs

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (sigmoide)](/en/terms/sigmoid-sigmoide/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (redes neuronales)](/en/terms/neural_networks-redes-neuronales/)
