---
title: "프리픽스 튜닝"
term_id: "prefix_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "transformers"]
difficulty: 4
weight: 1
slug: "prefix_tuning"
aliases:
  - /ko/terms/prefix_tuning/
date: "2026-07-18T16:10:25.380694Z"
lastmod: "2026-07-18T16:38:06.897581Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "트랜스포머 레이어의 입력에 학습 가능한 연속 벡터를 추가하여 파라미터 효율적인 파인튜닝을 수행하는 방법입니다."
---

## Definition

프리픽스 튜닝은 사전 훈련된 트랜스포머 모델에 적용되는 파라미터 효율적인 적응 기술입니다. 모든 모델 가중치를 업데이트하는 대신, 학습 가능한 연속 벡터 시퀀스(프리픽스)를 입력 앞에 붙여 모델을 조정합니다.

### Summary

트랜스포머 레이어의 입력에 학습 가능한 연속 벡터를 추가하여 파라미터 효율적인 파인튜닝을 수행하는 방법입니다.

## Key Concepts

- 파라미터 효율적 튜닝
- 소프트 프롬프트
- 트랜스포머 레이어
- 동결 백본(Frozen backbone)

## Use Cases

- 소량 데이터 학습(Few-shot learning) 적응
- 제한된 자원에서의 다중 작업 학습
- 특정 도메인에 맞춘 LLM 사용자 정의

## Related Terms

- [prompt_tuning (프롬프트 튜닝)](/en/terms/prompt_tuning-프롬프트-튜닝/)
- [p_tuning (P-tuning)](/en/terms/p_tuning-p-tuning/)
- [adapter_modules (어댑터 모듈)](/en/terms/adapter_modules-어댑터-모듈/)
- [peft (파라미터 효율적 미세 조정)](/en/terms/peft-파라미터-효율적-미세-조정/)
