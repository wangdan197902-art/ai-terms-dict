---
title: "경사 하강법"
term_id: "gradient_descent"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Training", "Optimization"]
difficulty: 2
weight: 1
slug: "gradient_descent"
date: "2026-07-18T15:34:33.739739Z"
lastmod: "2026-07-18T16:38:06.795806Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "경사 하강법은 모델의 매개변수를 조정하여 손실 함수(Loss function)를 최소화하기 위해 사용되는 반복적 최적화 알고리즘입니다."
---
## Definition

경사 하강법은 미분 가능한 함수의 국소 최소값을 찾기 위한 1차원 반복 최적화 알고리즘입니다. 머신러닝에서는 모델의 가중치를 손실 함수의 기울기(그래디언트)가 반대 방향으로 이동하도록 업데이트합니다. 학습률(Learning rate)이라는 하이퍼파라미터를 사용하여 각 단계의 크기를 조절하며, 더 작은 손실 값을 향해 점진적으로 수렴해 나갑니다.

### Summary

경사 하강법은 모델의 매개변수를 조정하여 손실 함수(Loss function)를 최소화하기 위해 사용되는 반복적 최적화 알고리즘입니다.

## Key Concepts

- 손실 함수
- 학습률
- 최적화
- 역전파

## Use Cases

- 심층 신경망 훈련
- 선형 회귀 매개변수 튜닝
- 이미지 인식 모델 최적화

## Related Terms

- [Backpropagation (역전파: 오차를 앞쪽으로 전달하여 가중치 업데이트)](/en/terms/backpropagation-역전파-오차를-앞쪽으로-전달하여-가중치-업데이트/)
- [Learning Rate (학습률: 경사 하강법의 단계 크기)](/en/terms/learning-rate-학습률-경사-하강법의-단계-크기/)
- [Optimizer (옵티마이저: 최적화를 수행하는 알고리즘)](/en/terms/optimizer-옵티마이저-최적화를-수행하는-알고리즘/)
- [Loss Function (손실 함수: 예측값과 정답의 차이 측정)](/en/terms/loss-function-손실-함수-예측값과-정답의-차이-측정/)
