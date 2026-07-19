---
title: "그로킹 (Grokking)"
term_id: "grokking"
category: "basic_concepts"
subcategory: ""
tags: ["theory", "training", "phenomena"]
difficulty: 4
weight: 1
slug: "grokking"
date: "2026-07-18T15:58:08.183769Z"
lastmod: "2026-07-18T16:38:06.848106Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "신경망이 작은 데이터셋에 장기간 훈련하여 암기 지점을 훨씬 넘은 시점에서도 갑자기 일반화 성능이 급격히 향상되는 현상입니다."
---
## Definition

그로킹(Grokking)은 딥러닝에서 관찰되는 직관에 반하는 행동으로, 모델이 오랫동안 훈련 데이터에 과적합(overfitting)되어 일반화 성능이 낮게 유지되다가, 특정 시점이 지나자 갑자기 테스트 데이터에 대한 일반화 성능이 급격히 향상되는 현상을 의미합니다.

### Summary

신경망이 작은 데이터셋에 장기간 훈련하여 암기 지점을 훨씬 넘은 시점에서도 갑자기 일반화 성능이 급격히 향상되는 현상입니다.

## Key Concepts

- 지연된 일반화 (Delayed Generalization)
- 과적합 (Overfitting)
- 소형 데이터셋 (Small Datasets)
- 최적화 역학 (Optimization Dynamics)

## Use Cases

- 모델 일반화의 한계 연구
- 훈련 역학 분석
- 암기와 학습의 차이 이해

## Related Terms

- [overfitting (과적합: 모델이 훈련 데이터에 너무 맞춰져 새로운 데이터에서 성능이 떨어지는 현상)](/en/terms/overfitting-과적합-모델이-훈련-데이터에-너무-맞춰져-새로운-데이터에서-성능이-떨어지는-현상/)
- [generalization (일반화: 모델이 미처 보지 못한 데이터에서도 잘 작동하는 능력)](/en/terms/generalization-일반화-모델이-미처-보지-못한-데이터에서도-잘-작동하는-능력/)
- [deep_learning_theory (딥러닝 이론: 신경망의 동작 원리를 설명하는 이론적 배경)](/en/terms/deep_learning_theory-딥러닝-이론-신경망의-동작-원리를-설명하는-이론적-배경/)
- [training_dynamics (훈련 역학: 모델 훈련 과정에서의 손실 감소 및 수렴 패턴 변화)](/en/terms/training_dynamics-훈련-역학-모델-훈련-과정에서의-손실-감소-및-수렴-패턴-변화/)
