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
  - /pl/terms/vllm/
date: "2026-07-18T16:21:51.695460Z"
lastmod: "2026-07-18T17:15:08.927512Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "vLLM to silnik wnioskowania o wysokiej przepustowości i efektywnym zużyciu pamięci dla dużych modeli językowych, wykorzystujący PagedAttention do optymalizacji użycia pamięci GPU."
---

## Definition

vLLM (Virtual Large Language Model) to biblioteka open-source zaprojektowana w celu przyspieszenia usługi (serving) LLM. Wprowadza ona PagedAttention, technikę zarządzania pamięcią inspirowaną wirtualną pamięcią systemów operacyjnych

### Summary

vLLM to silnik wnioskowania o wysokiej przepustowości i efektywnym zużyciu pamięci dla dużych modeli językowych, wykorzystujący PagedAttention do optymalizacji użycia pamięci GPU.

## Key Concepts

- PagedAttention
- Zarządzanie buforem KV
- Usługiwnienie wnioskowania
- Optymalizacja przepustowości

## Use Cases

- Obsługa API o wysokiej konkurencji
- Przetwarzanie wsadowe wnioskowań
- Kosztoefektywne wdrażanie LLM

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (optymalizator inferencji NVIDIA)](/en/terms/tensorrt-optymalizator-inferencji-nvidia/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (mechanizm zarządzania pamięcią)](/en/terms/pagedattention-mechanizm-zarządzania-pamięcią/)
- [Usługiwnienie LLM](/en/terms/usługiwnienie-llm/)
