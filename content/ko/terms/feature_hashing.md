---
title: 피처 해싱 (Feature Hashing)
term_id: feature_hashing
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- Text Mining
- Optimization
difficulty: 3
weight: 1
slug: feature_hashing
date: '2026-07-18T15:55:33.510356Z'
lastmod: '2026-07-18T16:38:06.840086Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 고차원의 희소 피처를 해시 함수를 사용하여 고정 크기의 벡터로 매핑하는 기법입니다.
---
## Definition

해시 트릭이라고도 불리는 피처 해싱은 머신러닝 모델이 피처와 인덱스 간의 명시적인 매핑 테이블을 유지하지 않고도 대규모 희소 피처 공간을 처리할 수 있게 해줍니다. 해시 함수를 적용함으로써 메모리 효율성을 높이고 차원 축소를 수행합니다.

### Summary

고차원의 희소 피처를 해시 함수를 사용하여 고정 크기의 벡터로 매핑하는 기법입니다.

## Key Concepts

- 해시 함수
- 희소 벡터
- 차원 축소
- 메모리 효율성

## Use Cases

- 대규모 어휘를 가진 텍스트 분류
- 거대한 아이템 집합을 다루는 추천 시스템
- 실시간 스트리밍 데이터 처리

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-hot encoding (원-핫 인코딩)](/en/terms/one-hot-encoding-원-핫-인코딩/)
- [Bag of Words (단어 빈도 벡터)](/en/terms/bag-of-words-단어-빈도-벡터/)
- [Dimensionality reduction (차원 축소)](/en/terms/dimensionality-reduction-차원-축소/)
- [Sparse matrix (희소 행렬)](/en/terms/sparse-matrix-희소-행렬/)
