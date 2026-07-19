---
title: 롱 컨텍스트(Long Context)
term_id: long_context
category: basic_concepts
subcategory: ''
tags:
- NLP
- transformers
- architecture
difficulty: 2
weight: 1
slug: long_context
date: '2026-07-18T16:03:15.502036Z'
lastmod: '2026-07-18T16:38:06.868980Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 수천 개 또는 수백만 개의 토큰으로 구성된 입력 시퀀스에서 정보를 처리하고 유지할 수 있는 언어 모델의 능력.
---
## Definition

롱 컨텍스트는 트랜스포머 기반 모델이 표준 제한(예: 2k 또는 4k 토큰)을 종종 초과하는 광범위한 입력 길이를 처리할 수 있는 능력을 의미합니다. 이 기능은 모델이 전체

### Summary

수천 개 또는 수백만 개의 토큰으로 구성된 입력 시퀀스에서 정보를 처리하고 유지할 수 있는 언어 모델의 능력.

## Key Concepts

- 컨텍스트 윈도우(Context Window)
- 토큰 제한(Token Limit)
- 어텐션 메커니즘(Attention Mechanism)
- 위치 인코딩(Positional Encoding)

## Use Cases

- 전체 법적 계약서 요약
- 완전한 소스 코드 저장소 분석
- 장편 오디오 트랜스크립트 처리

## Related Terms

- [Context Window (컨텍스트 윈도우)](/en/terms/context-window-컨텍스트-윈도우/)
- [Transformer Architecture (트랜스포머 아키텍처)](/en/terms/transformer-architecture-트랜스포머-아키텍처/)
- [RoPE (Rotary Positional Embeddings) (회전 위치 임베딩)](/en/terms/rope-rotary-positional-embeddings-회전-위치-임베딩/)
- [KV Cache (KV 캐시)](/en/terms/kv-cache-kv-캐시/)
