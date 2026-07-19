---
title: 피 계수(Phi coefficient)
term_id: phi_coefficient
category: basic_concepts
subcategory: ''
tags:
- statistics
- Evaluation Metrics
- Binary Classification
difficulty: 3
weight: 1
slug: phi_coefficient
date: '2026-07-18T16:09:36.005151Z'
lastmod: '2026-07-18T16:38:06.896490Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 두 이항 변수(binary variables) 간의 연관성을 측정하는 통계적 지표.
---
## Definition

피 계수(φ)는 두 개의 이항 변수 간 연관성을 측정하는 지표로, 이분형 변수에 대한 피어슨 상관계수(Pearson correlation coefficient)와 같습니다. 값은 -1부터 +1까지 범위를 가지며, 0은 연관성이 없음을, ±1은 완전한 양의 또는 음의 연관성을 나타냅니다.

### Summary

두 이항 변수(binary variables) 간의 연관성을 측정하는 통계적 지표.

## Key Concepts

- 이항 변수(Binary variables)
- 상관관계(Correlation)
- 연표(Contingency table)
- 연관 강도(Association strength)

## Use Cases

- 정확도(Accuracy) 외에도 이진 분류기 성능 평가
- 예/아니오 응답이 있는 설문 데이터 관계 분석
- 범주형 입력 데이터셋의 특징 선택(Feature selection)

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [Cramer's V (크래머 V 계수)](/en/terms/cramer-s-v-크래머-v-계수/)
- [Pearson correlation (피어슨 상관계수)](/en/terms/pearson-correlation-피어슨-상관계수/)
- [Confusion matrix (혼동 행렬)](/en/terms/confusion-matrix-혼동-행렬/)
- [Mutual information (상호 정보량)](/en/terms/mutual-information-상호-정보량/)
