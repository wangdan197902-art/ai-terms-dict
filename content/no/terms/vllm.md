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
  - /no/terms/vllm/
date: "2026-07-18T16:20:46.332458Z"
lastmod: "2026-07-18T16:38:07.056883Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "vLLM er en inferenstmotor med høy gjennomstrømning og minneeffektivitet for store språkmodeller, som bruker PagedAttention for å optimalisere GPU-minnebruk."
---

## Definition

vLLM (Virtual Large Language Model) er et åpen kildekode-bibliotek designet for å akselerere levering av LLM-er. Det introduserer PagedAttention, en minnehåndteringsteknikk inspirert av operativsystemers virtuelle minne, som effektivt håndterer KV-cache og reduserer minneavfall.

### Summary

vLLM er en inferenstmotor med høy gjennomstrømning og minneeffektivitet for store språkmodeller, som bruker PagedAttention for å optimalisere GPU-minnebruk.

## Key Concepts

- PagedAttention
- KV-cache-håndtering
- Inferens-levering
- Gjennomstrømsoptimalisering

## Use Cases

- Levering av API-er med høy konkurrens
- Batch-prosessering av inferens
- Kostnadseffektiv distribusjon av LLM

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (NVIDIA-inferensplattform)](/en/terms/tensorrt-nvidia-inferensplattform/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (minneadministrasjonsalgoritme)](/en/terms/pagedattention-minneadministrasjonsalgoritme/)
- [LLM-levering](/en/terms/llm-levering/)
