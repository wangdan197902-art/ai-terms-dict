---
title: "인스턴스 기반 학습"
term_id: "instance_based_learning"
category: "training_techniques"
subcategory: ""
tags: ["algorithm", "lazy_learning", "classification"]
difficulty: 2
weight: 1
slug: "instance_based_learning"
aliases:
  - /ko/terms/instance_based_learning/
date: "2026-07-18T16:00:18.596088Z"
lastmod: "2026-07-18T16:38:06.855262Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "새로운 입력을 저장된 훈련 인스턴스와 비교하여 예측을 수행하는 지연 학습(lazy learning) 접근법입니다."
---

## Definition

기억 기반 학습이라고도 알려진 이 기법은 훈련 중에 일반화된 모델을 구축하지 않습니다. 대신 전체 훈련 데이터셋을 저장합니다. 예측이 필요할 때 가장 유사한 인스턴스를 찾아 기반으로 예측을 생성합니다.

### Summary

새로운 입력을 저장된 훈련 인스턴스와 비교하여 예측을 수행하는 지연 학습(lazy learning) 접근법입니다.

## Key Concepts

- 지연 학습
- 유사도 지표
- K-최근접 이웃(KNN)
- 기반 학습

## Use Cases

- 추천 시스템
- 패턴 인식
- 소규모부터 중규모 데이터셋

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```

## Related Terms

- [KNN (K-최근접 이웃 알고리즘)](/en/terms/knn-k-최근접-이웃-알고리즘/)
- [Similarity search (유사도 검색)](/en/terms/similarity-search-유사도-검색/)
- [Lazy learning (지연 학습)](/en/terms/lazy-learning-지연-학습/)
- [Kernel methods (커널 방법)](/en/terms/kernel-methods-커널-방법/)
