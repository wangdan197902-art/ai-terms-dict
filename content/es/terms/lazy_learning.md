---
title: Aprendizaje perezoso
term_id: lazy_learning
category: training_techniques
subcategory: ''
tags:
- algorithms
- Training Methods
- Machine Learning
difficulty: 2
weight: 1
slug: lazy_learning
date: '2026-07-18T10:57:10.137065Z'
lastmod: '2026-07-18T11:44:44.824859Z'
draft: false
source: agnes_llm
status: published
language: es
description: Un enfoque de aprendizaje que retrasa la generalización hasta el momento
  de la clasificación, almacenando instancias de entrenamiento en lugar de construir
  un modelo explícito.
---
## Definition

Los aprendices perezosos, como los k-Vecinos Más Cercanos (k-NN), memorizan todo el conjunto de datos de entrenamiento y realizan cálculos únicamente al hacer predicciones. Esto contrasta con el aprendizaje ansioso, que construye un modelo generalizado antes de ver datos nuevos.

### Summary

Un enfoque de aprendizaje que retrasa la generalización hasta el momento de la clasificación, almacenando instancias de entrenamiento en lugar de construir un modelo explícito.

## Key Concepts

- Aprendizaje basado en instancias
- k-Vecinos Más Cercanos
- Costo de inferencia
- Generalización

## Use Cases

- Sistemas de recomendación
- Reconocimiento de patrones en conjuntos de datos pequeños
- Prototipado de modelos predictivos

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)
```

## Related Terms

- [instance_based_learning (aprendizaje basado en instancias)](/en/terms/instance_based_learning-aprendizaje-basado-en-instancias/)
- [knn (k-NN)](/en/terms/knn-k-nn/)
- [eager_learning (aprendizaje ansioso)](/en/terms/eager_learning-aprendizaje-ansioso/)
- [generalization (generalización)](/en/terms/generalization-generalización/)
