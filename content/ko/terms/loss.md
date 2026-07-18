---
title: "손실(Loss)"
term_id: "loss"
category: "training_techniques"
subcategory: ""
tags: ["training", "optimization"]
difficulty: 3
weight: 1
slug: "loss"
aliases:
  - /ko/terms/loss/
date: "2026-07-18T15:26:53.281260Z"
lastmod: "2026-07-18T16:38:06.778183Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델의 예측값과 실제 목표 값 사이의 오차를 수치화한 값입니다."
---

## Definition

비용 함수(Cost Function)라고도 불리는 손실 함수는 훈련 중 머신러닝 모델의 예측이 정답(Ground Truth)과 얼마나 일치하는지를 측정합니다. 최적화 알고리즘의 목표는 이 손실 값을 최소화하는 것입니다.

### Summary

모델의 예측값과 실제 목표 값 사이의 오차를 수치화한 값입니다.

## Key Concepts

- 비용 함수(Cost Function)
- 최적화(Optimization)
- 경사 하강법(Gradient Descent)
- 오차 지표(Error Metric)

## Use Cases

- 이미지 분류기 훈련하기
- 회귀 모델 최적화하기
- 모델 수렴 평가하기

## Code Example

```python
import torch.nn as nn
criterion = nn.CrossEntropyLoss()
loss = criterion(outputs, targets)
```

## Related Terms

- [Accuracy (정확도)](/en/terms/accuracy-정확도/)
- [Gradient Descent (경사 하강법)](/en/terms/gradient-descent-경사-하강법/)
- [Cross-Entropy (교차 엔트로피)](/en/terms/cross-entropy-교차-엔트로피/)
- [Overfitting (과적합)](/en/terms/overfitting-과적합/)
