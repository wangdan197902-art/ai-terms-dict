---
title: "신경망(Neural Network)"
term_id: "neural_network"
category: "basic_concepts"
subcategory: ""
tags: ["Deep Learning", "Architecture", "AI"]
difficulty: 4
weight: 1
slug: "neural_network"
aliases:
  - /ko/terms/neural_network/
date: "2026-07-18T15:27:21.460652Z"
lastmod: "2026-07-18T16:38:06.779806Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "생물학적 뇌에서 영감을 받은 컴퓨팅 시스템으로, 레이어로 조직화된 상호 연결된 노드(뉴런)로 구성됨."
---

## Definition

신경망은 인간의 뇌가 작동하는 방식을 모방하는 과정을 통해 데이터 세트의 숨겨진 관계를 인식하려는 일련의 알고리즘입니다. 이는 입력층, 은닉층, 출력층 등 여러 레이어로 구성된 뉴런(노드) 네트워크로 이루어져 있습니다.

### Summary

생물학적 뇌에서 영감을 받은 컴퓨팅 시스템으로, 레이어로 조직화된 상호 연결된 노드(뉴런)로 구성됨.

## Key Concepts

- 퍼셉트론(Perceptron)
- 역전파(Backpropagation)
- 활성화 함수(Activation Functions)
- 가중치와 편향(Weights and Biases)

## Use Cases

- 이미지 인식
- 음성 인식
- 예측 분석(Predictive analytics)

## Code Example

```python
import torch.nn as nn
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.layer = nn.Linear(10, 1)
    def forward(self, x):
        return self.layer(x)
```

## Related Terms

- [deep_learning (딥러닝)](/en/terms/deep_learning-딥러닝/)
- [artificial_intelligence (인공지능)](/en/terms/artificial_intelligence-인공지능/)
- [machine_learning (기계 학습)](/en/terms/machine_learning-기계-학습/)
- [convolutional_neural_network (합성곱 신경망)](/en/terms/convolutional_neural_network-합성곱-신경망/)
