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
date: '2026-07-18T16:04:09.205825Z'
lastmod: '2026-07-18T17:15:09.144420Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Neparametrická metoda používaná k odhadu hustoty pravděpodobnosti náhodné
  proměnné na základě konečného vzorku dat.
---
## Definition

Estimace hustoty pomocí jádra (KDE) je základní statistická technika, která hladí diskrétní datové body, aby vytvořila spojitou křivku rozdělení pravděpodobnosti. Umisťuje funkci jádra, typicky Gaussovo jádro, kolem každého pozorování.

### Summary

Neparametrická metoda používaná k odhadu hustoty pravděpodobnosti náhodné proměnné na základě konečného vzorku dat.

## Key Concepts

- Funkce hustoty pravděpodobnosti
- Neparametrická statistika
- Vyhlazování
- Gaussovo jádro

## Use Cases

- Průzkumná analýza dat (EDA)
- Detekce anomálií v univariátních datech
- Vizualizace rozdělení vlastností v sadách dat

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

- [Histogram (histogram)](/en/terms/histogram-histogram/)
- [Parzen Window (Parzenovo okno)](/en/terms/parzen-window-parzenovo-okno/)
- [Bandwidth Selection (výběr šířky pásma)](/en/terms/bandwidth-selection-výběr-šířky-pásma/)
- [Scipy Stats (modul Scipy pro statistiku)](/en/terms/scipy-stats-modul-scipy-pro-statistiku/)
