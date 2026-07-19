---
title: Lineær prediktorfunksjon
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
date: '2026-07-18T16:02:59.608232Z'
lastmod: '2026-07-18T16:38:07.019324Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En matematisk funksjon som beregner en lineær kombinasjon av inndatavariabler
  for å forutse et utfall.
---
## Definition

Inn statistisk modellering og maskinlæring representerer en lineær prediktorfunksjon den vektete summen av inndatafunksjoner pluss en bias-ledd. Den fungerer som kjernekomponenten i generaliserte lineære modeller (GLM).

### Summary

En matematisk funksjon som beregner en lineær kombinasjon av inndatavariabler for å forutse et utfall.

## Key Concepts

- Vektet sum
- Bias-ledd
- Generaliserte lineære modeller
- Funksjonskoeffisienter

## Use Cases

- Lineær regresjonsanalyse
- Logistisk regresjonsklassifisering
- Støttevektormaskiner (i kontekst av kernel-tricket)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (regresjonskoeffisienter)](/en/terms/regression_coefficients-regresjonskoeffisienter/)
- [bias_intercept (bias/avskjæring)](/en/terms/bias_intercept-bias-avskjæring/)
- [feature_engineering (funksjonsutvikling)](/en/terms/feature_engineering-funksjonsutvikling/)
- [generalized_linear_model (generalisert lineær modell)](/en/terms/generalized_linear_model-generalisert-lineær-modell/)
