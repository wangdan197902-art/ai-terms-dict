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
date: '2026-07-18T11:37:38.125342Z'
lastmod: '2026-07-18T11:44:44.997998Z'
draft: false
source: agnes_llm
status: published
language: de
description: vLLM ist eine hochdurchsatzorientierte und speichereffiziente Inferenz-Engine
  für Large Language Models, die PagedAttention nutzt, um die GPU-Speichernutzung
  zu optimieren.
---
## Definition

vLLM (Virtual Large Language Model) ist eine Open-Source-Bibliothek, die darauf ausgelegt ist, das Serving von LLMs zu beschleunigen. Es führt PagedAttention ein, eine Speichermanagement-Technik, die von der virtuellen Speicherverwaltung von Be

### Summary

vLLM ist eine hochdurchsatzorientierte und speichereffiziente Inferenz-Engine für Large Language Models, die PagedAttention nutzt, um die GPU-Speichernutzung zu optimieren.

## Key Concepts

- PagedAttention
- KV-Cache-Management
- Inferenz-Serving
- Durchsatzoptimierung

## Use Cases

- Serving von APIs mit hoher Parallelität
- Batch-Verarbeitung von Inferenzen
- Kosteneffiziente Bereitstellung von LLMs

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (Optimierungs-Toolkit)](/en/terms/tensorrt-optimierungs-toolkit/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (Seitenbasierte Aufmerksamkeit)](/en/terms/pagedattention-seitenbasierte-aufmerksamkeit/)
- [LLM Serving (Bereitstellung von LLMs)](/en/terms/llm-serving-bereitstellung-von-llms/)
