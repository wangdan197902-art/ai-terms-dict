---
title: 순방향 신경망
term_id: feed_forward_network
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- fundamentals
difficulty: 2
weight: 1
slug: feed_forward_network
date: '2026-07-18T15:55:47.592298Z'
lastmod: '2026-07-18T16:38:06.840557Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 노드 간 연결이 사이클을 형성하지 않고 정보를 한 방향으로 전달하는 인공 신경망의 한 클래스입니다.
---
## Definition

순방향 신경망(FFN)은 다층 퍼셉트론(MLP)이라고도 하며, 피드백 루프 없이 입력에서 출력까지 뉴런 레이어를 통해 데이터를 순차적으로 처리합니다. 각 뉴런은 입력을 받아 가중합을 계산합니다.

### Summary

노드 간 연결이 사이클을 형성하지 않고 정보를 한 방향으로 전달하는 인공 신경망의 한 클래스입니다.

## Key Concepts

- 사이클 없음
- 레이어(입력, 은닉, 출력)
- 활성화 함수
- 가중 합

## Use Cases

- 간단한 회귀 작업
- 표 형식 데이터의 분류 문제
- 더 깊은 아키텍처의 구성 요소

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron (다층 퍼셉트론)](/en/terms/multi-layer-perceptron-다층-퍼셉트론/)
- [Backpropagation (역전파)](/en/terms/backpropagation-역전파/)
- [Activation Function (활성화 함수)](/en/terms/activation-function-활성화-함수/)
- [Neural Network (신경망)](/en/terms/neural-network-신경망/)
