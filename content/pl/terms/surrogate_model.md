---
title: "Model zastępczy"
term_id: "surrogate_model"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "approximation", "ml_technique"]
difficulty: 3
weight: 1
slug: "surrogate_model"
aliases:
  - /pl/terms/surrogate_model/
date: "2026-07-18T16:19:37.710685Z"
lastmod: "2026-07-18T17:15:08.921995Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Uproszczony model matematyczny używany do przybliżania zachowania bardziej złożonego, obliczeniowo kosztownego lub niedostępnego modelu typu \"czarna skrzynka\"."
---

## Definition

W uczeniu maszynowym i optymalizacji model zastępczy pełni rolę zastępczą dla funkcji docelowej, której bezpośrednia ewaluacja jest trudna. Jest trenowany na parach wejście-wyjście pochodzących z oryginalnego modelu, aby zapewnić...

### Summary

Uproszczony model matematyczny używany do przybliżania zachowania bardziej złożonego, obliczeniowo kosztownego lub niedostępnego modelu typu "czarna skrzynka".

## Key Concepts

- Przybliżanie modelu
- Optymalizacja "czarnej skrzynki"
- Wydajność obliczeniowa
- Model proxy

## Use Cases

- Optymalizacja hiperparametrów
- Przyspieszenie symulacji w projektowaniu inżynierskim
- Analiza wrażliwości złożonych systemów

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

- [Optymalizacja bayesowska (Bayesian Optimization)](/en/terms/optymalizacja-bayesowska-bayesian-optimization/)
- [Proces Gaussowski (Gaussian Process)](/en/terms/proces-gaussowski-gaussian-process/)
- [Funkcja "czarnej skrzynki" (Black-Box Function)](/en/terms/funkcja-czarnej-skrzynki-black-box-function/)
- [Emulator (Emulator)](/en/terms/emulator-emulator/)
