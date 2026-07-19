---
title: Softmax
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T10:32:20.236370Z'
lastmod: '2026-07-18T11:44:44.767137Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una función matemática que convierte un vector de puntuaciones reales
  arbitrarias en una distribución de probabilidad.
---
## Definition

Softmax se utiliza ampliamente en la capa de salida de las redes neuronales para tareas de clasificación multiclase. Toma un vector de logit sin procesar y los normaliza de modo que cada elemento represente una probabilidad de pertenecer a esa clase.

### Summary

Una función matemática que convierte un vector de puntuaciones reales arbitrarias en una distribución de probabilidad.

## Key Concepts

- Distribución de Probabilidad
- Logit
- Normalización
- Clasificación Multiclase

## Use Cases

- Capas de salida de clasificación de imágenes
- Predicción de tokens en modelos de lenguaje
- Categorización multietiqueta

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (Función que devuelve el índice del valor máximo)](/en/terms/argmax-función-que-devuelve-el-índice-del-valor-máximo/)
- [Pérdida de Entropía Cruzada (Función de costo común)](/en/terms/pérdida-de-entropía-cruzada-función-de-costo-común/)
- [Logit (Salida cruda antes de la activación)](/en/terms/logit-salida-cruda-antes-de-la-activación/)
- [Red Neuronal (Arquitectura de modelo)](/en/terms/red-neuronal-arquitectura-de-modelo/)
