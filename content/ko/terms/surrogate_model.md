---
title: 대리 모델
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T16:17:37.518726Z'
lastmod: '2026-07-18T16:38:06.912336Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 더 복잡하거나 계산 비용이 많이 들거나 접근하기 어려운 블랙박스 모델의 동작을 근사화하는 데 사용되는 단순화된 수학적 모델입니다.
---
## Definition

기계 학습 및 최적화에서 대리 모델은 직접 평가하기 어려운 대상 함수의 대리자 역할을 합니다. 원래 모델의 입력-출력 쌍을 기반으로 훈련되어, 원본 모델의 행동을 효율적으로 모사합니다.

### Summary

더 복잡하거나 계산 비용이 많이 들거나 접근하기 어려운 블랙박스 모델의 동작을 근사화하는 데 사용되는 단순화된 수학적 모델입니다.

## Key Concepts

- 모델 근사화
- 블랙박스 최적화
- 계산 효율성
- 대리 모델

## Use Cases

- 하이퍼파라미터 최적화
- 공학 설계 시뮬레이션 가속화
- 복잡한 시스템의 민감도 분석

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Bayesian Optimization (베이지안 최적화)](/en/terms/bayesian-optimization-베이지안-최적화/)
- [Gaussian Process (가우시안 프로세스)](/en/terms/gaussian-process-가우시안-프로세스/)
- [Black-Box Function (블랙박스 함수)](/en/terms/black-box-function-블랙박스-함수/)
- [Emulator (에뮬레이터)](/en/terms/emulator-에뮬레이터/)
