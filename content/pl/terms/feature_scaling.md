---
title: "Skalowanie cech"
term_id: "feature_scaling"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "statistics", "optimization"]
difficulty: 2
weight: 1
slug: "feature_scaling"
aliases:
  - /pl/terms/feature_scaling/
date: "2026-07-18T15:54:44.595706Z"
lastmod: "2026-07-18T17:15:08.873448Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Proces normalizacji zakresu zmiennych niezależnych lub cech danych w celu zapewnienia jednolitości wielkości."
---

## Definition

Skalowanie cech standaryzuje zakres zmiennych wejściowych, aby zapobiec dominowaniu cech o większych wartościach w procesie uczenia. Powszechne metody obejmują normalizację (skalowanie min-max) oraz standaryzację (skalowanie Z-score). Jest to kluczowy krok wstępny dla wielu algorytmów, takich jak sieci neuronowe czy maszyny wektorów nośnych, które są wrażliwe na skalę danych.

### Summary

Proces normalizacji zakresu zmiennych niezależnych lub cech danych w celu zapewnienia jednolitości wielkości.

## Key Concepts

- Normalizacja
- Standaryzacja
- Spadek gradientowy
- Przetwarzanie wstępne danych

## Use Cases

- Trening sieci neuronowych
- Klasteryzacja K-średnich
- Maszyny wektorów nośnych (SVM)

## Code Example

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
```

## Related Terms

- [Min-Max Scaling (Skalowanie min-max)](/en/terms/min-max-scaling-skalowanie-min-max/)
- [Z-score Normalization (Normalizacja Z-score)](/en/terms/z-score-normalization-normalizacja-z-score/)
- [Data preprocessing (Przetwarzanie wstępne danych)](/en/terms/data-preprocessing-przetwarzanie-wstępne-danych/)
- [Gradient Descent (Spadek gradientowy)](/en/terms/gradient-descent-spadek-gradientowy/)
