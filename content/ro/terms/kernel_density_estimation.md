---
title: Estimarea densității kernel
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
date: '2026-07-18T16:06:45.361020Z'
lastmod: '2026-07-18T17:15:09.671041Z'
draft: false
source: agnes_llm
status: published
language: ro
description: O metodă neparametrică utilizată pentru a estima funcția de densitate
  de probabilitate a unei variabile aleatoare pe baza unui eșantion finit de date.
---
## Definition

Estimarea densității kernel (KDE) este o tehnică statistică fundamentală care netezește punctele de date discrete pentru a crea o curbă continuă a distribuției de probabilitate. Plasează o funcție kernel, de obicei G

### Summary

O metodă neparametrică utilizată pentru a estima funcția de densitate de probabilitate a unei variabile aleatoare pe baza unui eșantion finit de date.

## Key Concepts

- Funcția de densitate de probabilitate
- Statistici neparametrice
- Netezire
- Kernel gaussian

## Use Cases

- Analiza exploratorie a datelor (EDA)
- Detectarea anomaliilor în date univariante
- Vizualizarea distribuțiilor caracteristicilor în seturi de date

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

- [Histogram (Histogramă)](/en/terms/histogram-histogramă/)
- [Parzen Window (Fereastră Parzen)](/en/terms/parzen-window-fereastră-parzen/)
- [Bandwidth Selection (Selecția lățimii benzii)](/en/terms/bandwidth-selection-selecția-lățimii-benzii/)
- [Scipy Stats (Module de statistici Scipy)](/en/terms/scipy-stats-module-de-statistici-scipy/)
