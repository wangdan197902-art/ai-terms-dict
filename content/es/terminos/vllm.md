---
title: "vLLM"
term_id: "vllm"
category: "application_paradigms"
subcategory: ""
tags: ["inference", "optimization", "serving", "library"]
difficulty: 4
weight: 1
slug: "vllm"
aliases:
  - /es/terms/vllm/
date: "2026-07-18T11:12:55.053427Z"
lastmod: "2026-07-18T11:44:44.864533Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "vLLM es un motor de inferencia de alto rendimiento y eficiente en memoria para modelos de lenguaje grandes, que utiliza PagedAttention para optimizar el uso de la memoria de la GPU."
---

## Definition

vLLM (Virtual Large Language Model) es una biblioteca de código abierto diseñada para acelerar el servicio de LLM. Introduce PagedAttention, una técnica de gestión de memoria inspirada en la memoria virtual de los sistemas operativos, lo que permite un manejo más eficiente de la caché KV y mayor concurrencia.

### Summary

vLLM es un motor de inferencia de alto rendimiento y eficiente en memoria para modelos de lenguaje grandes, que utiliza PagedAttention para optimizar el uso de la memoria de la GPU.

## Key Concepts

- PagedAttention
- Gestión de caché KV
- Servicio de inferencia
- Optimización de rendimiento

## Use Cases

- Servicio de APIs de alta concurrencia
- Procesamiento de inferencia por lotes
- Despliegue de LLM rentable

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (optimizador de inferencia de NVIDIA)](/en/terms/tensorrt-optimizador-de-inferencia-de-nvidia/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (mecanismo de atención paginada)](/en/terms/pagedattention-mecanismo-de-atención-paginada/)
- [Servicio de LLM (despliegue de modelos)](/en/terms/servicio-de-llm-despliegue-de-modelos/)
