---
title: Surrogaatmodel
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T16:19:09.501563Z'
lastmod: '2026-07-18T17:15:08.791329Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Een vereenvoudigd wiskundig model dat wordt gebruikt om het gedrag van
  een complexer, rekenintensiever of ontoegankelijk black-box-model te benaderen.
---
## Definition

In machine learning en optimalisatie fungeert een surrogaatmodel als een proxy voor een doelwitfunctie die moeilijk direct te evalueren is. Het wordt getraind op invoer-uitvoerparen van het oorspronkelijke model om de berekeningskosten te verlagen.

### Summary

Een vereenvoudigd wiskundig model dat wordt gebruikt om het gedrag van een complexer, rekenintensiever of ontoegankelijk black-box-model te benaderen.

## Key Concepts

- Modelbenadering
- Black-box-optimalisatie
- Rekenkundige efficiëntie
- Proxymodel

## Use Cases

- Hyperparameteroptimalisatie
- Versnelling van simulaties in ingenieursontwerp
- Gevoeligheidsanalyse van complexe systemen

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Bayesian Optimization (Bayesiaanse optimalisatie)](/en/terms/bayesian-optimization-bayesiaanse-optimalisatie/)
- [Gaussian Process (Gaussisch proces)](/en/terms/gaussian-process-gaussisch-proces/)
- [Black-Box Function (Black-boxfunctie)](/en/terms/black-box-function-black-boxfunctie/)
- [Emulator (Emulator)](/en/terms/emulator-emulator/)
