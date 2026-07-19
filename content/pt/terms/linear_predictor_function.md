---
title: Função preditora linear
term_id: linear_predictor_function
category: basic_concepts
subcategory: ''
tags:
- statistics
- Linear Models
- mathematics
difficulty: 2
weight: 1
slug: linear_predictor_function
date: '2026-07-18T15:08:20.668453Z'
lastmod: '2026-07-18T15:51:59.507746Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Uma função matemática que calcula uma combinação linear de variáveis
  de entrada para prever um resultado.
---
## Definition

Em modelagem estatística e aprendizado de máquina, uma função preditora linear representa a soma ponderada das características de entrada mais um termo de viés. Ela serve como componente central em modelos lineares generalizados (GLMs).

### Summary

Uma função matemática que calcula uma combinação linear de variáveis de entrada para prever um resultado.

## Key Concepts

- Soma Ponderada
- Termo de Viés
- Modelos Lineares Generalizados
- Coeficientes de Características

## Use Cases

- Análise de regressão linear
- Classificação por regressão logística
- Máquinas de Vetores de Suporte (no contexto do truque do kernel)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (coeficientes de regressão)](/en/terms/regression_coefficients-coeficientes-de-regressão/)
- [bias_intercept (intercepto/viés)](/en/terms/bias_intercept-intercepto-viés/)
- [feature_engineering (engenharia de características)](/en/terms/feature_engineering-engenharia-de-características/)
- [generalized_linear_model (modelo linear generalizado)](/en/terms/generalized_linear_model-modelo-linear-generalizado/)
