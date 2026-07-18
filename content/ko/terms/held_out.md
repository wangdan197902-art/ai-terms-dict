---
title: "홀드아웃(Held-out)"
term_id: "held_out"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "data_splitting", "validation"]
difficulty: 2
weight: 1
slug: "held_out"
aliases:
  - /ko/terms/held_out/
date: "2026-07-18T15:31:36.908059Z"
lastmod: "2026-07-18T16:38:06.789080Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "개발 중 과적합을 방지하고 모델 성능을 평가하기 위해 훈련 세트에서 예약된 데이터 샘플."
---

## Definition

'홀드아웃' 데이터셋은 머신러닝 모델의 훈련 단계에서 의도적으로 제외된 예제들의 집합입니다. 이 부분집합은 모델이 보지 못한 데이터(Unseen data)에 대해 얼마나 잘 일반화되는지 평가하는 데 사용되며, 훈련 과정에서의 과적합(Overfitting)을 방지하고 모델의 실제 성능을 unbiased하게 추정하는 역할을 합니다.

### Summary

개발 중 과적합을 방지하고 모델 성능을 평가하기 위해 훈련 세트에서 예약된 데이터 샘플.

## Key Concepts

- 일반화(Generalization)
- 과적합(Overfitting)
- 검증 세트(Validation set)
- 편향 없는 평가(Unbiased evaluation)

## Use Cases

- 하이퍼파라미터 튜닝
- 서로 다른 모델 아키텍처 비교
- 서비스 출시 전 최종 성능 추정

## Related Terms

- [training_set (훈련 세트: 모델 학습에 사용되는 데이터)](/en/terms/training_set-훈련-세트-모델-학습에-사용되는-데이터/)
- [test_set (테스트 세트: 최종 성능 평가를 위해 사용된 데이터)](/en/terms/test_set-테스트-세트-최종-성능-평가를-위해-사용된-데이터/)
- [cross_validation (교차 검증: 데이터를 여러 부분으로 나누어 반복적으로 검증하는 방법)](/en/terms/cross_validation-교차-검증-데이터를-여러-부분으로-나누어-반복적으로-검증하는-방법/)
- [generalization (일반화: 훈련되지 않은 데이터에서도 좋은 성능을 내는 능력)](/en/terms/generalization-일반화-훈련되지-않은-데이터에서도-좋은-성능을-내는-능력/)
