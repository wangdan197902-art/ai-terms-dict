---
title: "LoRA (Low-Rank Adaptation)"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
aliases:
  - /ru/terms/lora/
date: "2026-07-18T15:26:33.915295Z"
lastmod: "2026-07-18T16:38:07.081085Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Адаптация низкого ранга — метод эффективной по параметрам дообучения, внедряющий обучаемые матрицы разложения ранга в существующие веса модели."
---

## Definition

LoRA фиксирует предварительно обученные веса модели и вставляет обучаемые матрицы разложения в каждый слой архитектуры трансформера. Оптимизируя только эти матрицы низкого ранга, LoRA значительно снижает

### Summary

Адаптация низкого ранга — метод эффективной по параметрам дообучения, внедряющий обучаемые матрицы разложения ранга в существующие веса модели.

## Key Concepts

- Эффективное по параметрам дообучение (PEFT)
- Разложение ранга
- Фиксация весов
- Модули-адаптеры

## Use Cases

- Кастомизация больших языковых моделей
- Адаптация под конкретную предметную область
- Обучение при ограниченных ресурсах

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Дообучение (Fine-Tuning)](/en/terms/дообучение-fine-tuning/)
- [Квантование](/en/terms/квантование/)
