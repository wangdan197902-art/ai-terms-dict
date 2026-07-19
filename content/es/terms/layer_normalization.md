---
title: Normalización por capa
term_id: layer_normalization
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Optimization
- architecture
difficulty: 3
weight: 1
slug: layer_normalization
date: '2026-07-18T10:57:10.137058Z'
lastmod: '2026-07-18T11:44:44.824744Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una técnica que normaliza las activaciones de una capa de red neuronal
  a lo largo de la dimensión de características para cada muestra individual.
---
## Definition

La normalización por capa estabiliza el entrenamiento reduciendo el desplazamiento de covarianza interno, siendo particularmente efectiva en arquitecturas recurrentes y transformadoras. A diferencia de la normalización por lotes, que depende de las estadísticas del lote, esta funciona independientemente del tamaño del mismo.

### Summary

Una técnica que normaliza las activaciones de una capa de red neuronal a lo largo de la dimensión de características para cada muestra individual.

## Key Concepts

- Normalización
- Desplazamiento de covarianza interno
- Modelos transformadores
- RNNs

## Use Cases

- Entrenamiento de modelos Transformadores como BERT
- Estabilización del entrenamiento de RNN/LSTM
- Aprendizaje profundo con tamaños de lote pequeños

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization (normalización por lotes)](/en/terms/batch_normalization-normalización-por-lotes/)
- [transformer (transformador)](/en/terms/transformer-transformador/)
- [normalization (normalización)](/en/terms/normalization-normalización/)
- [deep_learning (aprendizaje profundo)](/en/terms/deep_learning-aprendizaje-profundo/)
