---
title: PagedAttention
term_id: pagedattention
category: training_techniques
subcategory: ''
tags:
- inference
- Optimization
- Memory Management
difficulty: 4
weight: 1
slug: pagedattention
date: '2026-07-18T16:08:54.598698Z'
lastmod: '2026-07-18T16:38:06.894339Z'
draft: false
source: agnes_llm
status: published
language: ko
description: PagedAttention는 가상 메모리 페이징 개념을 적용하여 트랜스포머 모델의 키-값(KV) 캐시 저장 및 접근을 최적화하는
  메모리 관리 알고리즘입니다.
---
## Definition

PagedAttention는 vLLM 프로젝트에서 도입된 기법으로, 대규모 언어 모델(LLM) 추론의 효율성을 개선합니다. 이는 KV 캐시를 관리할 때 발생하는 단편화 및 오버헤드 문제를 해결하며, 메모리 사용량을 크게...

### Summary

PagedAttention는 가상 메모리 페이징 개념을 적용하여 트랜스포머 모델의 키-값(KV) 캐시 저장 및 접근을 최적화하는 메모리 관리 알고리즘입니다.

## Key Concepts

- KV 캐시 관리
- 메모리 단편화
- 추론 최적화
- 가상 메모리 페이징

## Use Cases

- 고속 처리 LLM 서빙
- GPU 메모리 사용량 절감
- 프로덕션 환경의 배치 처리 최적화

## Related Terms

- [vLLM (vLLM 라이브러리)](/en/terms/vllm-vllm-라이브러리/)
- [Key-Value Cache (키-값 캐시)](/en/terms/key-value-cache-키-값-캐시/)
- [Transformer Architecture (트랜스포머 아키텍처)](/en/terms/transformer-architecture-트랜스포머-아키텍처/)
- [GPU Memory Optimization (GPU 메모리 최적화)](/en/terms/gpu-memory-optimization-gpu-메모리-최적화/)
