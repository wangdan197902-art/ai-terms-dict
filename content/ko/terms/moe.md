---
title: "전문가 혼합 (Mixture of Experts)"
term_id: "moe"
category: "basic_concepts"
subcategory: ""
tags: ["Architecture", "Efficiency", "LLMs"]
difficulty: 4
weight: 1
slug: "moe"
date: "2026-07-18T16:06:06.322285Z"
lastmod: "2026-07-18T16:38:06.886686Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "여러 개의 특수화된 신경망(전문가)이 게이트 메커니즘을 통해 결합되어 입력을 처리하는 아키텍처 패턴입니다."
---
## Definition

전문가 혼합(MoE)은 효율성과 확장성을 향상시키기 위해 설계된 머신러닝 아키텍처입니다. MoE는 모든 작업에 단일 대형 모델을 사용하는 대신, 여러 개의 작은 '전문가' 네트워크를 사용합니다.

### Summary

여러 개의 특수화된 신경망(전문가)이 게이트 메커니즘을 통해 결합되어 입력을 처리하는 아키텍처 패턴입니다.

## Key Concepts

- 희소 활성화
- 게이트 네트워크
- 전문가 특화
- 확장성

## Use Cases

- 대형 언어 모델의 효율적인 학습
- 대규모 모델의 추론 지연 시간 감소
- 멀티모달 시스템에서 다양한 입력 유형 처리

## Related Terms

- [Sparse Transformers (희소 트랜스포머)](/en/terms/sparse-transformers-희소-트랜스포머/)
- [Conditional Computation (조건부 계산)](/en/terms/conditional-computation-조건부-계산/)
- [Large Language Models (대형 언어 모델)](/en/terms/large-language-models-대형-언어-모델/)
- [Neural Architecture Search (신경망 아키텍처 검색)](/en/terms/neural-architecture-search-신경망-아키텍처-검색/)
