---
title: 활성화 함수(Activation Function)
term_id: activation_function
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- mathematics
- Deep Learning
- basics
difficulty: 3
weight: 1
slug: activation_function
date: '2026-07-18T15:33:06.668101Z'
lastmod: '2026-07-18T16:38:06.792592Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 뉴럴 네트워크 노드의 출력값을 입력 신호에 따라 결정하는 수학적 방정식.
---
## Definition

활성화 함수는 뉴럴 네트워크에 비선형성을 도입하여 복잡한 패턴과 데이터 내 관계를 학습할 수 있게 합니다. 이러한 함수가 없다면 다층 네트워크는 단순한 선형 회귀 모델처럼 동작하게 되어 복잡한 문제를 해결할 수 없습니다.

### Summary

뉴럴 네트워크 노드의 출력값을 입력 신호에 따라 결정하는 수학적 방정식.

## Key Concepts

- 비선형성
- 경사 하강법
- 뉴런 활성화
- 역전파

## Use Cases

- 딥 뉴럴 네트워크를 통한 이미지 분류 가능하게 함
- 자연어 처리(NLP) 작업 지원
- 생성 모델 학습 시 수렴 속도 향상

## Code Example

```python
import torch.nn as nn
relu = nn.ReLU()
output = relu(input_tensor)
```

## Related Terms

- [ReLU (Rectified Linear Unit: 가장 널리 쓰이는 비선형 활성화 함수)](/en/terms/relu-rectified-linear-unit-가장-널리-쓰이는-비선형-활성화-함수/)
- [Sigmoid (시그모이드: 출력을 0과 1 사이로 압축하는 함수)](/en/terms/sigmoid-시그모이드-출력을-0과-1-사이로-압축하는-함수/)
- [Tanh (탄젠트 하이볼루메트릭: 출력을 -1과 1 사이로 압축하는 함수)](/en/terms/tanh-탄젠트-하이볼루메트릭-출력을-1과-1-사이로-압축하는-함수/)
- [Softmax (소프트맥스: 확률 분포로 변환하는 함수, 주로 분류 문제의 출력층에 사용)](/en/terms/softmax-소프트맥스-확률-분포로-변환하는-함수-주로-분류-문제의-출력층에-사용/)
