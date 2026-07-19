---
title: Modelo sustituto
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T11:09:24.296461Z'
lastmod: '2026-07-18T11:44:44.858584Z'
draft: false
source: agnes_llm
status: published
language: es
description: Un modelo matemático simplificado utilizado para aproximar el comportamiento
  de un modelo más complejo, computacionalmente costoso o inaccesible.
---
## Definition

En aprendizaje automático y optimización, un modelo sustituto actúa como un proxy para una función objetivo que es difícil de evaluar directamente. Se entrena con pares entrada-salida del modelo original para aproximar su comportamiento.

### Summary

Un modelo matemático simplificado utilizado para aproximar el comportamiento de un modelo más complejo, computacionalmente costoso o inaccesible.

## Key Concepts

- Aproximación de modelos
- Optimización de caja negra
- Eficiencia computacional
- Modelo proxy

## Use Cases

- Optimización de hiperparámetros
- Aceleración de simulaciones en diseño de ingeniería
- Análisis de sensibilidad de sistemas complejos

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Optimización bayesiana](/en/terms/optimización-bayesiana/)
- [Proceso gaussiano](/en/terms/proceso-gaussiano/)
- [Función de caja negra](/en/terms/función-de-caja-negra/)
- [Emulador](/en/terms/emulador/)
