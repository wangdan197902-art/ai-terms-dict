---
title: 은닉 계층
term_id: hidden_layer
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- Deep Learning
difficulty: 3
weight: 1
slug: hidden_layer
date: '2026-07-18T15:58:32.648592Z'
lastmod: '2026-07-18T16:38:06.849758Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 입력 계층과 출력 계층 사이에 위치하여 특징(feature)을 처리하는 신경망의 중간 계층입니다.
---
## Definition

은닉 계층은 이전 계층으로부터 입력을 받아 가중치와 편향을 적용한 후, 활성화 함수를 통해 변환된 데이터를 다음 계층으로 전달하는 뉴런들로 구성됩니다. 이러한 계층들은 신경망이 복잡한 패턴을 학습하고 추상적인 특징을 추출할 수 있게 합니다.

### Summary

입력 계층과 출력 계층 사이에 위치하여 특징(feature)을 처리하는 신경망의 중간 계층입니다.

## Key Concepts

- 신경망
- 특징 추출
- 활성화 함수
- 딥 러닝

## Use Cases

- 이미지 인식 시스템
- 자연어 처리 모델
- 예측 분석

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron (뉴런)](/en/terms/neuron-뉴런/)
- [backpropagation (역전파)](/en/terms/backpropagation-역전파/)
- [activation_function (활성화 함수)](/en/terms/activation_function-활성화-함수/)
- [deep_learning (딥 러닝)](/en/terms/deep_learning-딥-러닝/)
