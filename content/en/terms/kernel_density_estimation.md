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
date: '2026-07-18T10:03:27.085160Z'
lastmod: '2026-07-18T11:44:44.687972Z'
draft: false
source: agnes_llm
status: published
language: en
description: A non-parametric method used to estimate the probability density function
  of a random variable based on a finite data sample.
---
## Definition

Kernel Density Estimation (KDE) is a fundamental statistical technique that smooths discrete data points to create a continuous probability distribution curve. It places a kernel function, typically Gaussian, at each data point and sums them to estimate the underlying density. Unlike histograms, KDE does not depend on binning choices, providing a smoother and more accurate representation of data distribution. It is widely used in exploratory data analysis to understand feature distributions and detect anomalies.

### Summary

A non-parametric method used to estimate the probability density function of a random variable based on a finite data sample.

## Key Concepts

- Probability Density Function
- Non-parametric Statistics
- Smoothing
- Gaussian Kernel

## Use Cases

- Exploratory Data Analysis (EDA)
- Anomaly detection in univariate data
- Visualizing feature distributions in datasets

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
- [Parzen Window](/en/terms/parzen-window/)
- [Bandwidth Selection](/en/terms/bandwidth-selection/)
- [Scipy Stats](/en/terms/scipy-stats/)
