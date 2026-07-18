---
title: "피처 스케일링"
term_id: "feature_scaling"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "statistics", "optimization"]
difficulty: 2
weight: 1
slug: "feature_scaling"
aliases:
  - /ko/terms/feature_scaling/
date: "2026-07-18T15:55:47.592237Z"
lastmod: "2026-07-18T16:38:06.840321Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "데이터의 독립 변수 또는 피처 범위를 정규화하여 크기의 균일성을 보장하는 과정입니다."
---

## Definition

피처 스케일링은 입력 변수의 범위를 표준화하여, 크기가 큰 피처가 학습 과정을 지배하는 것을 방지합니다. 일반적인 방법으로는 정규화(최소-최대 스케일링)와 표준화가 있습니다.

### Summary

데이터의 독립 변수 또는 피처 범위를 정규화하여 크기의 균일성을 보장하는 과정입니다.

## Key Concepts

- 정규화
- 표준화
- 경사 하강법
- 데이터 전처리

## Use Cases

- 신경망 훈련
- K-평균 클러스터링
- 서포트 벡터 머신(SVM)

## Code Example

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
```

## Related Terms

- [Min-Max Scaling (최소-최대 스케일링)](/en/terms/min-max-scaling-최소-최대-스케일링/)
- [Z-score Normalization (Z-점수 정규화)](/en/terms/z-score-normalization-z-점수-정규화/)
- [Data preprocessing (데이터 전처리)](/en/terms/data-preprocessing-데이터-전처리/)
- [Gradient Descent (경사 하강법)](/en/terms/gradient-descent-경사-하강법/)
