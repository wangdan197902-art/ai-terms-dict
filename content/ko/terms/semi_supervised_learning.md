---
title: "반지도 학습(Semi-supervised learning)"
term_id: "semi_supervised_learning"
category: "training_techniques"
subcategory: ""
tags: ["ML Paradigms", "Data Efficiency", "Training Strategies"]
difficulty: 3
weight: 1
slug: "semi_supervised_learning"
aliases:
  - /ko/terms/semi_supervised_learning/
date: "2026-07-18T16:14:49.554441Z"
lastmod: "2026-07-18T16:38:06.906824Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "레이블이 있는 데이터와 없는 데이터를 모두 활용하여 모델의 정확도와 일반화 성능을 향상시키는 머신러닝 접근 방식입니다."
---

## Definition

반지도 학습은 소량의 레이블이 지정된 데이터와 대량의 레이블이 지정되지 않은 데이터를 함께 사용하는 하이브리드 학습 패러다임입니다. 핵심 가정은 레이블이 없는 데이터의 구조가 레이블이 있는 데이터의 분포를 반영한다는 것이며, 이를 통해 제한된 라벨링 비용으로도 강력한 모델을 구축할 수 있습니다.

### Summary

레이블이 있는 데이터와 없는 데이터를 모두 활용하여 모델의 정확도와 일반화 성능을 향상시키는 머신러닝 접근 방식입니다.

## Key Concepts

- 레이블 데이터(Labeled data)
- 비레이블 데이터(Unlabeled data)
- 셀프 트레이닝(Self-training)
- 매니폴드 가정(Manifold assumption)

## Use Cases

- 제한된 주석으로 이미지 분류(Image classification with limited annotations)
- 희소한 라벨로 텍스트 감성 분석(Text sentiment analysis with sparse labels)
- 제한된 전문가 데이터로 의료 진단 예측(Medical diagnosis prediction with scarce expert data)

## Related Terms

- [Supervised learning (지도 학습: 완전한 라벨 사용)](/en/terms/supervised-learning-지도-학습-완전한-라벨-사용/)
- [Unsupervised learning (비지도 학습: 라벨 없음)](/en/terms/unsupervised-learning-비지도-학습-라벨-없음/)
- [Active learning (능동 학습: 모델이 라벨 요청)](/en/terms/active-learning-능동-학습-모델이-라벨-요청/)
- [Self-supervised learning (자기 지도 학습: 데이터 자체에서 라벨 생성)](/en/terms/self-supervised-learning-자기-지도-학습-데이터-자체에서-라벨-생성/)
