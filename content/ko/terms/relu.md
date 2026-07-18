---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /ko/terms/relu/
date: "2026-07-18T15:36:05.902118Z"
lastmod: "2026-07-18T16:38:06.799425Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "Rectified Linear Unit는 양수인 경우 입력을 그대로 출력하고, 그렇지 않으면 0을 출력하는 활성화 함수입니다."
---

## Definition

ReLU는 계산 효율성이 뛰어나고 기울기 소실 문제를 완화할 수 있어 딥러닝 신경망에서 널리 사용됩니다. 수학적으로 f(x) = max(0, x)로 정의되며, 이는 입력이 0보다 작을 때 출력을 0으로 클리핑(cropping)하고 양수일 때는 입력값을 그대로 전달하는(piecewise linear) 특성을 가집니다.

### Summary

Rectified Linear Unit는 양수인 경우 입력을 그대로 출력하고, 그렇지 않으면 0을 출력하는 활성화 함수입니다.

## Key Concepts

- 비선형성
- 활성화 함수
- 기울기 소실
- 조각별 선형(Piecewise Linear)

## Use Cases

- CNN의 은닉층
- 심층 순방향 네트워크
- 이미지 인식 모델

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (시그모이드: S자 곡선 형태의 활성화 함수)](/en/terms/sigmoid-시그모이드-s자-곡선-형태의-활성화-함수/)
- [Tanh (탄젠트 하이퍼볼릭: -1에서 1 사이의 값을 출력하는 활성화 함수)](/en/terms/tanh-탄젠트-하이퍼볼릭-1에서-1-사이의-값을-출력하는-활성화-함수/)
- [Leaky ReLU (리키 ReLU: 음수 구간에서도 작은 기울기를 갖도록 수정된 ReLU)](/en/terms/leaky-relu-리키-relu-음수-구간에서도-작은-기울기를-갖도록-수정된-relu/)
- [Neural Network (신경망: 생물학적 신경계에서 영감을 받은 계산 모델)](/en/terms/neural-network-신경망-생물학적-신경계에서-영감을-받은-계산-모델/)
