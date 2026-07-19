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
date: '2026-07-18T16:21:27.232745Z'
lastmod: '2026-07-18T17:15:08.796900Z'
draft: false
source: agnes_llm
status: published
language: nl
description: vLLM is een inferentie-engine met hoge doorvoer en efficiënt geheugengebruik
  voor Large Language Models, die PagedAttention gebruikt om het GPU-geheugengebruik
  te optimaliseren.
---
## Definition

vLLM (Virtual Large Language Model) is een open-source bibliotheek die is ontworpen om het serveren van LLM's te versnellen. Het introduceert PagedAttention, een techniek voor geheugenbeheer geïnspireerd door virtueel geheugen in besturingssystemen, wat leidt tot efficiënter gebruik van GPU-geheugen en hogere doorvoer.

### Summary

vLLM is een inferentie-engine met hoge doorvoer en efficiënt geheugengebruik voor Large Language Models, die PagedAttention gebruikt om het GPU-geheugengebruik te optimaliseren.

## Key Concepts

- PagedAttention
- KV-cachebeheer
- Inferentieservering
- Doorvoeroptimalisatie

## Use Cases

- Servering van API's met hoge gelijktijdigheid
- Batchgewijze verwerking van inferenties
- Kostenefficiënte implementatie van LLM's

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (inference-optimalisatie toolkit)](/en/terms/tensorrt-inference-optimalisatie-toolkit/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (geheugenbeheertechniek)](/en/terms/pagedattention-geheugenbeheertechniek/)
- [LLM Serving (serveren van grote taalmodellen)](/en/terms/llm-serving-serveren-van-grote-taalmodellen/)
