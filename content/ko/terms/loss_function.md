---
title: "손실 함수"
term_id: "loss_function"
category: "basic_concepts"
subcategory: ""
tags: ["training", "mathematics", "evaluation"]
difficulty: 3
weight: 1
slug: "loss_function"
date: "2026-07-18T15:35:05.258512Z"
lastmod: "2026-07-18T16:38:06.796937Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "훈련 중 예측값과 실제 목표값 간의 차이를 정량화하는 수학적 함수입니다."
---
## Definition

비용 함수 또는 오차 함수라고도 불리는 손실 함수는 모델의 성능이 얼마나 좋은지를 나타내는 스칼라 값을 제공합니다. 훈련 중 최적화 알고리즘은 이 값을 사용하여 기울기를 계산하고 모델의 가중치를 업데이트하여 손실을 최소화합니다.

### Summary

훈련 중 예측값과 실제 목표값 간의 차이를 정량화하는 수학적 함수입니다.

## Key Concepts

- 역전파
- 기울기 계산
- 최적화
- 오차 지표

## Use Cases

- 지도 학습 모델 훈련
- 모델 성능 평가
- 하이퍼파라미터 튜닝

## Code Example

```python
import torch.nn as nn
criterion = nn.CrossEntropyLoss()
```

## Related Terms

- [backpropagation (역전파)](/en/terms/backpropagation-역전파/)
- [gradient_descent (경사 하강법)](/en/terms/gradient_descent-경사-하강법/)
- [cross_entropy (교차 엔트로피)](/en/terms/cross_entropy-교차-엔트로피/)
- [mse (평균 제곱 오차)](/en/terms/mse-평균-제곱-오차/)
