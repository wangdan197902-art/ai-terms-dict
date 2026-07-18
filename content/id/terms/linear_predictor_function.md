---
title: "Fungsi prediktor linear"
term_id: "linear_predictor_function"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "linear_models", "mathematics"]
difficulty: 2
weight: 1
slug: "linear_predictor_function"
aliases:
  - /id/terms/linear_predictor_function/
date: "2026-07-18T15:58:12.199928Z"
lastmod: "2026-07-18T16:38:07.477581Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Fungsi matematika yang menghitung kombinasi linear dari variabel input untuk memprediksi suatu hasil."
---

## Definition

Dalam pemodelan statistik dan pembelajaran mesin, fungsi prediktor linear mewakili jumlah tertimbang dari fitur input ditambah dengan istilah bias. Fungsi ini merupakan komponen inti dalam model linear umum (generalized linear models).

### Summary

Fungsi matematika yang menghitung kombinasi linear dari variabel input untuk memprediksi suatu hasil.

## Key Concepts

- Jumlah tertimbang
- Istilah bias
- Model linear umum
- Koefisien fitur

## Use Cases

- Analisis regresi linear
- Klasifikasi regresi logistik
- Mesin vektor dukungan (dalam konteks trik kernel)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (koefisien regresi)](/en/terms/regression_coefficients-koefisien-regresi/)
- [bias_intercept (intersep bias)](/en/terms/bias_intercept-intersep-bias/)
- [feature_engineering (rekayasa fitur)](/en/terms/feature_engineering-rekayasa-fitur/)
- [generalized_linear_model (model linear umum)](/en/terms/generalized_linear_model-model-linear-umum/)
