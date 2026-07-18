---
title: "Трюк репараметризации"
term_id: "reparameterization_trick"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "probabilistic_models", "optimization"]
difficulty: 4
weight: 1
slug: "reparameterization_trick"
aliases:
  - /ru/terms/reparameterization_trick/
date: "2026-07-18T16:13:10.204887Z"
lastmod: "2026-07-18T16:38:07.198439Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Метод, разделяющий стохастические переменные и обучаемые параметры для обеспечения градиентной оптимизации в вариационном выводе."
---

## Definition

Трюк репараметризации — это фундаментальный метод, используемый в вариационных автокодировщиках и других вероятностных моделях. Он позволяет градиентам проходить через стохастические узлы путем выражения случайной переменной как детерминированной функции ее параметров и независимого шума.

### Summary

Метод, разделяющий стохастические переменные и обучаемые параметры для обеспечения градиентной оптимизации в вариационном выводе.

## Key Concepts

- Вариационный вывод
- Оценка градиентов
- Стохастические узлы
- Дифференцируемое моделирование

## Use Cases

- Обучение вариационных автокодировщиков (VAE)
- Байесовские нейронные сети
- Вероятностные графовые модели

## Code Example

```python
import torch
epsilon = torch.randn(100, 10)
mu = torch.zeros(100, 10)
sigma = torch.ones(100, 10)
z = mu + sigma * epsilon  # Reparameterized sampling
```

## Related Terms

- [ELBO (нижняя оценка правдоподобия)](/en/terms/elbo-нижняя-оценка-правдоподобия/)
- [Скрытые переменные](/en/terms/скрытые-переменные/)
- [Обратное распространение ошибки](/en/terms/обратное-распространение-ошибки/)
- [Монте-Карло оценка](/en/terms/монте-карло-оценка/)
