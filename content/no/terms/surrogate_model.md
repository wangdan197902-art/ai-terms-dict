---
title: "Erstatningsmodell"
term_id: "surrogate_model"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "approximation", "ml_technique"]
difficulty: 3
weight: 1
slug: "surrogate_model"
aliases:
  - /no/terms/surrogate_model/
date: "2026-07-18T16:17:52.295456Z"
lastmod: "2026-07-18T16:38:07.051202Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En forenklet matematisk modell brukt til å approksimere oppførselen til en mer kompleks, datamessig kostbar eller utilgjengelig svartboksmodell."
---

## Definition

Innen maskinlæring og optimering fungerer en erstatningsmodell som en proxy for en målfunksjon som er vanskelig å evaluere direkte. Den trenes på input-output-par fra den opprinnelige modellen for å etterligne dens oppførsel.

### Summary

En forenklet matematisk modell brukt til å approksimere oppførselen til en mer kompleks, datamessig kostbar eller utilgjengelig svartboksmodell.

## Key Concepts

- Modellapproksimasjon
- Svartboks-optimering
- Datamessig effektivitet
- Proxy-modell

## Use Cases

- Optimalisering av hyperparametre
- Akselerering av simuleringer i ingeniørdesign
- Følsomhetsanalyse av komplekse systemer

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

- [Bayesian Optimization (Bayesiansk optimering)](/en/terms/bayesian-optimization-bayesiansk-optimering/)
- [Gaussian Process (Gaussisk prosess)](/en/terms/gaussian-process-gaussisk-prosess/)
- [Black-Box Function (Svartboksfunksjon)](/en/terms/black-box-function-svartboksfunksjon/)
- [Emulator (Emulator)](/en/terms/emulator-emulator/)
