---
title: "Плотный слой"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /ru/terms/dense/
date: "2026-07-18T15:49:49.004908Z"
lastmod: "2026-07-18T16:38:07.148359Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Слой или тензор, в котором каждый элемент связан с каждым элементом предыдущего слоя или измерения."
---

## Definition

В нейронных сетях термин «плотный» (dense) относится к полностью связанным слоям, где каждый нейрон получает входные данные от всех нейронов предыдущего слоя. Это контрастирует с разреженными связями, встречающимися в сверточных или других архитектурах.

### Summary

Слой или тензор, в котором каждый элемент связан с каждым элементом предыдущего слоя или измерения.

## Key Concepts

- Полностью связанный
- Матрица весов
- Функция активации
- Интеграция признаков

## Use Cases

- Финальные классификационные слои в многослойных перцептронах (MLP)
- Объединение признаков в гибридных моделях
- Простые задачи регрессии

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Прямая нейронная сеть)](/en/terms/feedforward-neural-network-прямая-нейронная-сеть/)
- [Backpropagation (Обратное распространение ошибки)](/en/terms/backpropagation-обратное-распространение-ошибки/)
- [ReLU (Функция активации ReLU)](/en/terms/relu-функция-активации-relu/)
- [Bias Term (Член смещения)](/en/terms/bias-term-член-смещения/)
