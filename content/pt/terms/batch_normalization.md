---
title: Normalização em Lote
term_id: batch_normalization
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- Optimization
- Neural Networks
difficulty: 3
weight: 1
slug: batch_normalization
date: '2026-07-18T14:51:20.538270Z'
lastmod: '2026-07-18T15:51:59.467275Z'
draft: false
source: agnes_llm
status: published
language: pt
description: A normalização em lote é uma técnica que normaliza as entradas de uma
  camada ao longo de um mini-lote para estabilizar e acelerar o treinamento de redes
  neurais.
---
## Definition

Este método ajusta e escala as ativações para terem média zero e variância unitária dentro de cada mini-lote durante o treinamento. Ele reduz o deslocamento de covariância interna, permitindo taxas de aprendizado mais altas e convergência mais rápida, além de atuar como um regularizador leve.

### Summary

A normalização em lote é uma técnica que normaliza as entradas de uma camada ao longo de um mini-lote para estabilizar e acelerar o treinamento de redes neurais.

## Key Concepts

- Deslocamento de covariância interna
- Estatísticas de mini-lote
- Estabilização de gradiente
- Efeito de regularização

## Use Cases

- Redes Neurais Profundas
- Redes Neurais Convolucionais
- Otimização de treinamento

## Code Example

```python
import torch.nn as nn
layer = nn.Sequential(
    nn.Linear(10, 20),
    nn.BatchNorm1d(20),
    nn.ReLU()
)
```

## Related Terms

- [Layer Normalization (Normalização de Camada)](/en/terms/layer-normalization-normalização-de-camada/)
- [Gradient Descent (Descida do Gradiente)](/en/terms/gradient-descent-descida-do-gradiente/)
- [Overfitting (Sobreajuste)](/en/terms/overfitting-sobreajuste/)
