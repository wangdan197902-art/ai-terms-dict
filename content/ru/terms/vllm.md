---
title: Vllm
term_id: vllm
category: application_paradigms
subcategory: ''
tags:
- inference
- Optimization
- serving
- library
difficulty: 4
weight: 1
slug: vllm
date: '2026-07-18T16:19:56.811101Z'
lastmod: '2026-07-18T16:38:07.212471Z'
draft: false
source: agnes_llm
status: published
language: ru
description: vLLM — это высокопроизводительный и эффективный по памяти движок инференса
  для больших языковых моделей, использующий технологию PagedAttention для оптимизации
  использования памяти GPU.
---
## Definition

vLLM (Virtual Large Language Model) — это библиотека с открытым исходным кодом, разработанная для ускорения обслуживания LLM. Она внедряет PagedAttention, технику управления памятью, вдохновленную виртуальной памятью операционных систем, что позволяет эффективно управлять KV-кэшем.

### Summary

vLLM — это высокопроизводительный и эффективный по памяти движок инференса для больших языковых моделей, использующий технологию PagedAttention для оптимизации использования памяти GPU.

## Key Concepts

- PagedAttention
- Управление KV-кэшем
- Сервисный инференс
- Оптимизация пропускной способности

## Use Cases

- Обслуживание API с высокой конкурентностью
- Пакетная обработка инференса
- Экономически эффективное развертывание LLM

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (библиотека оптимизации ИИ NVIDIA)](/en/terms/tensorrt-библиотека-оптимизации-ии-nvidia/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (алгоритм управления памятью)](/en/terms/pagedattention-алгоритм-управления-памятью/)
- [LLM Serving (сервисное обслуживание LLM)](/en/terms/llm-serving-сервисное-обслуживание-llm/)
