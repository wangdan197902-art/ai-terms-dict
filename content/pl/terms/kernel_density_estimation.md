---
title: Estymacja gęstości jądra
term_id: kernel_density_estimation
category: basic_concepts
subcategory: ''
tags:
- statistics
- probability
- Data Analysis
difficulty: 3
weight: 1
slug: kernel_density_estimation
date: '2026-07-18T16:02:26.980741Z'
lastmod: '2026-07-18T17:15:08.887910Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Nienparametryczna metoda używana do estymacji funkcji gęstości prawdopodobieństwa
  zmiennej losowej na podstawie skończonego próbkowania danych.
---
## Definition

Estymacja gęstości jądra (KDE) to fundamentalna technika statystyczna, która wygładza dyskretne punkty danych, aby utworzyć ciągłą krzywą rozkładu prawdopodobieństwa. Polega ona na umieszczeniu funkcji jądra (zazwyczaj Gaussa) w każdym punkcie danych i zsumowaniu ich wkładów.

### Summary

Nienparametryczna metoda używana do estymacji funkcji gęstości prawdopodobieństwa zmiennej losowej na podstawie skończonego próbkowania danych.

## Key Concepts

- Funkcja gęstości prawdopodobieństwa
- Statystyka nienparametryczna
- Wygładzanie
- Jądro Gaussa

## Use Cases

- Eksploracyjna analiza danych (EDA)
- Wykrywanie anomalii w danych jednowymiarowych
- Wizualizacja rozkładów cech w zbiorach danych

## Code Example

```python
from scipy.stats import gaussian_kde
import numpy as np

data = np.random.normal(0, 1, 100)
kde = gaussian_kde(data)
x_vals = np.linspace(-3, 3, 100)
y_vals = kde(x_vals)
```

## Related Terms

- [Histogram](/en/terms/histogram/)
- [Okno Parzena (Parzen Window)](/en/terms/okno-parzena-parzen-window/)
- [Wybór szerokości pasma (Bandwidth Selection)](/en/terms/wybór-szerokości-pasma-bandwidth-selection/)
- [Moduł Scipy Stats](/en/terms/moduł-scipy-stats/)
