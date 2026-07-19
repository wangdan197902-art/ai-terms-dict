---
title: Funcție de predicție liniară
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
date: '2026-07-18T16:09:05.636607Z'
lastmod: '2026-07-18T17:15:09.675275Z'
draft: false
source: agnes_llm
status: published
language: ro
description: O funcție matematică care calculează o combinație liniară a variabilelor
  de intrare pentru a prezice un rezultat.
---
## Definition

În modelarea statistică și învățarea automată, o funcție de predicție liniară reprezintă suma ponderată a caracteristicilor de intrare plus un termen de bias. Aceasta servește ca componentă centrală în modelele liniare generalizate (GLM).

### Summary

O funcție matematică care calculează o combinație liniară a variabilelor de intrare pentru a prezice un rezultat.

## Key Concepts

- Sumă ponderată
- Termen de bias
- Modele liniare generalizate
- Coeficienți de caracteristici

## Use Cases

- Analiza regresiei liniare
- Clasificarea prin regresie logistică
- Mașini cu vectori de suport (în contextul trucului kernel)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (coeficienți de regresie)](/en/terms/regression_coefficients-coeficienți-de-regresie/)
- [bias_intercept (pantă/intercept bias)](/en/terms/bias_intercept-pantă-intercept-bias/)
- [feature_engineering (ingineria caracteristicilor)](/en/terms/feature_engineering-ingineria-caracteristicilor/)
- [generalized_linear_model (model liniar generalizat)](/en/terms/generalized_linear_model-model-liniar-generalizat/)
