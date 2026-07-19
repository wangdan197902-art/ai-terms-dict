---
title: 조기 종료(Early Stopping)
term_id: early_stopping
category: training_techniques
subcategory: ''
tags:
- Regularization
- training
- Optimization
difficulty: 2
weight: 1
slug: early_stopping
date: '2026-07-18T15:54:09.943580Z'
lastmod: '2026-07-18T16:38:06.835445Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 조기 종료(Early Stopping)는 검증 세트에서 모델 성능이 저하되기 시작할 때 훈련 과정을 중단하여 과적합(overfitting)을
  방지하는 정규화 기법입니다.
---
## Definition

조기 종료(Early Stopping)는 경사 하강법(gradient descent)과 같은 반복적 훈련 과정에서 주로 사용되는 정규화 방법입니다. 훈련 중 모델의 훈련 데이터에 대한 성능은 일반적으로 지속적으로 향상되지만, 검증 데이터에 대한 성능은 일정 시점 이후부터 악화되기 시작합니다. 조기 종료는 이러한 검증 성능의 악화를 감지하고 훈련을 즉시 중지함으로써 모델이 훈련 데이터에 지나치게 맞춰지는 것을 막습니다.

### Summary

조기 종료(Early Stopping)는 검증 세트에서 모델 성능이 저하되기 시작할 때 훈련 과정을 중단하여 과적합(overfitting)을 방지하는 정규화 기법입니다.

## Key Concepts

- 정규화
- 검증 세트
- 과적합 방지
- 인내 파라미터(Patience Parameter)

## Use Cases

- 신경망 훈련
- 그래디언트 부스팅 알고리즘
- 시계열 예측 모델

## Related Terms

- [L2 정규화 (가중치 감소)](/en/terms/l2-정규화-가중치-감소/)
- [드롭아웃(Dropout)](/en/terms/드롭아웃-dropout/)
- [교차 검증(Cross-Validation)](/en/terms/교차-검증-cross-validation/)
- [일반화 오차(Generalization Error)](/en/terms/일반화-오차-generalization-error/)
