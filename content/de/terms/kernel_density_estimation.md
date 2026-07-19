---
title: Kernel-Dichteschätzung
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
date: '2026-07-18T11:20:16.151377Z'
lastmod: '2026-07-18T11:44:44.954187Z'
draft: false
source: agnes_llm
status: published
language: de
description: Eine nichtparametrische Methode zur Schätzung der Wahrscheinlichkeitsdichtefunktion
  einer Zufallsvariable auf Basis einer endlichen Datenstichprobe.
---
## Definition

Die Kernel-Dichteschätzung (KDE) ist eine grundlegende statistische Technik, die diskrete Datenpunkte glättet, um eine kontinuierliche Kurve der Wahrscheinlichkeitsverteilung zu erstellen. Dabei wird eine Kernelfunktion, typischerweise eine Gauß-

### Summary

Eine nichtparametrische Methode zur Schätzung der Wahrscheinlichkeitsdichtefunktion einer Zufallsvariable auf Basis einer endlichen Datenstichprobe.

## Key Concepts

- Wahrscheinlichkeitsdichtefunktion
- Nichtparametrische Statistik
- Glättung
- Gauß-Kernel

## Use Cases

- Explorative Datenanalyse (EDA)
- Anomalieerkennung in univariaten Daten
- Visualisierung von Merkmalsverteilungen in Datensätzen

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

- [Histogramm (Histogram)](/en/terms/histogramm-histogram/)
- [Parzen-Fenster (Parzen Window)](/en/terms/parzen-fenster-parzen-window/)
- [Bandbreitenwahl (Bandwidth Selection)](/en/terms/bandbreitenwahl-bandwidth-selection/)
- [Scipy Stats (Python-Bibliotheksfunktionen)](/en/terms/scipy-stats-python-bibliotheksfunktionen/)
