---
title: "Извлечение модели (Model Extraction)"
term_id: "model_extraction"
category: "ethics_safety"
subcategory: ""
tags: ["security", "adversarial_ml"]
difficulty: 4
weight: 1
slug: "model_extraction"
aliases:
  - /ru/terms/model_extraction/
date: "2026-07-18T16:21:07.577408Z"
lastmod: "2026-07-18T16:38:07.215894Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Атака, при которой злоумышленник запрашивает модель для восстановления ее параметров или создания копии."
---

## Definition

Извлечение модели включает отправку запросов к API целевой модели машинного обучения для вывода ее внутренней структуры, весов или границ принятия решений. Злоумышленники используют эти запросы для построения суррогатной модели, которая ведет себя аналогично оригиналу.

### Summary

Атака, при которой злоумышленник запрашивает модель для восстановления ее параметров или создания копии.

## Key Concepts

- Суррогатное моделирование
- Запросы к API
- Кража интеллектуальной собственности
- Вредоносная атака (Adversarial Attack)

## Use Cases

- Аудит безопасности коммерческих API искусственного интеллекта
- Защита проприетарных алгоритмов от клонирования
- Исследование механизмов защиты от извлечения моделей

## Related Terms

- [Membership Inference (Вывод о принадлежности к выборке)](/en/terms/membership-inference-вывод-о-принадлежности-к-выборке/)
- [Adversarial Examples (Вредоносные примеры)](/en/terms/adversarial-examples-вредоносные-примеры/)
- [Model Watermarking (Водяные знаки в моделях)](/en/terms/model-watermarking-водяные-знаки-в-моделях/)
- [API Security (Безопасность API)](/en/terms/api-security-безопасность-api/)
