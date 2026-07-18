---
title: "Función de predictor lineal"
term_id: "linear_predictor_function"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "linear_models", "mathematics"]
difficulty: 2
weight: 1
slug: "linear_predictor_function"
aliases:
  - /es/terms/linear_predictor_function/
date: "2026-07-18T10:57:52.028833Z"
lastmod: "2026-07-18T11:44:44.826222Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Una función matemática que calcula una combinación lineal de variables de entrada para predecir un resultado."
---

## Definition

En el modelado estadístico y el aprendizaje automático, una función de predictor lineal representa la suma ponderada de las características de entrada más un término de sesgo. Sirve como componente central en los modelos lineales generalizados (GLM).

### Summary

Una función matemática que calcula una combinación lineal de variables de entrada para predecir un resultado.

## Key Concepts

- Suma ponderada
- Término de sesgo
- Modelos lineales generalizados
- Coeficientes de características

## Use Cases

- Análisis de regresión lineal
- Clasificación por regresión logística
- Máquinas de vectores de soporte (en el contexto del truco del núcleo)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (coeficientes de regresión)](/en/terms/regression_coefficients-coeficientes-de-regresión/)
- [bias_intercept (intercepto de sesgo)](/en/terms/bias_intercept-intercepto-de-sesgo/)
- [feature_engineering (ingeniería de características)](/en/terms/feature_engineering-ingeniería-de-características/)
- [generalized_linear_model (modelo lineal generalizado)](/en/terms/generalized_linear_model-modelo-lineal-generalizado/)
