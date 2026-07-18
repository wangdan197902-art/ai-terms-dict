---
title: "MobileNet"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
aliases:
  - /ru/terms/mobilenet/
date: "2026-07-18T16:06:07.285564Z"
lastmod: "2026-07-18T16:38:07.181239Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "MobileNet — это семейство легких глубоких нейронных сетей, разработанных для мобильных и встроенных систем компьютерного зрения."
---

## Definition

MobileNet использует глубинные сепарабельные свертки, что позволяет значительно снизить вычислительные затраты и размер модели по сравнению со стандартными сверточными операциями. Такая архитектура обеспечивает эффективное извлечение признаков на

### Summary

MobileNet — это семейство легких глубоких нейронных сетей, разработанных для мобильных и встроенных систем компьютерного зрения.

## Key Concepts

- Глубинные сепарабельные свертки
- Эффективность модели
- Периферийные вычисления
- Перенос обучения

## Use Cases

- Обнаружение объектов в реальном времени на смартфонах
- Классификация изображений на устройствах Интернета вещей
- Распознавание лиц в мобильных приложениях

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (архитектура нейронной сети)](/en/terms/shufflenet-архитектура-нейронной-сети/)
- [SqueezeNet (легкая сверточная сеть)](/en/terms/squeezenet-легкая-сверточная-сеть/)
- [EfficientNet (эффективная архитектура CNN)](/en/terms/efficientnet-эффективная-архитектура-cnn/)
- [Сверточная нейронная сеть](/en/terms/сверточная-нейронная-сеть/)
