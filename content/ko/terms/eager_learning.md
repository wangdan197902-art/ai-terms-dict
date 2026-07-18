---
title: "기대 학습(Eager Learning)"
term_id: "eager_learning"
category: "training_techniques"
subcategory: ""
tags: ["learning_paradigms", "training", "inference"]
difficulty: 2
weight: 1
slug: "eager_learning"
aliases:
  - /ko/terms/eager_learning/
date: "2026-07-18T15:53:50.594658Z"
lastmod: "2026-07-18T16:38:06.835203Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "일반화 함수가 훈련 단계 동안 학습되어 훈련 완료 후 빠른 예측 시간을 허용하는 머신러닝 접근 방식."
---

## Definition

기대 학습(Eager Learning)에서는 시스템이 새로운 인스턴스를 마주하기 전에 훈련 데이터를 기반으로 일반적인 목표 함수나 모델을 사전에 구축합니다. 이는 새로운 데이터를 받을 때마다 학습을 수행하는 지연 학습(Lazy Learning)과 대조됩니다. 기대 학습은 일반적으로 더 높은 계산 비용의 훈련 단계를 거치지만, 추론(Inference) 단계에서는 매우 빠르게 동작합니다.

### Summary

일반화 함수가 훈련 단계 동안 학습되어 훈련 완료 후 빠른 예측 시간을 허용하는 머신러닝 접근 방식.

## Key Concepts

- 훈련 단계 일반화(Training Phase Generalization)
- 빠른 추론(Fast Inference)
- 모델 복잡도(Model Complexity)
- 과적합 위험(Overfitting Risk)

## Use Cases

- 실시간 이미지 분류
- 사기 탐지 시스템
- 추천 엔진

## Related Terms

- [지연 학습(Lazy Learning) - 추론 시점에 학습을 수행하는 방식 (예: k-NN)](/en/terms/지연-학습-lazy-learning-추론-시점에-학습을-수행하는-방식-예-k-nn/)
- [인스턴스 기반 학습(Instance-based Learning) - 저장된 사례를 직접 비교하여 예측하는 학습](/en/terms/인스턴스-기반-학습-instance-based-learning-저장된-사례를-직접-비교하여-예측하는-학습/)
- [지도 학습(Supervised Learning) - 레이블이 달린 데이터를 사용하여 모델을 학습하는 방식](/en/terms/지도-학습-supervised-learning-레이블이-달린-데이터를-사용하여-모델을-학습하는-방식/)
- [모델 훈련(Model Training) - 데이터를 사용하여 모델의 파라미터를 조정하는 과정](/en/terms/모델-훈련-model-training-데이터를-사용하여-모델의-파라미터를-조정하는-과정/)
