---
title: Coeficiente Phi
term_id: phi_coefficient
category: basic_concepts
subcategory: ''
tags:
- statistics
- Evaluation Metrics
- Binary Classification
difficulty: 3
weight: 1
slug: phi_coefficient
date: '2026-07-18T11:04:04.178982Z'
lastmod: '2026-07-18T11:44:44.843042Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una medida estadística de asociación entre dos variables binarias.
---
## Definition

El coeficiente Phi (φ) es una medida de asociación para dos variables binarias, que funciona como el coeficiente de correlación de Pearson para variables dicotómicas. Varía entre -1 y +1, donde 0 indica ausencia de asociación.

### Summary

Una medida estadística de asociación entre dos variables binarias.

## Key Concepts

- Variables binarias
- Correlación
- Tabla de contingencia
- Intensidad de la asociación

## Use Cases

- Evaluación del rendimiento de clasificadores binarios más allá de la precisión
- Análisis de relaciones en datos de encuestas con respuestas sí/no
- Selección de características en conjuntos de datos con entradas categóricas

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [V de Cramér (medida de asociación para tablas de contingencia)](/en/terms/v-de-cramér-medida-de-asociación-para-tablas-de-contingencia/)
- [Correlación de Pearson (medida de relación lineal)](/en/terms/correlación-de-pearson-medida-de-relación-lineal/)
- [Matriz de confusión (tabla para evaluar rendimiento de clasificación)](/en/terms/matriz-de-confusión-tabla-para-evaluar-rendimiento-de-clasificación/)
- [Información mutua (medida de dependencia estadística)](/en/terms/información-mutua-medida-de-dependencia-estadística/)
