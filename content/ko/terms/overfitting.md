---
title: "과적합"
term_id: "overfitting"
category: "training_techniques"
subcategory: ""
tags: ["model_evaluation", "training_dynamics", "generalization"]
difficulty: 2
weight: 1
slug: "overfitting"
aliases:
  - /ko/terms/overfitting/
date: "2026-07-18T15:35:37.491221Z"
lastmod: "2026-07-18T16:38:06.798220Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "기계 학습 알고리즘이 근본적인 신호(noise가 아닌 실제 패턴) 대신 노이즈를 포착하여 일반화 성능을 저해하는 모델링 오류."
---

## Definition

과적합은 모델이 훈련 데이터의 무작위 노이즈와 이상치를 포함하여 너무 잘 학습할 때 발생합니다. 그 결과 훈련 데이터에서는 우수한 성능을 보이지만, 새로운 미시청 테스트 데이터에서는 성능이 떨어집니다.

### Summary

기계 학습 알고리즘이 근본적인 신호(noise가 아닌 실제 패턴) 대신 노이즈를 포착하여 일반화 성능을 저해하는 모델링 오류.

## Key Concepts

- 높은 분산
- 열악한 일반화
- 훈련 오차와 테스트 오차의 격차
- 모델 복잡도

## Use Cases

- 모델 성능 문제 진단
- 정규화 강도 선택
- 최적 모델 깊이 결정

## Related Terms

- [underfitting (과소적합)](/en/terms/underfitting-과소적합/)
- [regularization (정규화)](/en/terms/regularization-정규화/)
- [cross_validation (교차 검증)](/en/terms/cross_validation-교차-검증/)
- [bias_variance_tradeoff (편향-분산 트레이드오프)](/en/terms/bias_variance_tradeoff-편향-분산-트레이드오프/)
