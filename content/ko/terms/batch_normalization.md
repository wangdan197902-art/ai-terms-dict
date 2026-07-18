---
title: "배치 정규화(Batch Normalization)"
term_id: "batch_normalization"
category: "basic_concepts"
subcategory: ""
tags: ["deep-learning", "optimization", "neural-networks"]
difficulty: 3
weight: 1
slug: "batch_normalization"
aliases:
  - /ko/terms/batch_normalization/
date: "2026-07-18T15:43:24.253819Z"
lastmod: "2026-07-18T16:38:06.812525Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "미니 배치 전체에 걸쳐 레이어 입력값을 정규화하여 신경망 학습을 안정화하고 가속화하는 기법입니다."
---

## Definition

이 방법은 훈련 중 각 미니 배치 내에서 활성화 값의 평균을 0, 분산을 1로 조정 및 스케일링합니다. 이를 통해 내부 공변량 변화(Internal covariate shift)를 줄여 더 높은 학습률 사용과 빠른 수렴을 가능하게 합니다.

### Summary

미니 배치 전체에 걸쳐 레이어 입력값을 정규화하여 신경망 학습을 안정화하고 가속화하는 기법입니다.

## Key Concepts

- 내부 공변량 변화(Internal covariate shift)
- 미니 배치 통계(Mini-batch statistics)
- 그라디언트 안정화(Gradient stabilization)
- 정규화 효과(Regularization effect)

## Use Cases

- 딥 뉴럴 네트워크(Deep Neural Networks)
- 합성곱 신경망(Convolutional Neural Networks)
- 학습 최적화(Training optimization)

## Code Example

```python
import torch.nn as nn
layer = nn.Sequential(
    nn.Linear(10, 20),
    nn.BatchNorm1d(20),
    nn.ReLU()
)
```

## Related Terms

- [Layer Normalization (레이어 정규화)](/en/terms/layer-normalization-레이어-정규화/)
- [Gradient Descent (경사 하강법)](/en/terms/gradient-descent-경사-하강법/)
- [Overfitting (과적합)](/en/terms/overfitting-과적합/)
