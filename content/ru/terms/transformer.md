---
title: Трансформер
term_id: transformer
category: basic_concepts
subcategory: ''
tags:
- architecture
- NLP
- attention
difficulty: 4
weight: 1
slug: transformer
date: '2026-07-18T15:30:21.397017Z'
lastmod: '2026-07-18T16:38:07.092573Z'
draft: false
source: agnes_llm
status: published
language: ru
description: Архитектура глубокого обучения, основанная на механизмах самовнимания,
  которая обрабатывает последовательные данные параллельно, а не последовательно.
---
## Definition

Впервые представленная в статье «Attention Is All You Need», архитектура трансформера произвела революцию в обработке естественного языка и не только. Она использует многоголовое самовнимание для оценки значимости

### Summary

Архитектура глубокого обучения, основанная на механизмах самовнимания, которая обрабатывает последовательные данные параллельно, а не последовательно.

## Key Concepts

- Самовнимание
- Многоголовое внимание
- Позиционное кодирование
- Структура энкодер-декодер

## Use Cases

- Машинный перевод
- Генерация текста
- Распознавание изображений (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (механизм внимания)](/en/terms/attention_mechanism-механизм-внимания/)
- [bert (BERT)](/en/terms/bert-bert/)
- [gpt (GPT)](/en/terms/gpt-gpt/)
- [self_attention (самовнимание)](/en/terms/self_attention-самовнимание/)
