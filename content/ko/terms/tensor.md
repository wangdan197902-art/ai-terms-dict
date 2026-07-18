---
title: "텐서"
term_id: "tensor"
category: "basic_concepts"
subcategory: ""
tags: ["math", "data-structures", "pytorch"]
difficulty: 2
weight: 1
slug: "tensor"
aliases:
  - /ko/terms/tensor/
date: "2026-07-18T16:17:51.303222Z"
lastmod: "2026-07-18T16:38:06.913615Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "딥러닝 프레임워크의 기본 데이터 구조로 사용되는 다차원 배열입니다."
---

## Definition

컴퓨터 과학과 딥러닝에서 텐서는 스칼라, 벡터, 행렬을 고차원으로 일반화한 수학적 객체입니다. 텐서는 차원의 수인 랭크(rank)와 각 차원의 크기인 모양(shape)으로 특징지어집니다. 딥러닝 라이브러리(예: PyTorch, TensorFlow)에서는 연산 효율성을 위해 GPU 가속이 가능한 다차원 배열 형태로 데이터를 관리하며, 신경망의 입력, 가중치, 출력 등을 표현하는 핵심 요소입니다.

### Summary

딥러닝 프레임워크의 기본 데이터 구조로 사용되는 다차원 배열입니다.

## Key Concepts

- 랭크
- 모양(Shape)
- 차원성
- 브로드캐스팅

## Use Cases

- 이미지 처리 (4D 텐서)
- 신경망 가중치 저장
- 배치 데이터 입력

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix (행렬)](/en/terms/matrix-행렬/)
- [Vector (벡터)](/en/terms/vector-벡터/)
- [Deep Learning (딥러닝)](/en/terms/deep-learning-딥러닝/)
- [NumPy (넘파이)](/en/terms/numpy-넘파이/)
