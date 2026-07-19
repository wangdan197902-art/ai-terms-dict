---
title: 선형 예측 함수
term_id: linear_predictor_function
category: basic_concepts
subcategory: ''
tags:
- statistics
- Linear Models
- mathematics
difficulty: 2
weight: 1
slug: linear_predictor_function
date: '2026-07-18T16:02:32.715320Z'
lastmod: '2026-07-18T16:38:06.862903Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 입력 변수들의 선형 결합을 계산하여 결과값을 예측하는 수학적 함수입니다.
---
## Definition

통계 모델링 및 머신러닝에서 선형 예측 함수는 가중치가 적용된 입력 특징들의 합과 편향 항(bias term)으로 구성됩니다. 이는 일반화 선형 모델(GLM)의 핵심 구성 요소로, 예측값의 기초를 형성합니다.

### Summary

입력 변수들의 선형 결합을 계산하여 결과값을 예측하는 수학적 함수입니다.

## Key Concepts

- 가중 합
- 편향 항
- 일반화 선형 모델
- 특징 계수

## Use Cases

- 선형 회귀 분석
- 로지스틱 회귀 분류
- 서포트 벡터 머신(커널 트릭 맥락)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (회귀 계수)](/en/terms/regression_coefficients-회귀-계수/)
- [bias_intercept (편향/절편)](/en/terms/bias_intercept-편향-절편/)
- [feature_engineering (특징 공학)](/en/terms/feature_engineering-특징-공학/)
- [generalized_linear_model (일반화 선형 모델)](/en/terms/generalized_linear_model-일반화-선형-모델/)
