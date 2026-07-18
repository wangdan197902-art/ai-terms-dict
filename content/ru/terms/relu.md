---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /ru/terms/relu/
date: "2026-07-18T15:36:07.358387Z"
lastmod: "2026-07-18T16:38:07.109596Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Rectified Linear Unit (Ректифицированная линейная единица) — функция активации, которая выводит входное значение напрямую, если оно положительно, и ноль в противном случае."
---

## Definition

ReLU широко используется в нейронных сетях глубокого обучения благодаря своей вычислительной эффективности и способности смягчать проблему затухания градиента. Математически определяется как f(x) = max(0, x), она вносит нелинейность в модель.

### Summary

Rectified Linear Unit (Ректифицированная линейная единица) — функция активации, которая выводит входное значение напрямую, если оно положительно, и ноль в противном случае.

## Key Concepts

- Нелинейность
- Функция активации
- Затухание градиента
- Кусочно-линейная функция

## Use Cases

- Скрытые слои в сверточных нейронных сетях (CNN)
- Глубокие прямого распространения сети
- Модели распознавания изображений

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (сигмоидная функция)](/en/terms/sigmoid-сигмоидная-функция/)
- [Tanh (гиперболический тангенс)](/en/terms/tanh-гиперболический-тангенс/)
- [Leaky ReLU (непротекающая линейная единица)](/en/terms/leaky-relu-непротекающая-линейная-единица/)
- [Neural Network (нейронная сеть)](/en/terms/neural-network-нейронная-сеть/)
