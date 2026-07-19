---
title: Линейная предикторная функция
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
date: '2026-07-18T16:01:40.136495Z'
lastmod: '2026-07-18T16:38:07.175282Z'
draft: false
source: agnes_llm
status: published
language: ru
description: Математическая функция, вычисляющая линейную комбинацию входных переменных
  для прогнозирования результата.
---
## Definition

В статистическом моделировании и машинном обучении линейная предикторная функция представляет собой взвешенную сумму входных признаков плюс член смещения. Она является ключевым компонентом обобщенных линейных моделей (GLM), где она связывает математическое ожидание целевой переменной с линейной комбинацией предикторов через функцию связи.

### Summary

Математическая функция, вычисляющая линейную комбинацию входных переменных для прогнозирования результата.

## Key Concepts

- Взвешенная сумма
- Член смещения
- Обобщенные линейные модели
- Коэффициенты признаков

## Use Cases

- Анализ линейной регрессии
- Классификация логистической регрессией
- Метод опорных векторов (в контексте ядра)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (коэффициенты регрессии)](/en/terms/regression_coefficients-коэффициенты-регрессии/)
- [bias_intercept (свободный член / пересечение с осью)](/en/terms/bias_intercept-свободный-член-пересечение-с-осью/)
- [feature_engineering (конструирование признаков)](/en/terms/feature_engineering-конструирование-признаков/)
- [generalized_linear_model (обобщенная линейная модель)](/en/terms/generalized_linear_model-обобщенная-линейная-модель/)
