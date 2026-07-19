---
title: 이진 분류기 평가
term_id: evaluation_of_binary_classifiers
category: basic_concepts
subcategory: ''
tags:
- metrics
- Classification
- evaluation
difficulty: 2
weight: 1
slug: evaluation_of_binary_classifiers
date: '2026-07-18T15:54:50.648688Z'
lastmod: '2026-07-18T16:38:06.837983Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 두 가지 가능한 결과 중 하나를 예측하는 기계 학습 모델의 성능을 평가하는 과정입니다.
---
## Definition

이 분야에는 정확도, 정밀도, 재현율, F1 점수 및 ROC 곡선 아래 면적(AUC-ROC) 등의 지표를 분석하는 작업이 포함됩니다. 이는 모델이 두 클래스를 얼마나 잘 구분하는지 결정하는 데 도움이 됩니다.

### Summary

두 가지 가능한 결과 중 하나를 예측하는 기계 학습 모델의 성능을 평가하는 과정입니다.

## Key Concepts

- 혼동 행렬
- 정밀도-재현율 트레이드오프
- ROC 곡선
- F1 점수

## Use Cases

- 의료 질병 스크리닝
- 스팸 이메일 필터링
- 신용 위험 평가

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (혼동 행렬)](/en/terms/confusion_matrix-혼동-행렬/)
- [roc_auc (ROC-AUC)](/en/terms/roc_auc-roc-auc/)
- [precision_recall (정밀도-재현율)](/en/terms/precision_recall-정밀도-재현율/)
- [cross_validation (교차 검증)](/en/terms/cross_validation-교차-검증/)
