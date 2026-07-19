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
date: '2026-07-18T10:31:53.811693Z'
lastmod: '2026-07-18T11:44:44.766031Z'
draft: false
source: agnes_llm
status: published
language: es
description: La unidad lineal rectificada es una función de activación que devuelve
  la entrada directamente si es positiva, o cero en caso contrario.
---
## Definition

ReLU se utiliza ampliamente en redes neuronales de aprendizaje profundo debido a su eficiencia computacional y capacidad para mitigar el problema del gradiente desvanecido. Definida matemáticamente como f(x) = max(0, x), introduce

### Summary

La unidad lineal rectificada es una función de activación que devuelve la entrada directamente si es positiva, o cero en caso contrario.

## Key Concepts

- No linealidad
- Función de activación
- Gradiente desvanecido
- Lineal a trozos

## Use Cases

- Capas ocultas en CNN
- Redes feedforward profundas
- Modelos de reconocimiento de imágenes

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (Función sigmoidea)](/en/terms/sigmoid-función-sigmoidea/)
- [Tanh (Función tangente hiperbólica)](/en/terms/tanh-función-tangente-hiperbólica/)
- [Leaky ReLU (ReLU filtrante)](/en/terms/leaky-relu-relu-filtrante/)
- [Neural Network (Red neuronal)](/en/terms/neural-network-red-neuronal/)
