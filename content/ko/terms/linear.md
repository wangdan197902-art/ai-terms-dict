---
title: "선형(Linear)"
term_id: "linear"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Foundations"]
difficulty: 2
weight: 1
slug: "linear"
aliases:
  - /ko/terms/linear/
date: "2026-07-18T15:26:28.689529Z"
lastmod: "2026-07-18T16:38:06.777468Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "출력이 입력에 비례하는 연산이나 관계를 설명하며, 신경망 레이어의 아핀 변환의 기초를 형성합니다."
---

## Definition

선형 연산은 비선형 활성화 함수 없이 곱셈과 덧셈만을 포함합니다. 신경망에서 선형 레이어(또는 밀집 레이어)는 입력 벡터에 가중치 행렬 변환을 적용합니다.

### Summary

출력이 입력에 비례하는 연산이나 관계를 설명하며, 신경망 레이어의 아핀 변환의 기초를 형성합니다.

## Key Concepts

- 가중치 행렬(Weight Matrix)
- 아핀 변환(Affine Transformation)
- 내적(Dot Product)
- 중첩 원리(Superposition)

## Use Cases

- 특징 투영(Feature Projection)
- 로지스틱 회귀(Logistic Regression)
- 어텐션 메커니즘(Attention Mechanisms)

## Code Example

```python
import torch.nn as nn
layer = nn.Linear(10, 5)
output = layer(input_tensor)
```

## Related Terms

- [Activation Function (활성화 함수: 비선형성을 도입하는 함수)](/en/terms/activation-function-활성화-함수-비선형성을-도입하는-함수/)
- [Dense Layer (밀집 레이어: 모든 입력 노드가 출력 노드에 연결된 레이어)](/en/terms/dense-layer-밀집-레이어-모든-입력-노드가-출력-노드에-연결된-레이어/)
- [Matrix Multiplication (행렬 곱셈: 선형 대수 연산의 기본)](/en/terms/matrix-multiplication-행렬-곱셈-선형-대수-연산의-기본/)
