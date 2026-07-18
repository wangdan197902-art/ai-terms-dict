---
title: "Vllm"
term_id: "vllm"
category: "application_paradigms"
subcategory: ""
tags: ["inference", "optimization", "serving", "library"]
difficulty: 4
weight: 1
slug: "vllm"
aliases:
  - /pt/terms/vllm/
date: "2026-07-18T15:26:39.509729Z"
lastmod: "2026-07-18T15:51:59.541307Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "O vLLM é um mecanismo de inferência de alta taxa de transferência e eficiente em memória para Grandes Modelos de Linguagem, utilizando PagedAttention para otimizar o uso de memória da GPU."
---

## Definition

O vLLM (Virtual Large Language Model) é uma biblioteca de código aberto projetada para acelerar o serviço de LLMs. Ele introduz o PagedAttention, uma técnica de gerenciamento de memória inspirada na memória virtual de sistemas operacionais

### Summary

O vLLM é um mecanismo de inferência de alta taxa de transferência e eficiente em memória para Grandes Modelos de Linguagem, utilizando PagedAttention para otimizar o uso de memória da GPU.

## Key Concepts

- PagedAttention
- Gerenciamento de Cache KV
- Serviço de Inferência
- Otimização de Taxa de Transferência

## Use Cases

- Serviço de APIs de alta concorrência
- Processamento de inferência em lotes
- Implantação de LLMs com baixo custo

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT](/en/terms/tensorrt/)
- [TGI](/en/terms/tgi/)
- [PagedAttention](/en/terms/pagedattention/)
- [LLM Serving (Serviço de LLMs)](/en/terms/llm-serving-serviço-de-llms/)
