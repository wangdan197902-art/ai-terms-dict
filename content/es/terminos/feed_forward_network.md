---
title: "Red de alimentación directa"
term_id: "feed_forward_network"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "architecture", "fundamentals"]
difficulty: 2
weight: 1
slug: "feed_forward_network"
aliases:
  - /es/terms/feed_forward_network/
date: "2026-07-18T10:49:18.358296Z"
lastmod: "2026-07-18T11:44:44.806815Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Una clase de red neuronal artificial donde las conexiones entre nodos no forman ciclos, propagando la información en una sola dirección."
---

## Definition

Las Redes de Alimentación Directa (FFN), también conocidas como Perceptrones Multicapa (MLP), procesan los datos secuencialmente a través de capas de neuronas desde la entrada hasta la salida, sin bucles de retroalimentación. Cada neurona recibe entradas

### Summary

Una clase de red neuronal artificial donde las conexiones entre nodos no forman ciclos, propagando la información en una sola dirección.

## Key Concepts

- Sin ciclos
- Capas (Entrada, Oculta, Salida)
- Funciones de activación
- Sumas ponderadas

## Use Cases

- Tareas simples de regresión
- Problemas de clasificación con datos tabulares
- Bloques de construcción para arquitecturas más profundas

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron (Perceptrón multicapa)](/en/terms/multi-layer-perceptron-perceptrón-multicapa/)
- [Backpropagation (Propagación hacia atrás)](/en/terms/backpropagation-propagación-hacia-atrás/)
- [Activation Function (Función de activación)](/en/terms/activation-function-función-de-activación/)
- [Neural Network (Red neuronal)](/en/terms/neural-network-red-neuronal/)
