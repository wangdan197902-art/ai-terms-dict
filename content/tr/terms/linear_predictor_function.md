---
title: Doğrusal tahminci fonksiyon
term_id: linear_predictor_function
category: basic_concepts
subcategory: ''
tags:
- statistics
- Linear Models
- mathematics
difficulty: 2
weight: 1
slug: linear_predictor_function
date: '2026-07-18T16:01:04.025852Z'
lastmod: '2026-07-18T16:38:07.327918Z'
draft: false
source: agnes_llm
status: published
language: tr
description: Bir sonucu tahmin etmek için girdi değişkenlerinin doğrusal kombinasyonunu
  hesaplayan matematiksel bir fonksiyon.
---
## Definition

İstatistiksel modelleme ve makine öğreniminde, doğrusal tahminci fonksiyon, girdi özelliklerinin ağırlıklı toplamına bir sapma (bias) teriminin eklenmesiyle temsil edilir. Genelleştirilmiş doğrusal modellerin (GLM) temel bileşenini oluşturur.

### Summary

Bir sonucu tahmin etmek için girdi değişkenlerinin doğrusal kombinasyonunu hesaplayan matematiksel bir fonksiyon.

## Key Concepts

- Ağırlıklı toplam
- Sapma terimi
- Genelleştirilmiş doğrusal modeller
- Özellik katsayıları

## Use Cases

- Doğrusal regresyon analizi
- Lojistik regresyon sınıflandırması
- Destek vektör makineleri (çekirdek hilesi bağlamında)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (regresyon katsayıları)](/en/terms/regression_coefficients-regresyon-katsayıları/)
- [bias_intercept (sapma/kesişim noktası)](/en/terms/bias_intercept-sapma-kesişim-noktası/)
- [feature_engineering (özellik mühendisliği)](/en/terms/feature_engineering-özellik-mühendisliği/)
- [generalized_linear_model (genelleştirilmiş doğrusal model)](/en/terms/generalized_linear_model-genelleştirilmiş-doğrusal-model/)
