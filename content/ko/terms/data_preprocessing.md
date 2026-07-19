---
title: "데이터 전처리(Data Preprocessing)"
term_id: "data_preprocessing"
category: "basic_concepts"
subcategory: ""
tags: ["pipeline", "cleaning", "standardization"]
difficulty: 2
weight: 1
slug: "data_preprocessing"
date: "2026-07-18T15:47:25.983512Z"
lastmod: "2026-07-18T16:38:06.824758Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "원시 데이터를 머신러닝 알고리즘이 사용할 수 있는 깨끗하고 일관된 형식으로 변환하는 과정입니다."
---
## Definition

데이터 전처리는 원시, 비구조화 또는 노이즈가 많은 데이터를 머신러닝 모델이 효과적으로 처리할 수 있는 표준화된 형식으로 변환하는 필수 작업입니다. 이 단계에는 일반적으로 데이터 정제, 정규화, 인코딩 등이 포함됩니다.

### Summary

원시 데이터를 머신러닝 알고리즘이 사용할 수 있는 깨끗하고 일관된 형식으로 변환하는 과정입니다.

## Key Concepts

- 데이터 정제(Data Cleaning)
- 정규화(Normalization)
- 인코딩(Encoding)
- 특징 스케일링(Feature Scaling)

## Use Cases

- 신경망 수렴을 위한 수치 입력 스케일링
- 텍스트 레이블을 수치 벡터로 변환
- 센서 데이터의 누락된 값 보간

## Code Example

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(raw_data)
```

## Related Terms

- [data_augmentation (데이터 증강)](/en/terms/data_augmentation-데이터-증강/)
- [feature_selection (특징 선택)](/en/terms/feature_selection-특징-선택/)
- [normalization (정규화)](/en/terms/normalization-정규화/)
- [one_hot_encoding (원-핫 인코딩)](/en/terms/one_hot_encoding-원-핫-인코딩/)
