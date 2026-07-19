---
title: 대조적 학습
term_id: contrastive_learning
category: training_techniques
subcategory: ''
tags:
- Self Supervised
- Representation Learning
- Optimization
difficulty: 4
weight: 1
slug: contrastive_learning
date: '2026-07-18T15:46:36.340289Z'
lastmod: '2026-07-18T16:38:06.822174Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 양성 쌍은 가까이 모으고 음성 쌍은 멀리 떨어뜨려 표현을 학습하는 자기지도 학습 기법입니다.
---
## Definition

대조적 학습은 레이블이 붙은 데이터가 필요 없는 표현 학습 방법입니다. 동일한 입력의 증강된 뷰(양성 쌍)를 생성하고, 서로 다른 입력 또는 증강된 뷰(음성 쌍)와 대비시킴으로써 모델이 데이터의 본질적인 구조와 특징을 학습하도록 합니다.

### Summary

양성 쌍은 가까이 모으고 음성 쌍은 멀리 떨어뜨려 표현을 학습하는 자기지도 학습 기법입니다.

## Key Concepts

- 자기지도 학습
- 양성/음성 쌍
- 임베딩 공간
- 증강 전략

## Use Cases

- 레이블 없는 이미지 분류
- 시맨틱 검색 인덱싱
- 시계열 이상 감지

## Related Terms

- [SimCLR (대조적 프레임워크 기반 모델)](/en/terms/simclr-대조적-프레임워크-기반-모델/)
- [MoCo (모멘텀 컨트라스티브)](/en/terms/moco-모멘텀-컨트라스티브/)
- [Self-Supervised Learning (자기지도 학습)](/en/terms/self-supervised-learning-자기지도-학습/)
- [Representation Learning (표현 학습)](/en/terms/representation-learning-표현-학습/)
