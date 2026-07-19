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
date: '2026-07-18T11:37:39.249169Z'
lastmod: '2026-07-18T11:44:45.566881Z'
draft: false
source: agnes_llm
status: published
language: zh
description: vLLM 是一个高吞吐量且内存高效的 LLM 推理引擎，利用 PagedAttention 优化 GPU 内存使用。
---
## Definition

vLLM（Virtual Large Language Model）是一个旨在加速 LLM 服务的开源库。它引入了 PagedAttention，这是一种受操作系统虚拟内存

### Summary

vLLM 是一个高吞吐量且内存高效的 LLM 推理引擎，利用 PagedAttention 优化 GPU 内存使用。

## Key Concepts

- PagedAttention
- KV Cache 管理
- 推理服务
- 吞吐量优化

## Use Cases

- 高并发 API 服务
- 批处理推理处理
- 具有成本效益的 LLM 部署

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (NVIDIA 推理优化库)](/en/terms/tensorrt-nvidia-推理优化库/)
- [TGI (文本生成推理服务器)](/en/terms/tgi-文本生成推理服务器/)
- [PagedAttention (分页注意力机制)](/en/terms/pagedattention-分页注意力机制/)
- [LLM Serving (LLM 服务化)](/en/terms/llm-serving-llm-服务化/)
