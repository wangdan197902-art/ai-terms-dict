---
title: 데이터셋 시프트
term_id: dataset_shift
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- statistics
- Model Deployment
difficulty: 3
weight: 1
slug: dataset_shift
date: '2026-07-18T15:47:39.161844Z'
lastmod: '2026-07-18T16:38:06.825256Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 데이터셋 시프트는 훈련 단계와 배포 단계 간 입력 데이터의 통계적 특성이 변화하는 현상을指합니다.
---
## Definition

데이터셋 시프트는 머신러닝 모델을 훈련하는 데 사용된 데이터의 분포가 추론(inference) 단계에서 마주치는 데이터의 분포와 다를 때 발생합니다. 이러한 불일치는 모델 성능 저하로 이어질 수 있습니다.

### Summary

데이터셋 시프트는 훈련 단계와 배포 단계 간 입력 데이터의 통계적 특성이 변화하는 현상을指합니다.

## Key Concepts

- 공변량 시프트(Covariate shift)
- 개념 드리프트(Concept drift)
- 도메인 적응(Domain adaptation)
- 일반화(Generalization)

## Use Cases

- 프로덕션 환경의 ML 모델 모니터링
- 재학습 전략 수립
- 견고성 테스트(Robustness testing)

## Related Terms

- [Overfitting (과적합)](/en/terms/overfitting-과적합/)
- [Underfitting (과소적합)](/en/terms/underfitting-과소적합/)
- [Domain Adaptation (도메인 적응)](/en/terms/domain-adaptation-도메인-적응/)
- [Data Drift (데이터 드리프트)](/en/terms/data-drift-데이터-드리프트/)
