---
title: Capa Oculta
term_id: hidden_layer
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- Deep Learning
difficulty: 3
weight: 1
slug: hidden_layer
date: '2026-07-18T10:53:08.479768Z'
lastmod: '2026-07-18T11:44:44.814987Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una capa intermedia en una red neuronal entre las capas de entrada y
  salida que procesa características.
---
## Definition

Una capa oculta consiste en neuronas que reciben entradas de capas anteriores, aplican pesos y sesgos, y transmiten datos transformados hacia adelante a través de una función de activación. Estas capas permiten a las redes neuronales aprender representaciones complejas y no lineales de los datos.

### Summary

Una capa intermedia en una red neuronal entre las capas de entrada y salida que procesa características.

## Key Concepts

- Redes Neuronales
- Extracción de Características
- Funciones de Activación
- Aprendizaje Profundo

## Use Cases

- Sistemas de reconocimiento de imágenes
- Modelos de procesamiento de lenguaje natural
- Analítica predictiva

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron (neurona)](/en/terms/neuron-neurona/)
- [backpropagation (retropropagación)](/en/terms/backpropagation-retropropagación/)
- [activation_function (función de activación)](/en/terms/activation_function-función-de-activación/)
- [deep_learning (aprendizaje profundo)](/en/terms/deep_learning-aprendizaje-profundo/)
