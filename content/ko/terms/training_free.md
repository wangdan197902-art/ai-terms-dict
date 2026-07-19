---
title: "훈련 불필요(Training-free)"
term_id: "training_free"
category: "training_techniques"
subcategory: ""
tags: ["techniques", "efficiency"]
difficulty: 3
weight: 1
slug: "training_free"
date: "2026-07-18T15:32:52.125875Z"
lastmod: "2026-07-18T16:38:06.791959Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "그래디언트 기반의 파라미터 업데이트 없이 모델을 적응하거나 향상시키는 방법론입니다."
---
## Definition

훈련 불필요 접근법은 역전파를 통해 기본 가중치를 업데이트하지 않고 모델의 동작이나 출력을 수정하는 기법을 지칭합니다. 이러한 방법은 종종 프롬프트 엔지니어링이나 사전 학습된 특징 추출 등을 활용하여 낮은 비용으로 새로운 작업에 적응합니다.

### Summary

그래디언트 기반의 파라미터 업데이트 없이 모델을 적응하거나 향상시키는 방법론입니다.

## Key Concepts

- 프롬프트 엔지니어링(Prompt engineering)
- 그래디언트 디센트 미사용(No gradient descent)
- 파라미터 효율성(Parameter-efficient)
- 제로 비용 적응(Zero-cost adaptation)

## Use Cases

- 프롬프팅을 통한 퓨샷 학습(Few-shot learning)
- 파인튜닝 없이 수행하는 도메인 적응
- LLM 애플리케이션의 신속한 프로토타이핑

## Related Terms

- [prompting (프롬프팅)](/en/terms/prompting-프롬프팅/)
- [fine_tuning (파인튜닝)](/en/terms/fine_tuning-파인튜닝/)
- [in_context_learning (컨텍스트 내 학습)](/en/terms/in_context_learning-컨텍스트-내-학습/)
