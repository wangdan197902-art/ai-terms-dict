---
title: Lineare Prädiktorfunktion
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
date: '2026-07-18T11:21:48.680993Z'
lastmod: '2026-07-18T11:44:44.958802Z'
draft: false
source: agnes_llm
status: published
language: de
description: Eine mathematische Funktion, die eine lineare Kombination von Eingangsvariablen
  berechnet, um ein Ergebnis vorherzusagen.
---
## Definition

In der statistischen Modellierung und im maschinellen Lernen stellt eine lineare Prädiktorfunktion die gewichtete Summe der Eingangsmerkmale plus einem Bias-Term dar. Sie ist die Kernkomponente in verallgemeinerten linearen Modellen (GLMs).

### Summary

Eine mathematische Funktion, die eine lineare Kombination von Eingangsvariablen berechnet, um ein Ergebnis vorherzusagen.

## Key Concepts

- Gewichtete Summe
- Bias-Term
- Verallgemeinerte lineare Modelle
- Merkmalskoeffizienten

## Use Cases

- Lineare Regressionsanalyse
- Logistische Regressionsklassifizierung
- Support Vector Machines (im Kontext des Kernel-Tricks)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (Regressionskoeffizienten)](/en/terms/regression_coefficients-regressionskoeffizienten/)
- [bias_intercept (Bias-Achsenabschnitt)](/en/terms/bias_intercept-bias-achsenabschnitt/)
- [feature_engineering (Merkmalskonstruktion)](/en/terms/feature_engineering-merkmalskonstruktion/)
- [generalized_linear_model (verallgemeinertes lineares Modell)](/en/terms/generalized_linear_model-verallgemeinertes-lineares-modell/)
