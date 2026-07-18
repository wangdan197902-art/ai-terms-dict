---
title: "학습률"
term_id: "learning_rate"
category: "training_techniques"
subcategory: ""
tags: ["training", "optimization", "hyperparameters"]
difficulty: 3
weight: 1
slug: "learning_rate"
aliases:
  - /ko/terms/learning_rate/
date: "2026-07-18T15:35:05.258471Z"
lastmod: "2026-07-18T16:38:06.796655Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "손실 함수를 최소화하기 위한 모델 최적화 과정에서 단계 크기를 제어하는 하이퍼파라미터입니다."
---

## Definition

학습률은 각 학습 반복 동안 계산된 기울기에 비해 모델의 가중치가 얼마나 업데이트되는지를 결정합니다. 너무 높은 학습률은 모델이 최적점을 지나쳐서 발산하거나 불안정해질 수 있습니다. 반면, 너무 낮은 학습률은 학습 속도를 느리게 하여 최적점에 도달하는 데 오랜 시간이 걸릴 수 있습니다.

### Summary

손실 함수를 최소화하기 위한 모델 최적화 과정에서 단계 크기를 제어하는 하이퍼파라미터입니다.

## Key Concepts

- 경사 하강법
- 하이퍼파라미터 튜닝
- 수렴
- 옵티마이저

## Use Cases

- 신경망 훈련
- 딥러닝 모델 최적화
- 강화학습 정책 업데이트

## Code Example

```python
import torch.optim as optim
model = MyModel()
optimizer = optim.SGD(model.parameters(), lr=0.01)
```

## Related Terms

- [gradient_descent (경사 하강법)](/en/terms/gradient_descent-경사-하강법/)
- [optimizer (최적화 알고리즘)](/en/terms/optimizer-최적화-알고리즘/)
- [hyperparameter (하이퍼파라미터)](/en/terms/hyperparameter-하이퍼파라미터/)
- [convergence (수렴)](/en/terms/convergence-수렴/)
