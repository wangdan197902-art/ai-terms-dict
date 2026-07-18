---
title: "Funzione di predittore lineare"
term_id: "linear_predictor_function"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "linear_models", "mathematics"]
difficulty: 2
weight: 1
slug: "linear_predictor_function"
aliases:
  - /it/terms/linear_predictor_function/
date: "2026-07-18T16:08:17.299713Z"
lastmod: "2026-07-18T17:15:08.643710Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Una funzione matematica che calcola una combinazione lineare di variabili di input per prevedere un risultato."
---

## Definition

Nella modellazione statistica e nell'apprendimento automatico, una funzione di predittore lineare rappresenta la somma pesata delle caratteristiche di input più un termine di bias. Rappresenta il componente fondamentale nei modelli lineari generalizzati (GLM).

### Summary

Una funzione matematica che calcola una combinazione lineare di variabili di input per prevedere un risultato.

## Key Concepts

- Somma pesata
- Termine di bias
- Modelli lineari generalizzati
- Coefficienti delle caratteristiche

## Use Cases

- Analisi di regressione lineare
- Classificazione con regressione logistica
- Macchine a vettori di supporto (contesto del trucco del kernel)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (coefficienti di regressione)](/en/terms/regression_coefficients-coefficienti-di-regressione/)
- [bias_intercept (intercetta/bias)](/en/terms/bias_intercept-intercetta-bias/)
- [feature_engineering (ingegneria delle caratteristiche)](/en/terms/feature_engineering-ingegneria-delle-caratteristiche/)
- [generalized_linear_model (modello lineare generalizzato)](/en/terms/generalized_linear_model-modello-lineare-generalizzato/)
