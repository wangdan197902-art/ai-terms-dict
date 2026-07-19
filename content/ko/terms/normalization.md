---
title: 정규화
term_id: normalization
category: basic_concepts
subcategory: ''
tags:
- Data Preprocessing
- mathematics
- ML Basics
difficulty: 2
weight: 1
slug: normalization
date: '2026-07-18T16:07:56.829563Z'
lastmod: '2026-07-18T16:38:06.891612Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 정규화는 모델의 수렴 속도와 성능을 향상시키기 위해 수치형 특성을 일반적으로 0과 1 사이의 표준 범위로 스케일링하는 데이터
  전처리 기법입니다.
---
## Definition

주요 방법으로는 Min-Max 스케일링과 Z-점수 표준화가 있습니다. 이 과정은 특히 경사 기반 최적화 알고리즘에서 크기가 큰 특성이 학습 과정을 지배하는 것을 방지하여 모델의 안정성을 높입니다.

### Summary

정규화는 모델의 수렴 속도와 성능을 향상시키기 위해 수치형 특성을 일반적으로 0과 1 사이의 표준 범위로 스케일링하는 데이터 전처리 기법입니다.

## Key Concepts

- Min-Max 스케일링
- Z-점수 표준화
- 특성 스케일링
- 경사 하강법 안정성

## Use Cases

- 이미지 픽셀 값 전처리
- 신경망용 표 형식 데이터 준비
- 회귀 모델 정확도 향상

## Code Example

```python
from sklearn.preprocessing import MinMaxScaler
import numpy as np
data = np.array([[10], [20], [30]])
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)
```

## Related Terms

- [Standardization (표준화)](/en/terms/standardization-표준화/)
- [Data Preprocessing (데이터 전처리)](/en/terms/data-preprocessing-데이터-전처리/)
- [Feature Engineering (특성 공학)](/en/terms/feature-engineering-특성-공학/)
