---
title: "시그모이드"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
aliases:
  - /ko/terms/sigmoid/
date: "2026-07-18T16:15:19.466639Z"
lastmod: "2026-07-18T16:38:06.907674Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "임의의 실수 값을 0과 1 사이의 값으로 매핑하여 S자 곡선을 형성하는 수학적 함수입니다."
---

## Definition

σ(z) = 1 / (1 + e^-z)로 정의되는 시그모이드 함수는 머신러닝에서 확률을 모델링하는 데 널리 사용됩니다. 이 함수는 입력값을 (0, 1) 범위로 압축하여 이진 분류에 적합하게 만듭니다.

### Summary

임의의 실수 값을 0과 1 사이의 값으로 매핑하여 S자 곡선을 형성하는 수학적 함수입니다.

## Key Concepts

- 로지스틱 함수(Logistic function)
- 확률 매핑(Probability mapping)
- 기울기 소실(Vanishing gradient)
- 비선형성(Non-linearity)

## Use Cases

- 이진 분류 출력
- 로지스틱 회귀
- 얕은 신경망의 활성화 함수

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU (Rectified Linear Unit, 선형 활성화 함수)](/en/terms/relu-rectified-linear-unit-선형-활성화-함수/)
- [Softmax (소프트맥스)](/en/terms/softmax-소프트맥스/)
- [Logistic Regression (로지스틱 회귀)](/en/terms/logistic-regression-로지스틱-회귀/)
- [Activation Function (활성화 함수)](/en/terms/activation-function-활성화-함수/)
