---
title: Surrogate model
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
date: '2026-07-18T10:17:11.294395Z'
lastmod: '2026-07-18T11:44:44.725628Z'
draft: false
source: agnes_llm
status: published
language: en
description: A simplified mathematical model used to approximate the behavior of a
  more complex, computationally expensive, or inaccessible black-box model.
---
## Definition

In machine learning and optimization, a surrogate model serves as a proxy for a target function that is difficult to evaluate directly. It is trained on input-output pairs from the original model to predict outcomes quickly and cheaply. Common techniques include Gaussian Processes, Polynomial Chaos Expansion, and neural networks. Surrogate models are essential for hyperparameter tuning, sensitivity analysis, and optimizing systems where each evaluation takes significant time or resources.

### Summary

A simplified mathematical model used to approximate the behavior of a more complex, computationally expensive, or inaccessible black-box model.

## Key Concepts

- Model Approximation
- Black-Box Optimization
- Computational Efficiency
- Proxy Model

## Use Cases

- Hyperparameter optimization
- Engineering design simulation acceleration
- Sensitivity analysis of complex systems

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

- [Bayesian Optimization](/en/terms/bayesian-optimization/)
- [Gaussian Process](/en/terms/gaussian-process/)
- [Black-Box Function](/en/terms/black-box-function/)
- [Emulator](/en/terms/emulator/)
