---
title: "Dense (밀집)"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /ko/terms/dense/
date: "2026-07-18T15:51:42.693331Z"
lastmod: "2026-07-18T16:38:06.831108Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "이전 레이어나 차원의 모든 요소가 현재 레이어나 차원의 모든 요소와 연결된 레이어 또는 텐서를 의미합니다."
---

## Definition

신경망에서 'dense'(밀집)는 각 뉴런이 이전 레이어의 모든 뉴런으로부터 입력을 받는 완전 연결 레이어를 지칭합니다. 이는 합성곱이나...

### Summary

이전 레이어나 차원의 모든 요소가 현재 레이어나 차원의 모든 요소와 연결된 레이어 또는 텐서를 의미합니다.

## Key Concepts

- 완전 연결(Fully Connected)
- 가중치 행렬(Weight Matrix)
- 활성화 함수(Activation Function)
- 특징 통합(Feature Integration)

## Use Cases

- MLP의 최종 분류 레이어
- 하이브리드 모델의 특징 융합
- 단순 회귀 작업

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (순방향 신경망)](/en/terms/feedforward-neural-network-순방향-신경망/)
- [Backpropagation (역전파)](/en/terms/backpropagation-역전파/)
- [ReLU (Rectified Linear Unit)](/en/terms/relu-rectified-linear-unit/)
- [Bias Term (편향 항)](/en/terms/bias-term-편향-항/)
