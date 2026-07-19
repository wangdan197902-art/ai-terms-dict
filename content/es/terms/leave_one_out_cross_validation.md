---
title: Validación cruzada de un solo elemento
term_id: leave_one_out_cross_validation
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- evaluation
- statistics
difficulty: 3
weight: 1
slug: leave_one_out_cross_validation
date: '2026-07-18T10:57:37.952519Z'
lastmod: '2026-07-18T11:44:44.825546Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una técnica rigurosa de remuestreo en la que el modelo se entrena con
  todos los datos excepto uno y se prueba con esa única muestra retenida, repitiendo
  el proceso para cada punto de datos.
---
## Definition

La validación cruzada de un solo elemento (LOOCV, por sus siglas en inglés) es un caso específico de la validación cruzada k-fold donde k es igual al número de muestras en el conjunto de datos. Proporciona una estimación casi insesgada del rendimiento del modelo, siendo particularmente útil cuando los datos son limitados, aunque implica un alto costo computacional debido a la necesidad de entrenar el modelo tantas veces como puntos de datos existan.

### Summary

Una técnica rigurosa de remuestreo en la que el modelo se entrena con todos los datos excepto uno y se prueba con esa única muestra retenida, repitiendo el proceso para cada punto de datos.

## Key Concepts

- Remuestreo
- Evaluación de modelos
- Compromiso sesgo-varianza
- Coste computacional

## Use Cases

- Evaluación de modelos en conjuntos de datos médicos pequeños
- Ajuste de hiperparámetros cuando los datos son escasos
- Comparación rigurosa del rendimiento de algoritmos

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [validación cruzada k-fold (técnica generalizada de remuestreo)](/en/terms/validación-cruzada-k-fold-técnica-generalizada-de-remuestreo/)
- [división entrenamiento-prueba (separación básica de datos)](/en/terms/división-entrenamiento-prueba-separación-básica-de-datos/)
- [bootstrapping (remuestreo con reemplazo)](/en/terms/bootstrapping-remuestreo-con-reemplazo/)
- [puntuación de validación cruzada (métrica de evaluación)](/en/terms/puntuación-de-validación-cruzada-métrica-de-evaluación/)
