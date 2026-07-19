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
date: '2026-07-18T16:19:35.554110Z'
lastmod: '2026-07-18T16:38:07.665729Z'
draft: false
source: agnes_llm
status: published
language: th
description: vLLM คือเครื่องจักรอนุมานที่มีความเร็วสูงและใช้หน่วยความจำอย่างมีประสิทธิภาพสำหรับโมเดลภาษาขนาดใหญ่
  โดยใช้เทคนิค PagedAttention เพื่อปรับการใช้งานหน่วยความจำ GPU ให้เหมาะสม
---
## Definition

vLLM (Virtual Large Language Model) คือไลบรารีโอเพนซอร์สที่ออกแบบมาเพื่อเร่งความเร็วในการให้บริการโมเดลภาษาขนาดใหญ่ (LLM) โดยนำเสนอ PagedAttention ซึ่งเป็นเทคนิคการจัดการหน่วยความจำที่ได้รับแรงบันดาลใจจากระบบปฏิบัติการ

### Summary

vLLM คือเครื่องจักรอนุมานที่มีความเร็วสูงและใช้หน่วยความจำอย่างมีประสิทธิภาพสำหรับโมเดลภาษาขนาดใหญ่ โดยใช้เทคนิค PagedAttention เพื่อปรับการใช้งานหน่วยความจำ GPU ให้เหมาะสม

## Key Concepts

- PagedAttention
- การจัดการ KV Cache
- การให้บริการอนุมาน
- การเพิ่มประสิทธิภาพปริมาณงาน

## Use Cases

- การให้บริการ API ที่รองรับการเชื่อมต่อพร้อมกันสูง
- การประมวลผลอนุมานแบบแบทช์
- การนำโมเดลภาษาขนาดใหญ่ไปใช้งานอย่างคุ้มค่า

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (ไลบรารีเพิ่มประสิทธิภาพ inference ของ NVIDIA)](/en/terms/tensorrt-ไลบราร-เพ-มประส-ทธ-ภาพ-inference-ของ-nvidia/)
- [TGI (Text Generation Inference ของ Hugging Face)](/en/terms/tgi-text-generation-inference-ของ-hugging-face/)
- [PagedAttention (เทคนิคการจัดการหน่วยความจำ)](/en/terms/pagedattention-เทคน-คการจ-ดการหน-วยความจำ/)
- [LLM Serving (การให้บริการโมเดลภาษาขนาดใหญ่)](/en/terms/llm-serving-การให-บร-การโมเดลภาษาขนาดใหญ/)
