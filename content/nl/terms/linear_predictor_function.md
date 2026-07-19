---
title: Lineaire voorspellingsfunctie
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
date: '2026-07-18T16:04:45.160516Z'
lastmod: '2026-07-18T17:15:08.762258Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Een wiskundige functie die een lineaire combinatie van invoervariabelen
  berekent om een uitkomst te voorspellen.
---
## Definition

In statistische modellering en machine learning vertegenwoordigt een lineaire voorspellingsfunctie de gewogen som van invoerfuncties plus een bias-term. Het fungeert als het kernonderdeel in gegeneraliseerde lineaire modellen (GLM's).

### Summary

Een wiskundige functie die een lineaire combinatie van invoervariabelen berekent om een uitkomst te voorspellen.

## Key Concepts

- Gewogen som
- Bias-term
- Gegeneraliseerde lineaire modellen
- Functiecoëfficiënten

## Use Cases

- Lineaire regressie-analyse
- Classificatie met logistische regressie
- Support Vector Machines (in de context van de kernel-trick)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (regressiecoëfficiënten)](/en/terms/regression_coefficients-regressiecoëfficiënten/)
- [bias_intercept (bias-snijpunt)](/en/terms/bias_intercept-bias-snijpunt/)
- [feature_engineering (functieconstructie)](/en/terms/feature_engineering-functieconstructie/)
- [generalized_linear_model (gegeneraliseerd lineair model)](/en/terms/generalized_linear_model-gegeneraliseerd-lineair-model/)
