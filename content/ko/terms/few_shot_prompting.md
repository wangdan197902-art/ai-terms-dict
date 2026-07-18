---
title: "퓨 샷 프롬프팅"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /ko/terms/few_shot_prompting/
date: "2026-07-18T15:34:33.739670Z"
lastmod: "2026-07-18T16:38:06.795241Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "퓨 샷 프롬프팅은 대규모 언어 모델(LLM)에게 프롬프트 내에 소수의 입력-출력 예시를 제공하여 모델의 동작을 유도하는 기법입니다."
---

## Definition

이 방법은 프롬프트 내에 직접적인 설명 예시를 몇 개 제공함으로써 대규모 언어 모델의 문맥 내 학습(In-context learning) 능력을 활용합니다. 모델의 가중치를 업데이트해야 하는 파인튜닝(Fine-tuning)과는 달리, 퓨 샷 프롬프팅은 추가적인 훈련 없이도 모델이 특정 작업 형식이나 스타일을 빠르게 습득하도록 돕습니다.

### Summary

퓨 샷 프롬프팅은 대규모 언어 모델(LLM)에게 프롬프트 내에 소수의 입력-출력 예시를 제공하여 모델의 동작을 유도하는 기법입니다.

## Key Concepts

- 문맥 내 학습
- 프롬프트 엔지니어링
- 예시 기반 안내
- 제로 샷 비교

## Use Cases

- 감성 분석 결과 포맷팅
- 코드 스타일 적응
- 구조화된 데이터 추출

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (제로 샷: 예시 없이 수행)](/en/terms/zero_shot-제로-샷-예시-없이-수행/)
- [prompt_engineering (프롬프트 엔지니어링: 프롬프트 설계)](/en/terms/prompt_engineering-프롬프트-엔지니어링-프롬프트-설계/)
- [in_context_learning (문맥 내 학습: 외부 학습 없이 프롬프트 내에서 학습)](/en/terms/in_context_learning-문맥-내-학습-외부-학습-없이-프롬프트-내에서-학습/)
- [llm (대규모 언어 모델)](/en/terms/llm-대규모-언어-모델/)
