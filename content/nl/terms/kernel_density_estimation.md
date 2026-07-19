---
title: Kernel density estimation
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
date: '2026-07-18T16:01:18.448981Z'
lastmod: '2026-07-18T17:15:08.758027Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Een niet-parametrische methode om de waarschijnlijkheidsdichtheidsfunctie
  van een willekeurige variabele te schatten op basis van een eindige steekproef.
---
## Definition

Kernel Density Estimation (KDE) is een fundamentele statistische techniek die discrete gegevenspunten gladstrijkt om een continue waarschijnlijkheidsdistributiekromme te creëren. Het plaatst een kernfunctie, meestal een G

### Summary

Een niet-parametrische methode om de waarschijnlijkheidsdichtheidsfunctie van een willekeurige variabele te schatten op basis van een eindige steekproef.

## Key Concepts

- Wahrscheinlichheidsdichtheidsfunctie
- Niet-parametrische Statistiek
- Gladstrijken
- Gaussische Kern

## Use Cases

- Verkennde Data-analyse (EDA)
- Detectie van anomalieën in univariate gegevens
- Visualiseren van feature-distributies in datasets

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

- [Histogram (Histogram)](/en/terms/histogram-histogram/)
- [Parzen Window (Parven-venster)](/en/terms/parzen-window-parven-venster/)
- [Bandwidth Selection (Selectie van bandbreedte)](/en/terms/bandwidth-selection-selectie-van-bandbreedte/)
- [Scipy Stats (Scipy-statistiek)](/en/terms/scipy-stats-scipy-statistiek/)
