---
title: Суррогатная модель
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T16:17:22.513630Z'
lastmod: '2026-07-18T16:38:07.206499Z'
draft: false
source: agnes_llm
status: published
language: ru
description: Упрощенная математическая модель, используемая для аппроксимации поведения
  более сложной, вычислительно затратной или недоступной модели-черного ящика.
---
## Definition

В машинном обучении и оптимизации суррогатная модель служит прокси-функцией для целевой функции, которую трудно оценивать напрямую. Она обучается на парах входных и выходных данных исходной модели для п

### Summary

Упрощенная математическая модель, используемая для аппроксимации поведения более сложной, вычислительно затратной или недоступной модели-черного ящика.

## Key Concepts

- Аппроксимация модели
- Оптимизация черного ящика
- Вычислительная эффективность
- Модель-прокси

## Use Cases

- Оптимизация гиперпараметров
- Ускорение симуляций инженерного проектирования
- Анализ чувствительности сложных систем

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

- [Bayesian Optimization (Байесовская оптимизация)](/en/terms/bayesian-optimization-байесовская-оптимизация/)
- [Gaussian Process (Гауссовский процесс)](/en/terms/gaussian-process-гауссовский-процесс/)
- [Black-Box Function (Функция черного ящика)](/en/terms/black-box-function-функция-черного-ящика/)
- [Emulator (Эмулятор)](/en/terms/emulator-эмулятор/)
