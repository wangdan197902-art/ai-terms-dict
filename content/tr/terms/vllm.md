---
title: vLLM
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
date: '2026-07-18T16:20:31.655082Z'
lastmod: '2026-07-18T16:38:07.376366Z'
draft: false
source: agnes_llm
status: published
language: tr
description: vLLM, PagedAttention kullanarak GPU bellek kullanımını optimize eden
  Büyük Dil Modelleri için yüksek verimli ve bellek verimli bir çıkarım motorudur.
---
## Definition

vLLM (Virtual Large Language Model), LLM sunumunu hızlandırmak için tasarlanmış açık kaynaklı bir kütüphanedir. İşletim sistemlerinin sanal bellek yönetiminden ilham alan PagedAttention adlı bir bellek yönetimi tekniği tanıtır.

### Summary

vLLM, PagedAttention kullanarak GPU bellek kullanımını optimize eden Büyük Dil Modelleri için yüksek verimli ve bellek verimli bir çıkarım motorudur.

## Key Concepts

- PagedAttention
- KV Önbellek Yönetimi
- Çıkarım Sunumu
- Verimlilik Optimizasyonu

## Use Cases

- Yüksek eşzamanlılıkta API sunumu
- Toplu çıkarım işleme
- Maliyet etkin LLM dağıtımı

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (NVIDIA Derin Öğrenme Optimizasyon Kütüphanesi)](/en/terms/tensorrt-nvidia-derin-öğrenme-optimizasyon-kütüphanesi/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention](/en/terms/pagedattention/)
- [LLM Sunumu](/en/terms/llm-sunumu/)
