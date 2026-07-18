---
title: "Позиционное кодирование"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /ru/terms/positional_encoding/
date: "2026-07-18T15:35:53.227250Z"
lastmod: "2026-07-18T16:38:07.108784Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Техника, которая внедряет информацию о относительном или абсолютном положении токенов в последовательность в модели трансформеров."
---

## Definition

Поскольку трансформеры обрабатывают все токены параллельно, а не последовательно, как рекуррентные нейронные сети (RNN), они лишены встроенного понимания порядка следования токенов. Позиционное кодирование добавляет специфические векторы к входным эмбеддингам, чтобы предоставить модели информацию о позиции каждого токена в последовательности.

### Summary

Техника, которая внедряет информацию о относительном или абсолютном положении токенов в последовательность в модели трансформеров.

## Key Concepts

- Порядок последовательности
- Самовнимание
- Синусоидальные функции
- Эмбеддинги токенов

## Use Cases

- Машинный перевод
- Суммаризация текста
- Языковое моделирование

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Архитектура трансформера](/en/terms/архитектура-трансформера/)
- [Эмбеддинг](/en/terms/эмбеддинг/)
- [Механизм внимания](/en/terms/механизм-внимания/)
- [RoPE (Rotary Positional Embedding)](/en/terms/rope-rotary-positional-embedding/)
