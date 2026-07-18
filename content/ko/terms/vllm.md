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
  - /ko/terms/vllm/
date: "2026-07-18T16:20:07.434045Z"
lastmod: "2026-07-18T16:38:06.918784Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "vLLM은 PagedAttention을 활용하여 GPU 메모리 사용을 최적화하는 대규모 언어 모델(LLM)용 고속 처리 및 메모리 효율적인 추론 엔진입니다."
---

## Definition

vLLM(가상 대규모 언어 모델)은 LLM 서빙을 가속화하기 위해 설계된 오픈소스 라이브러리입니다. 이는 운영 체제의 가상 메모리에서 영감을 받은 메모리 관리 기법인 PagedAttention을 도입합니다.

### Summary

vLLM은 PagedAttention을 활용하여 GPU 메모리 사용을 최적화하는 대규모 언어 모델(LLM)용 고속 처리 및 메모리 효율적인 추론 엔진입니다.

## Key Concepts

- 페이징 어텐션(PagedAttention)
- KV 캐시 관리
- 추론 서빙
- 처리량 최적화

## Use Cases

- 고동시성 API 서빙
- 배치 처리 추론
- 비용 효율적인 LLM 배포

## Code Example

```python
from vllm import LLM, SamplingParams
llm = LLM(model="facebook/opt-125m")
prompts = ["Hello, my name is", "The capital of France is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
outputs = llm.generate(prompts, sampling_params)
```

## Related Terms

- [TensorRT (텐서RT)](/en/terms/tensorrt-텐서rt/)
- [TGI (텍스트 생성 인퍼런스)](/en/terms/tgi-텍스트-생성-인퍼런스/)
- [PagedAttention (페이징 어텐션)](/en/terms/pagedattention-페이징-어텐션/)
- [LLM Serving (LLM 서빙)](/en/terms/llm-serving-llm-서빙/)
