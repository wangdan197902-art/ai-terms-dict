---
title: "Самовнимание"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /ru/terms/self_attention/
date: "2026-07-18T15:29:19.618639Z"
lastmod: "2026-07-18T16:38:07.090255Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Механизм, позволяющий нейронной сети оценивать важность различных частей входной последовательности относительно друг друга."
---

## Definition

Самовнимание позволяет моделям одновременно выявлять зависимости между всеми позициями в последовательности, независимо от расстояния между ними. Вычисляя оценки внимания между каждой парой токенов, оно позволяет...

### Summary

Механизм, позволяющий нейронной сети оценивать важность различных частей входной последовательности относительно друг друга.

## Key Concepts

- Запрос-Ключ-Значение
- Оценки внимания
- Контекстное взвешивание
- Параллельная обработка

## Use Cases

- Машинный перевод
- Суммаризация текста
- Классификация изображений с помощью Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Трансформер)](/en/terms/transformer-трансформер/)
- [Multi-Head Attention (Многоголовое внимание)](/en/terms/multi-head-attention-многоголовое-внимание/)
- [Embeddings (Векторные представления)](/en/terms/embeddings-векторные-представления/)
- [Sequence Modeling (Моделирование последовательностей)](/en/terms/sequence-modeling-моделирование-последовательностей/)
