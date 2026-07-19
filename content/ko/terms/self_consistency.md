---
title: "자기 일관성(Self-Consistency)"
term_id: "self_consistency"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "inference", "technique"]
difficulty: 4
weight: 1
slug: "self_consistency"
date: "2026-07-18T16:14:49.554374Z"
lastmod: "2026-07-18T16:38:06.906339Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "여러 추론 경로를 샘플링하여 가장 빈번하게 나타나는 답변을 최종 출력으로 선택하는 디코딩 전략입니다."
---
## Definition

주로 대규모 언어 모델(LLM)에서 사용되는 이 기법은 샘플링을 통해 프롬프트에 대해 다양한 응답을 여러 개 생성함으로써 정확도를 향상시킵니다. 탐욕적 디코딩(Greedy decoding)에 의존하는 대신, 생성된 여러 답변 중에서 다수결 원칙을 적용하여 가장 일관성 있는 결과를 선택합니다.

### Summary

여러 추론 경로를 샘플링하여 가장 빈번하게 나타나는 답변을 최종 출력으로 선택하는 디코딩 전략입니다.

## Key Concepts

- 다수결 투표(Majority voting)
- 디코딩 전략(Decoding strategy)
- LLM 추론(LLM reasoning)
- 환각 현상 감소(Hallucination reduction)

## Use Cases

- 수학적 응용 문제(Mathematical word problems)
- 복잡한 논리적 추론(Complex logical deduction)
- 코드 생성 작업(Code synthesis tasks)

## Related Terms

- [Chain-of-thought (사슬 사고: 단계별 추론 유도)](/en/terms/chain-of-thought-사슬-사고-단계별-추론-유도/)
- [Temperature sampling (온도 샘플링: 생성의 다양성 조절)](/en/terms/temperature-sampling-온도-샘플링-생성의-다양성-조절/)
- [Ensemble methods (앙상블 방법: 여러 모델 결합)](/en/terms/ensemble-methods-앙상블-방법-여러-모델-결합/)
- [Prompt engineering (프롬프트 엔지니어링: 입력 최적화)](/en/terms/prompt-engineering-프롬프트-엔지니어링-입력-최적화/)
