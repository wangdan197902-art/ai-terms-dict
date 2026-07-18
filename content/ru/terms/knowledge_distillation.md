---
title: "Дистилляция знаний"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /ru/terms/knowledge_distillation/
date: "2026-07-18T16:00:04.564300Z"
lastmod: "2026-07-18T16:38:07.171822Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Дистилляция знаний — это техника сжатия модели, при которой меньшая модель-ученик учится имитировать поведение большей модели-учителя."
---

## Definition

Дистилляция знаний — это метод машинного обучения, используемый для сжатия крупной сложной нейронной сети (учителя) в более маленькую и эффективную сеть (ученика). Модель-ученик обучается воспроизводить...

### Summary

Дистилляция знаний — это техника сжатия модели, при которой меньшая модель-ученик учится имитировать поведение большей модели-учителя.

## Key Concepts

- Модель учитель-ученик
- Сжатие модели
- Мягкие цели (Soft Targets)
- Эффективность

## Use Cases

- Развертывание моделей на периферийных устройствах
- Снижение задержки вывода
- Снижение затрат на облачные вычисления

## Code Example

```python
import torch
import torch.nn as nn

def distillation_loss(student_logits, teacher_logits, temperature=2.0):
    T = temperature
    student_probs = nn.functional.softmax(student_logits / T, dim=1)
    teacher_probs = nn.functional.softmax(teacher_logits / T, dim=1)
    return nn.functional.kl_div(
        nn.functional.log_softmax(student_logits / T, dim=1),
        teacher_probs,
        reduction='batchmean'
    ) * (T * T)
```

## Related Terms

- [Model Compression (Сжатие модели)](/en/terms/model-compression-сжатие-модели/)
- [Pruning (Отсечение)](/en/terms/pruning-отсечение/)
- [Quantization (Квантование)](/en/terms/quantization-квантование/)
- [Neural Networks (Нейронные сети)](/en/terms/neural-networks-нейронные-сети/)
