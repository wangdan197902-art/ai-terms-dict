---
title: Kernel tæthedsestimering
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
date: '2026-07-18T16:02:32.900115Z'
lastmod: '2026-07-18T17:15:09.301684Z'
draft: false
source: agnes_llm
status: published
language: da
description: En ikke-parametrisk metode til at estimere sandsynlighedstæthedsfunktionen
  for en stokastisk variabel baseret på et endeligt datasæt.
---
## Definition

Kernel Tæthedsestimering (KDE) er en fundamental statistisk teknik, der glatter diskrete datapunkter for at skabe en kontinuert kurve for sandsynlighedsfordelingen. Den placerer en kernefunktion, typisk en Gaussisk kerne, over hvert datapunkt.

### Summary

En ikke-parametrisk metode til at estimere sandsynlighedstæthedsfunktionen for en stokastisk variabel baseret på et endeligt datasæt.

## Key Concepts

- Sandsynlighedstæthedsfunktion
- Ikke-parametrisk statistik
- Glating (Smoothing)
- Gaussisk kerne

## Use Cases

- Eksplorativ dataanalyse (EDA)
- Detektion af anomalier i univariate data
- Visualisering af fordelingen af funktioner i datasæt

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
- [Parzen-vindue (Parzen Window)](/en/terms/parzen-vindue-parzen-window/)
- [Valg af båndbredde (Bandwidth Selection)](/en/terms/valg-af-båndbredde-bandwidth-selection/)
- [Scipy Stats (Python bibliotek)](/en/terms/scipy-stats-python-bibliotek/)
