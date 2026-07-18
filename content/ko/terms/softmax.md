---
title: "소프트맥스(Softmax)"
term_id: "softmax"
category: "basic_concepts"
subcategory: ""
tags: ["math", "neural-networks", "classification"]
difficulty: 2
weight: 1
slug: "softmax"
aliases:
  - /ko/terms/softmax/
date: "2026-07-18T15:36:19.379637Z"
lastmod: "2026-07-18T16:38:06.800461Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "임의의 실수 값 점수 벡터를 확률 분포로 변환하는 수학적 함수입니다."
---

## Definition

소프트맥스는 다중 클래스 분류 작업에서 신경망의 출력층에 널리 사용됩니다. 이는 원시 로짓(raw logits) 벡터를 입력받아 정규화하며, 각 요소가 특정 클래스에 속할 확률을 나타내도록 합니다...

### Summary

임의의 실수 값 점수 벡터를 확률 분포로 변환하는 수학적 함수입니다.

## Key Concepts

- 확률 분포
- 로짓(Logits)
- 정규화(Normalization)
- 다중 클래스 분류

## Use Cases

- 이미지 분류 출력층
- 언어 모델 토큰 예측
- 다중 레이블 범주화

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (최댓값 인덱스 반환 함수)](/en/terms/argmax-최댓값-인덱스-반환-함수/)
- [Cross-Entropy Loss (교차 엔트로피 손실)](/en/terms/cross-entropy-loss-교차-엔트로피-손실/)
- [Logits (로짓)](/en/terms/logits-로짓/)
- [Neural Network (신경망)](/en/terms/neural-network-신경망/)
