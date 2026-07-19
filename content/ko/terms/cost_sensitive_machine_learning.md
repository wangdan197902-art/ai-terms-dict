---
title: 비용 민감 기계 학습
term_id: cost_sensitive_machine_learning
category: training_techniques
subcategory: ''
tags:
- Optimization
- Loss Functions
- Imbalanced Data
difficulty: 4
weight: 1
slug: cost_sensitive_machine_learning
date: '2026-07-18T15:46:36.340305Z'
lastmod: '2026-07-18T16:38:06.822467Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 오분류 비용을 학습 과정에 반영하여 단순 정확도가 아닌 경제적 영향을 최적화하는 머신러닝 패러다임입니다.
---
## Definition

비용 민감 기계 학습은 전통적인 지도 학습을 확장하여, 서로 다른 유형의 오류에 서로 다른 패널티를 부여합니다. 실제 시나리오에서 위양성(False Positive)과 위음성(False Negative)의 비용은 대칭적이지 않으며, 모델은 이러한 비용 차이를 고려하여 의사 결정 경계를 조정함으로써 전체적인 경제적 손실을 최소화합니다.

### Summary

오분류 비용을 학습 과정에 반영하여 단순 정확도가 아닌 경제적 영향을 최적화하는 머신러닝 패러다임입니다.

## Key Concepts

- 손실 함수 수정
- 클래스 불균형
- 오분류 비용
- 최적화 목표

## Use Cases

- 은행 사기 탐지
- 의료 질병 스크리닝
- 위양성 비용이 높은 스팸 필터링

## Related Terms

- [Imbalanced Learning (불균형 학습)](/en/terms/imbalanced-learning-불균형-학습/)
- [Precision-Recall Tradeoff (정밀도-재현율 트레이드오프)](/en/terms/precision-recall-tradeoff-정밀도-재현율-트레이드오프/)
- [ROC Curve (수신자 조작 특성 곡선)](/en/terms/roc-curve-수신자-조작-특성-곡선/)
- [Weighted Loss (가중 손실)](/en/terms/weighted-loss-가중-손실/)
