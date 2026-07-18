---
title: "Сигмоид"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
aliases:
  - /ru/terms/sigmoid/
date: "2026-07-18T16:14:49.256347Z"
lastmod: "2026-07-18T16:38:07.201772Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Математическая функция, отображающая любое действительное число в значение между нулем и единицей, образуя S-образную кривую."
---

## Definition

Сигмоидная функция, определяемая как σ(z) = 1 / (1 + e^-z), широко используется в машинном обучении для моделирования вероятностей. Она сжимает входные значения в диапазон (0, 1), что делает её подходящей для задач бинарной классификации и в качестве функции активации в нейронных сетях.

### Summary

Математическая функция, отображающая любое действительное число в значение между нулем и единицей, образуя S-образную кривую.

## Key Concepts

- Логистическая функция
- Отображение вероятностей
- Исчезающий градиент
- Нелинейность

## Use Cases

- Выходной слой для бинарной классификации
- Логистическая регрессия
- Функция активации в неглубоких нейронных сетях

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU (Функция активации)](/en/terms/relu-функция-активации/)
- [Softmax (Функция нормализации вероятностей)](/en/terms/softmax-функция-нормализации-вероятностей/)
- [Logistic Regression (Логистическая регрессия)](/en/terms/logistic-regression-логистическая-регрессия/)
- [Activation Function (Функция активации)](/en/terms/activation-function-функция-активации/)
