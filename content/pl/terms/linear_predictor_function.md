---
title: Funkcja predyktora liniowego
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
date: '2026-07-18T16:04:33.498484Z'
lastmod: '2026-07-18T17:15:08.892253Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Funkcja matematyczna obliczająca liniową kombinację zmiennych wejściowych
  w celu przewidzenia wyniku.
---
## Definition

W modelowaniu statystycznym i uczeniu maszynowym funkcja predyktora liniowego reprezentuje ważoną sumę cech wejściowych plus składnik biasu. Stanowi ona kluczowy element w uogólnionych modelach liniowych (GLM).

### Summary

Funkcja matematyczna obliczająca liniową kombinację zmiennych wejściowych w celu przewidzenia wyniku.

## Key Concepts

- Suma ważona
- Składnik biasu
- Uogólnione modele liniowe
- Współczynniki cech

## Use Cases

- Analiza regresji liniowej
- Klasyfikacja przez regresję logistyczną
- Maszyny wektorów nośnych (w kontekście tricku jądra)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (współczynniki regresji)](/en/terms/regression_coefficients-współczynniki-regresji/)
- [bias_intercept (przecięcie/bias)](/en/terms/bias_intercept-przecięcie-bias/)
- [feature_engineering (inżynieria cech)](/en/terms/feature_engineering-inżynieria-cech/)
- [generalized_linear_model (uogólniony model liniowy)](/en/terms/generalized_linear_model-uogólniony-model-liniowy/)
