---
title: "Evaluación de clasificadores binarios"
term_id: "evaluation_of_binary_classifiers"
category: "basic_concepts"
subcategory: ""
tags: ["metrics", "classification", "evaluation"]
difficulty: 2
weight: 1
slug: "evaluation_of_binary_classifiers"
aliases:
  - /es/terms/evaluation_of_binary_classifiers/
date: "2026-07-18T10:48:37.407757Z"
lastmod: "2026-07-18T11:44:44.803514Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "El proceso de evaluar el rendimiento de los modelos de aprendizaje automático que predicen uno de dos resultados posibles."
---

## Definition

Este campo implica analizar métricas como la precisión global (accuracy), la precisión (precision), el recall, la puntuación F1 y el Área Bajo la Curva Característica Operativa del Receptor (AUC-ROC). Ayuda a determinar qué tan bien un modelo distingue entre clases.

### Summary

El proceso de evaluar el rendimiento de los modelos de aprendizaje automático que predicen uno de dos resultados posibles.

## Key Concepts

- Matriz de confusión
- Compromiso precisión-recall
- Curva ROC
- Puntuación F1

## Use Cases

- Tamizaje médico de enfermedades
- Filtrado de correo no deseado
- Evaluación del riesgo crediticio

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (matriz de confusión)](/en/terms/confusion_matrix-matriz-de-confusión/)
- [roc_auc (área bajo la curva ROC)](/en/terms/roc_auc-área-bajo-la-curva-roc/)
- [precision_recall (precisión y recall)](/en/terms/precision_recall-precisión-y-recall/)
- [cross_validation (validación cruzada)](/en/terms/cross_validation-validación-cruzada/)
