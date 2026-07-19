---
title: Обучение с учителем
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T15:36:46.873576Z'
lastmod: '2026-07-18T16:38:07.111010Z'
draft: false
source: agnes_llm
status: published
language: ru
description: Парадигма машинного обучения, в которой модель учится отображать входные
  данные на выходные на основе размеченных примеров обучения.
---
## Definition

В обучении с учителем алгоритм тренируется на размеченном наборе данных, что означает, что каждый входной пример сопровождается правильным выходным значением. Цель состоит в том, чтобы модель научилась выявлять скрытые закономерности между входами и выходами.

### Summary

Парадигма машинного обучения, в которой модель учится отображать входные данные на выходные на основе размеченных примеров обучения.

## Key Concepts

- Размеченные данные
- Отображение вход-выход
- Классификация
- Регрессия

## Use Cases

- Обнаружение спама в электронной почте
- Прогнозирование цен на жилье
- Распознавание изображений

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (Обучение без учителя)](/en/terms/unsupervised-learning-обучение-без-учителя/)
- [Training Set (Обучающая выборка)](/en/terms/training-set-обучающая-выборка/)
- [Validation Set (Валидационная выборка)](/en/terms/validation-set-валидационная-выборка/)
- [Model Accuracy (Точность модели)](/en/terms/model-accuracy-точность-модели/)
