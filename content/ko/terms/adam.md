---
title: "Adam"
term_id: "adam"
category: "basic_concepts"
subcategory: ""
tags: ["Optimization", "Deep Learning", "Algorithms"]
difficulty: 3
weight: 1
slug: "adam"
aliases:
  - /ko/terms/adam/
date: "2026-07-18T15:22:46.628600Z"
lastmod: "2026-07-18T16:38:06.767714Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "각 매개변수에 대해 적응형 학습률을 계산하는 최적화 알고리즘."
---

## Definition

Adam(적응 모멘트 추정)은 심층 신경망 훈련에 널리 사용되는 1계 경사 기반 최적화 알고리즘입니다. 이는 확률적 경사 하강법의 두 가지 확장 버전인 모멘텀(Momentum)과 RMSProp의 장점을 결합합니다.

### Summary

각 매개변수에 대해 적응형 학습률을 계산하는 최적화 알고리즘.

## Key Concepts

- 경사 하강법 (Gradient Descent)
- 학습률 (Learning Rate)
- 모멘텀 (Momentum)
- 분산 추정 (Variance Estimation)

## Use Cases

- 딥러닝 훈련 (Deep Learning Training)
- 컴퓨터 비전 모델 (Computer Vision Models)
- 자연어 처리 (Natural Language Processing)

## Code Example

```python
import torch.optim as optim
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

## Related Terms

- [SGD (확률적 경사 하강법)](/en/terms/sgd-확률적-경사-하강법/)
- [RMSProp (RMSProp 알고리즘)](/en/terms/rmsprop-rmsprop-알고리즘/)
- [Optimizer (최적화 함수)](/en/terms/optimizer-최적화-함수/)
- [Backpropagation (역전파)](/en/terms/backpropagation-역전파/)
