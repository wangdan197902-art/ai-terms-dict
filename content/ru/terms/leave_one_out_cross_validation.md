---
title: "Кросс-валидация методом «один против всех»"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /ru/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:01:25.233236Z"
lastmod: "2026-07-18T16:38:07.174628Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Строгий метод ресэмплинга, при котором модель обучается на всех выборках, кроме одной, и тестируется на этой единственной оставленной выборке; процесс повторяется для каждой точки данных."
---

## Definition

Кросс-валидация методом «один против всех» (LOOCV) является частным случаем k-блочной кросс-валидации, где k равно количеству образцов в наборе данных. Она дает почти несмещенную оценку производительности модели, вычисляя среднее значение ошибки на каждой итерации, когда одна точка используется как тестовая, а остальные — как обучающая.

### Summary

Строгий метод ресэмплинга, при котором модель обучается на всех выборках, кроме одной, и тестируется на этой единственной оставленной выборке; процесс повторяется для каждой точки данных.

## Key Concepts

- Ресэмплинг
- Оценка модели
- Компромисс смещения и дисперсии
- Вычислительная стоимость

## Use Cases

- Оценка моделей на небольших медицинских наборах данных
- Настройка гиперпараметров при дефиците данных
- Строгое сравнение производительности алгоритмов

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (k-блочная кросс-валидация)](/en/terms/k-fold-cross-validation-k-блочная-кросс-валидация/)
- [train_test_split (разделение на обучающую и тестовую выборки)](/en/terms/train_test_split-разделение-на-обучающую-и-тестовую-выборки/)
- [bootstrap (бутстрэп)](/en/terms/bootstrap-бутстрэп/)
- [cross_validation_score (оценка кросс-валидации)](/en/terms/cross_validation_score-оценка-кросс-валидации/)
