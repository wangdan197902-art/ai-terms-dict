---
title: Surrogatmodell
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
date: '2026-07-18T11:35:08.767318Z'
lastmod: '2026-07-18T11:44:44.989893Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein vereinfachtes mathematisches Modell, das verwendet wird, um das Verhalten
  eines komplexeren, rechenintensiveren oder unzugänglichen Black-Box-Modells anzunähern.
---
## Definition

Im maschinellen Lernen und in der Optimierung dient ein Surrogatmodell als Stellvertreter für eine Zielfunktion, die direkt schwer zu bewerten ist. Es wird anhand von Eingabe-Ausgabe-Paaren des ursprünglichen Modells trainiert, um...

### Summary

Ein vereinfachtes mathematisches Modell, das verwendet wird, um das Verhalten eines komplexeren, rechenintensiveren oder unzugänglichen Black-Box-Modells anzunähern.

## Key Concepts

- Modellapproximation
- Black-Box-Optimierung
- Recheneffizienz
- Stellvertretendes Modell (Proxy Model)

## Use Cases

- Hyperparameter-Optimierung
- Beschleunigung von Simulationen im Ingenieurdesign
- Sensitivitätsanalyse komplexer Systeme

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

- [Bayesian Optimization (Bayessche Optimierung)](/en/terms/bayesian-optimization-bayessche-optimierung/)
- [Gaussian Process (Gaußscher Prozess)](/en/terms/gaussian-process-gaußscher-prozess/)
- [Black-Box Function (Black-Box-Funktion)](/en/terms/black-box-function-black-box-funktion/)
- [Emulator (Emulator)](/en/terms/emulator-emulator/)
