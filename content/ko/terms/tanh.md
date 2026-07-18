---
title: "Tanh (쌍곡선 탄젠트)"
term_id: "tanh"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "mathematics"]
difficulty: 2
weight: 1
slug: "tanh"
aliases:
  - /ko/terms/tanh/
date: "2026-07-18T16:17:51.303188Z"
lastmod: "2026-07-18T16:38:06.913356Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "Tanh(쌍곡선 탄젠트)는 입력 값을 -1에서 1 사이의 범위로 매핑하는 활성화 함수입니다."
---

## Definition

쌍곡선 탄젠트(Tanh) 함수는 신경망에서 널리 사용되는 비선형 활성화 함수입니다. 이 함수는 입력 값을 구간 (-1, 1)으로 압축하여 제로 중심(zero-centered)의 출력을 제공합니다. 이는 시그모이드 함수의 단점인 출력의 편향을 해결하며, 역전파 과정에서 그래디언트 소실 문제를 완화하는 데 도움이 됩니다. 특히 순환 신경망(RNN)의 게이트 메커니즘 등에서 자주 활용됩니다.

### Summary

Tanh(쌍곡선 탄젠트)는 입력 값을 -1에서 1 사이의 범위로 매핑하는 활성화 함수입니다.

## Key Concepts

- 활성화 함수
- 비선형성
- 제로 중심 출력
- 역전파

## Use Cases

- 순환 신경망
- LSTM 셀 게이트
- 다층 퍼셉트론의 은닉층

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (시그모이드)](/en/terms/sigmoid-시그모이드/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (신경망)](/en/terms/neural_networks-신경망/)
