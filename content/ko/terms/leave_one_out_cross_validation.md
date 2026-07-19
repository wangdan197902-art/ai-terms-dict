---
title: 홀드아웃 교차 검증
term_id: leave_one_out_cross_validation
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- evaluation
- statistics
difficulty: 3
weight: 1
slug: leave_one_out_cross_validation
date: '2026-07-18T16:02:04.377989Z'
lastmod: '2026-07-18T16:38:06.862283Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 모델이 모든 샘플 중 하나를 제외하고 학습하고, 그 단일 홀드아웃 샘플로 테스트하는 엄격한 재표본 추출 기법으로, 모든 데이터
  포인트에 대해 반복됩니다.
---
## Definition

홀드아웃 교차 검증(LOOCV)은 k가 데이터셋의 샘플 수와 같아지는 k-폴드 교차 검증의 특정 경우입니다. 이는 모델 성능에 대해 거의 편향되지 않은 추정을 제공합니다.

### Summary

모델이 모든 샘플 중 하나를 제외하고 학습하고, 그 단일 홀드아웃 샘플로 테스트하는 엄격한 재표본 추출 기법으로, 모든 데이터 포인트에 대해 반복됩니다.

## Key Concepts

- 재표본 추출
- 모델 평가
- 편향-분산 트레이드오프
- 계산 비용

## Use Cases

- 소규모 의료 데이터셋에서 모델 평가
- 데이터가 부족할 때 하이퍼파라미터 튜닝
- 알고리즘 성능을 엄격하게 비교

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (k-폴드 교차 검증)](/en/terms/k-fold-cross-validation-k-폴드-교차-검증/)
- [train_test_split (훈련/테스트 분할)](/en/terms/train_test_split-훈련-테스트-분할/)
- [bootstrap (부트스트랩)](/en/terms/bootstrap-부트스트랩/)
- [cross_validation_score (교차 검증 점수)](/en/terms/cross_validation_score-교차-검증-점수/)
