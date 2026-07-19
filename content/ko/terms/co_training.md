---
title: 코 트레이닝
term_id: co_training
category: training_techniques
subcategory: ''
tags:
- Semi Supervised
- algorithm
- Data Efficiency
difficulty: 4
weight: 1
slug: co_training
date: '2026-07-18T15:45:14.520231Z'
lastmod: '2026-07-18T16:38:06.817089Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 코 트레이닝은 데이터의 두 가지 관점을 사용하여 별도의 분류기를 훈련시키고, 이들이 서로에게 미라벨링된 데이터에 대한 레이블을
  반복적으로 부여하는 준지도 학습 알고리즘입니다.
---
## Definition

이 방법은 동일한 데이터 포인트의 여러 고유한 특징 집합(관점)을 활용합니다. 초기에는 각 관점에서 작은 라벨링된 데이터셋으로 두 개의 분류기를 훈련시킵니다. 이후 이들은 미라벨링된 데이터에 대한 레이블을 예측하고, 높은 신뢰도를 가진 예측 결과를 서로 공유하며 레이블을 추가합니다.

### Summary

코 트레이닝은 데이터의 두 가지 관점을 사용하여 별도의 분류기를 훈련시키고, 이들이 서로에게 미라벨링된 데이터에 대한 레이블을 반복적으로 부여하는 준지도 학습 알고리즘입니다.

## Key Concepts

- 준지도 학습
- 다중 관점
- 반복적 레이블링
- 고신뢰도 선택

## Use Cases

- 다양한 특징을 활용한 텍스트 분류
- 웹 페이지 범주화
- 제한된 라벨 데이터 증강

## Related Terms

- [Semi-Supervised Learning (준지도 학습)](/en/terms/semi-supervised-learning-준지도-학습/)
- [Self-Training (자기 훈련)](/en/terms/self-training-자기-훈련/)
- [Multi-view Learning (다중 관점 학습)](/en/terms/multi-view-learning-다중-관점-학습/)
- [Active Learning (능동 학습)](/en/terms/active-learning-능동-학습/)
