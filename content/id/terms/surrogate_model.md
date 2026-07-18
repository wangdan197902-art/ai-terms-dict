---
title: "Model pengganti"
term_id: "surrogate_model"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "approximation", "ml_technique"]
difficulty: 3
weight: 1
slug: "surrogate_model"
aliases:
  - /id/terms/surrogate_model/
date: "2026-07-18T16:10:15.470071Z"
lastmod: "2026-07-18T16:38:07.511838Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Model matematika sederhana yang digunakan untuk memperkirakan perilaku model kotak hitam yang lebih kompleks, mahal secara komputasi, atau tidak dapat diakses."
---

## Definition

Dalam pembelajaran mesin dan optimisasi, model pengganti berfungsi sebagai proksi untuk fungsi target yang sulit dievaluasi secara langsung. Model ini dilatih menggunakan pasangan input-output dari model asli untuk mende

### Summary

Model matematika sederhana yang digunakan untuk memperkirakan perilaku model kotak hitam yang lebih kompleks, mahal secara komputasi, atau tidak dapat diakses.

## Key Concepts

- Pendekatan Model
- Optimisasi Kotak Hitam
- Efisiensi Komputasi
- Model Proksi

## Use Cases

- Optimisasi hiperparameter
- Percepatan simulasi desain teknik
- Analisis sensitivitas sistem kompleks

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

- [Optimisasi Bayesian (Bayesian Optimization)](/en/terms/optimisasi-bayesian-bayesian-optimization/)
- [Proses Gaussian (Gaussian Process)](/en/terms/proses-gaussian-gaussian-process/)
- [Fungsi Kotak Hitam (Black-Box Function)](/en/terms/fungsi-kotak-hitam-black-box-function/)
- [Emulator (Emulator)](/en/terms/emulator-emulator/)
