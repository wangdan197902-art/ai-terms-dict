---
title: "Erstatningsmodel"
term_id: "surrogate_model"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "approximation", "ml_technique"]
difficulty: 3
weight: 1
slug: "surrogate_model"
aliases:
  - /da/terms/surrogate_model/
date: "2026-07-18T16:20:39.138678Z"
lastmod: "2026-07-18T17:15:09.335107Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En forenklet matematisk model, der bruges til at approksimere adfærden hos en mere kompleks, beregningsmæssigt dyr eller utilgængelig black-box-model."
---

## Definition

Inden for maskinlæring og optimering fungerer en erstatningsmodel som en proxy for en målfunktion, der er svær at evaluere direkte. Den trænes på input-output-par fra den oprindelige model for at efterligne dens opførsel.

### Summary

En forenklet matematisk model, der bruges til at approksimere adfærden hos en mere kompleks, beregningsmæssigt dyr eller utilgængelig black-box-model.

## Key Concepts

- Modelapproksimation
- Black-box-optimering
- Beregningseffektivitet
- Proxy-model

## Use Cases

- Hyperparameteroptimering
- Fremskyndelse af simuleringer inden for ingeniørdesign
- Følsomhedsanalyse af komplekse systemer

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

- [Bayesisk optimering (Bayesian Optimization)](/en/terms/bayesisk-optimering-bayesian-optimization/)
- [Gaußsk proces (Gaussian Process)](/en/terms/gaußsk-proces-gaussian-process/)
- [Black-box-funktion (Black-Box Function)](/en/terms/black-box-funktion-black-box-function/)
- [Emulator (Emulator)](/en/terms/emulator-emulator/)
