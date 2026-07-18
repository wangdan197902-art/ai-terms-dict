---
title: "P-Tuning"
term_id: "p_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "nlp"]
difficulty: 4
weight: 1
slug: "p_tuning"
aliases:
  - /ko/terms/p_tuning/
date: "2026-07-18T16:08:40.266602Z"
lastmod: "2026-07-18T16:38:06.893948Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "전체 사전 훈련된 모델 가중치를 업데이트하는 대신 연속적인 프롬프트 임베딩을 최적화하는 매개변수 효율적 파인튜닝 방법."
---

## Definition

P-Tuning(프롬프트 튜닝)은 최소한의 계산 비용으로 대규모 사전 훈련된 언어 모델을 특정 다운스트림 작업에 적응시키기 위해 설계된 기술입니다. 모든 모델 매개변수를 미세 조정하는 대신, 고정된 가중치 위에 가상 토큰(virtual tokens)이나 임베딩을 최적화하여 작업을 수행합니다.

### Summary

전체 사전 훈련된 모델 가중치를 업데이트하는 대신 연속적인 프롬프트 임베딩을 최적화하는 매개변수 효율적 파인튜닝 방법.

## Key Concepts

- 매개변수 효율적 파인튜닝
- 가상 토큰
- 고정 가중치
- 임베딩 최적화

## Use Cases

- 소량 학습(few-shot learning) 적응
- 자원 제약 환경
- LLM 애플리케이션의 신속한 프로토타이핑

## Related Terms

- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [Adapter Modules (어댑터 모듈)](/en/terms/adapter-modules-어댑터-모듈/)
- [Prompt Engineering (프롬프트 엔지니어링)](/en/terms/prompt-engineering-프롬프트-엔지니어링/)
- [Transfer Learning (전이 학습)](/en/terms/transfer-learning-전이-학습/)
