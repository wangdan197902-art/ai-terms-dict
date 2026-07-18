---
title: "교차 검증"
term_id: "cross_validation"
category: "training_techniques"
subcategory: ""
tags: ["evaluation", "machine-learning", "statistics"]
difficulty: 2
weight: 1
slug: "cross_validation"
aliases:
  - /ko/terms/cross_validation/
date: "2026-07-18T15:46:58.023116Z"
lastmod: "2026-07-18T16:38:06.823262Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "제한된 데이터 샘플에서 기계 학습 모델을 평가하기 위해 데이터를 훈련 및 테스트용 하위 집합으로 분할하는 재표본 추출 절차입니다."
---

## Definition

교차 검증은 기계 학습 모델의 성능을 추정하는 통계적 방법입니다. 가장 일반적인 형태는 k-폴드 교차 검증으로, 데이터를 k개의 동일한 부분으로 나눕니다. 모델은 각 폴드에서 한 번은 테스트용으로, 나머지는 학습용으로 사용됩니다.

### Summary

제한된 데이터 샘플에서 기계 학습 모델을 평가하기 위해 데이터를 훈련 및 테스트용 하위 집합으로 분할하는 재표본 추출 절차입니다.

## Key Concepts

- k-폴드 분할
- 모델 일반화
- 과적합 감지
- 성능 추정

## Use Cases

- 하이퍼파라미터 튜닝
- 다양한 알고리즘 비교
- 소규모 데이터셋에서 모델 안정성 검증

## Code Example

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X, y, cv=5)
```

## Related Terms

- [Train-Test Split (학습-테스트 분할)](/en/terms/train-test-split-학습-테스트-분할/)
- [Leave-One-Out (한 개 제외)](/en/terms/leave-one-out-한-개-제외/)
- [Bootstrap (부트스트랩)](/en/terms/bootstrap-부트스트랩/)
