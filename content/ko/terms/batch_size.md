---
title: "배치 크기(Batch Size)"
term_id: "batch_size"
category: "training_techniques"
subcategory: ""
tags: ["hyperparameters", "optimization", "memory"]
difficulty: 2
weight: 1
slug: "batch_size"
aliases:
  - /ko/terms/batch_size/
date: "2026-07-18T15:43:24.253828Z"
lastmod: "2026-07-18T16:38:06.812761Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "확률적 경사 하강법(Stochastic Gradient Descent) 알고리즘의 한 번 반복(iteration)에서 사용되는 훈련 예제의 수입니다."
---

## Definition

배치 크기는 모델의 내부 매개변수가 업데이트되기 전에 처리되는 샘플의 수를 결정하는 중요한 하이퍼파라미터입니다. 더 큰 배치 크기는 그라디언트의 더 정확한 추정치를 제공하지만, 메모리 제약이 있을 수 있습니다.

### Summary

확률적 경사 하강법(Stochastic Gradient Descent) 알고리즘의 한 번 반복(iteration)에서 사용되는 훈련 예제의 수입니다.

## Key Concepts

- 그라디언트 추정(Gradient Estimation)
- 메모리 제약(Memory Constraints)
- 수렴 안정성(Convergence Stability)
- 하이퍼파라미터 튜닝(Hyperparameter Tuning)

## Use Cases

- 모델 수렴 속도 튜닝
- 학습 중 GPU 메모리 제한 관리
- 노이즈 있는 그라디언트를 통한 일반화 성능 향상

## Related Terms

- [learning_rate (학습률)](/en/terms/learning_rate-학습률/)
- [stochastic_gradient_descent (확률적 경사 하강법)](/en/terms/stochastic_gradient_descent-확률적-경사-하강법/)
- [mini_batch (미니 배치)](/en/terms/mini_batch-미니-배치/)
- [memory_usage (메모리 사용량)](/en/terms/memory_usage-메모리-사용량/)
