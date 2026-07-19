---
title: Matriz de confusión
term_id: confusion_matrix
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Classification
- metrics
difficulty: 2
weight: 1
slug: confusion_matrix
date: '2026-07-18T10:40:46.659143Z'
lastmod: '2026-07-18T11:44:44.788376Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una tabla utilizada para describir el rendimiento de un modelo de clasificación
  en un conjunto de datos de prueba.
---
## Definition

Una matriz de confusión es una disposición tabular específica que permite visualizar el rendimiento de un algoritmo, típicamente uno de aprendizaje supervisado. Muestra los conteos de verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos, facilitando la evaluación de la precisión y el recall del modelo.

### Summary

Una tabla utilizada para describir el rendimiento de un modelo de clasificación en un conjunto de datos de prueba.

## Key Concepts

- Verdaderos Positivos
- Falsos Negativos
- Precisión
- Exhaustividad (Recall)

## Use Cases

- Evaluación de clasificadores binarios
- Análisis del rendimiento en clasificación multiclase
- Depuración de sesgos del modelo en conjuntos de datos desbalanceados

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (precisión)](/en/terms/precision-precisión/)
- [recall (exhaustividad o recall)](/en/terms/recall-exhaustividad-o-recall/)
- [F1 score (puntuación F1)](/en/terms/f1-score-puntuación-f1/)
- [ROC curve (curva ROC)](/en/terms/roc-curve-curva-roc/)
