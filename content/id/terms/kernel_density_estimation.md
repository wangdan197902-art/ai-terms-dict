---
title: "Kernel density estimation"
term_id: "kernel_density_estimation"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "probability", "data-analysis"]
difficulty: 3
weight: 1
slug: "kernel_density_estimation"
aliases:
  - /id/terms/kernel_density_estimation/
date: "2026-07-18T15:56:36.565629Z"
lastmod: "2026-07-18T16:38:07.473054Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Metode non-parametrik yang digunakan untuk memperkirakan fungsi kepadatan probabilitas dari variabel acak berdasarkan sampel data terbatas."
---

## Definition

Kernel Density Estimation (KDE) adalah teknik statistik fundamental yang menghaluskan titik-titik data diskrit untuk menciptakan kurva distribusi probabilitas kontinu. Metode ini menempatkan fungsi kernel, biasanya Gaussian

### Summary

Metode non-parametrik yang digunakan untuk memperkirakan fungsi kepadatan probabilitas dari variabel acak berdasarkan sampel data terbatas.

## Key Concepts

- Fungsi Kepadatan Probabilitas
- Statistik Non-parametrik
- Penghalusan (Smoothing)
- Kernel Gaussian

## Use Cases

- Analisis Data Eksploratori (EDA)
- Deteksi anomali pada data univariat
- Visualisasi distribusi fitur dalam dataset

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

- [Histogram (Grafik frekuensi)](/en/terms/histogram-grafik-frekuensi/)
- [Parzen Window (Metode estimasi kepadatan)](/en/terms/parzen-window-metode-estimasi-kepadatan/)
- [Bandwidth Selection (Pemilihan bandwidth)](/en/terms/bandwidth-selection-pemilihan-bandwidth/)
- [Scipy Stats (Pustaka statistik Python)](/en/terms/scipy-stats-pustaka-statistik-python/)
