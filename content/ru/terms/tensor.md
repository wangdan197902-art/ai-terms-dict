---
title: "Тензор"
term_id: "tensor"
category: "basic_concepts"
subcategory: ""
tags: ["math", "data-structures", "pytorch"]
difficulty: 2
weight: 1
slug: "tensor"
aliases:
  - /ru/terms/tensor/
date: "2026-07-18T16:18:02.515710Z"
lastmod: "2026-07-18T16:38:07.207632Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Многомерный массив, служащий фундаментальной структурой данных для фреймворков глубокого обучения."
---

## Definition

В информатике и глубоком обучении тензор — это математический объект, обобщающий скаляры, векторы и матрицы до более высоких размерностей. Он характеризуется своим рангом (количеством измерений) и формой.

### Summary

Многомерный массив, служащий фундаментальной структурой данных для фреймворков глубокого обучения.

## Key Concepts

- Ранг
- Форма
- Размерность
- Бродкастинг (расширение размерности)

## Use Cases

- Обработка изображений (4D тензоры)
- Хранение весов нейронных сетей
- Подача данных батчами

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix (Матрица)](/en/terms/matrix-матрица/)
- [Vector (Вектор)](/en/terms/vector-вектор/)
- [Deep Learning (Глубокое обучение)](/en/terms/deep-learning-глубокое-обучение/)
- [NumPy (Библиотека для научных вычислений)](/en/terms/numpy-библиотека-для-научных-вычислений/)
