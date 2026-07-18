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
  - /vi/terms/vllm/
date: "2026-07-18T16:15:44.786976Z"
lastmod: "2026-07-18T16:38:07.815610Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "vLLM là một công cụ suy luận có thông lượng cao và hiệu quả bộ nhớ cho các Mô hình Ngôn ngữ Lớn, sử dụng cơ chế PagedAttention để tối ưu hóa việc sử dụng bộ nhớ GPU."
---

## Definition

vLLM (Virtual Large Language Model) là một thư viện mã nguồn mở được thiết kế để tăng tốc việc triển khai LLM. Nó giới thiệu PagedAttention, một kỹ thuật quản lý bộ nhớ lấy cảm hứng từ bộ nhớ ảo trong hệ điều hành...

### Summary

vLLM là một công cụ suy luận có thông lượng cao và hiệu quả bộ nhớ cho các Mô hình Ngôn ngữ Lớn, sử dụng cơ chế PagedAttention để tối ưu hóa việc sử dụng bộ nhớ GPU.

## Key Concepts

- PagedAttention
- Quản lý Bộ nhớ Cache KV
- Triển khai Suy luận
- Tối ưu hóa Thông lượng

## Use Cases

- Triển khai API chịu tải cao
- Xử lý suy luận theo lô
- Triển khai LLM tiết kiệm chi phí

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (Công cụ tối ưu hóa inference)](/en/terms/tensorrt-công-cụ-tối-ưu-hóa-inference/)
- [TGI (Text Generation Inference)](/en/terms/tgi-text-generation-inference/)
- [PagedAttention (Cơ chế quản lý bộ nhớ)](/en/terms/pagedattention-cơ-chế-quản-lý-bộ-nhớ/)
- [Triển khai LLM](/en/terms/triển-khai-llm/)
