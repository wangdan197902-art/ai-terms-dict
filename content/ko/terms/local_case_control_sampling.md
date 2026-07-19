---
title: Local case-control sampling
term_id: local_case_control_sampling
category: basic_concepts
subcategory: ''
tags:
- sampling
- Contrastive Learning
- Optimization
difficulty: 4
weight: 1
slug: local_case_control_sampling
date: '2026-07-18T16:03:01.834149Z'
lastmod: '2026-07-18T16:38:06.868606Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 임베딩 공간에서 양성 예제의 주변부에서 하드 네거티브(hard negatives)를 선택하는 부정적 샘플링 기법입니다.
---
## Definition

로컬 케이스-컨트롤 샘플링은 주로 대조 학습 모델이나 추천 시스템을 훈련하는 데 사용되는 전략입니다. 무작위로 음성 샘플을 선택하는 대신, 임베딩 공간에서 양성 예제와 유사하지만 구별 가능한 '하드 네거티브'를 식별하여 모델의 판별력을 높입니다.

### Summary

임베딩 공간에서 양성 예제의 주변부에서 하드 네거티브(hard negatives)를 선택하는 부정적 샘플링 기법입니다.

## Key Concepts

- 하드 네거티브
- 대조 학습
- 임베딩 공간
- 부정적 샘플링

## Use Cases

- 이미지 검색 시스템 훈련
- 추천 엔진 정확도 향상
- 특정 작업용 대형 언어 모델 파인튜닝

## Related Terms

- [Triplet Loss (트리플릿 손실)](/en/terms/triplet-loss-트리플릿-손실/)
- [InfoNCE (인포NCE)](/en/terms/infonce-인포nce/)
- [Hard Negative Mining (하드 네거티브 마이닝)](/en/terms/hard-negative-mining-하드-네거티브-마이닝/)
- [Contrastive Divergence (대조 발산)](/en/terms/contrastive-divergence-대조-발산/)
