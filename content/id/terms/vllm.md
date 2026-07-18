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
  - /id/terms/vllm/
date: "2026-07-18T16:12:47.315725Z"
lastmod: "2026-07-18T16:38:07.518069Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "vLLM adalah mesin inferensi ber throughput tinggi dan hemat memori untuk Model Bahasa Besar, yang memanfaatkan PagedAttention untuk mengoptimalkan penggunaan memori GPU."
---

## Definition

vLLM (Virtual Large Language Model) adalah pustaka sumber terbuka yang dirancang untuk mempercepat penyajian LLM. Alat ini memperkenalkan PagedAttention, sebuah teknik manajemen memori yang terinspirasi oleh memori virtual sistem operasi

### Summary

vLLM adalah mesin inferensi ber throughput tinggi dan hemat memori untuk Model Bahasa Besar, yang memanfaatkan PagedAttention untuk mengoptimalkan penggunaan memori GPU.

## Key Concepts

- PagedAttention
- Manajemen KV Cache
- Penyajian Inferensi
- Optimasi Throughput

## Use Cases

- Penyajian API dengan konkurensi tinggi
- Pemrosesan inferensi batch
- Penyebaran LLM yang hemat biaya

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (Pustaka optimasi inferensi NVIDIA)](/en/terms/tensorrt-pustaka-optimasi-inferensi-nvidia/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (Teknik manajemen memori)](/en/terms/pagedattention-teknik-manajemen-memori/)
- [LLM Serving (Penyajian Model Bahasa Besar)](/en/terms/llm-serving-penyajian-model-bahasa-besar/)
