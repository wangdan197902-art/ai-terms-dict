---
title: "예측 학습(Predictive learning)"
term_id: "predictive_learning"
category: "training_techniques"
subcategory: ""
tags: ["self_supervised", "pretraining", "representation"]
difficulty: 3
weight: 1
slug: "predictive_learning"
aliases:
  - /ko/terms/predictive_learning/
date: "2026-07-18T16:10:11.698289Z"
lastmod: "2026-07-18T16:38:06.897123Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델이 입력 데이터의 누락된 부분을 예측함으로써 표현을 학습하는 자기지도 방식 접근법입니다."
---

## Definition

예측 학습은 명시적인 인간 라벨 없이 관찰된 입력으로부터 관찰되지 않은 데이터 포인트를 추론하도록 신경망을 훈련시키는 과정입니다. 언어 모델에서의 다음 토큰 예측이나 이미지에서의 마스킹된 영역 복원 같은 과제를 해결함으로써 작동합니다.

### Summary

모델이 입력 데이터의 누락된 부분을 예측함으로써 표현을 학습하는 자기지도 방식 접근법입니다.

## Key Concepts

- 자기지도학습(Self-supervision)
- 마스킹 모델링
- 표현 학습
- 라벨 없는 데이터

## Use Cases

- 대규모 언어 모델 사전 훈련
- 이미지 인페인팅(Inpainting) 작업
- 시계열 이상 감지

## Related Terms

- [self_supervised_learning (자기지도학습)](/en/terms/self_supervised_learning-자기지도학습/)
- [masked_language_modeling (마스킹된 언어 모델링)](/en/terms/masked_language_modeling-마스킹된-언어-모델링/)
- [contrastive_learning (대조 학습)](/en/terms/contrastive_learning-대조-학습/)
- [autoencoder (오토인코더)](/en/terms/autoencoder-오토인코더/)
