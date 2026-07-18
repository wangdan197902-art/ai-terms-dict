---
title: "혼동 행렬 (Confusion Matrix)"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /ko/terms/confusion_matrix/
date: "2026-07-18T15:46:14.271492Z"
lastmod: "2026-07-18T16:38:06.820186Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "혼동 행렬은 분류 모델이 테스트 데이터 세트에서 수행한 결과를 설명하는 표입니다."
---

## Definition

혼동 행렬은 알고리즘(일반적으로 지도 학습 모델)의 성능을 시각화하기 위해 사용되는 특정 표 레이아웃입니다. 이 표는 참 양성(True Positive), 참 음성(True Negative), 거짓 양성(False Positive), 거짓 음성(False Negative)의 빈도를 보여주어 모델의 정확도와 오류 유형을 파악하는 데 도움을 줍니다.

### Summary

혼동 행렬은 분류 모델이 테스트 데이터 세트에서 수행한 결과를 설명하는 표입니다.

## Key Concepts

- 참 양성 (True Positives)
- 거짓 음성 (False Negatives)
- 정밀도 (Precision)
- 재현율 (Recall)

## Use Cases

- 이진 분류기 평가
- 다중 클래스 분류 성능 분석
- 불균형 데이터셋에서의 모델 편향 디버깅

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (정밀도: 양성으로 예측된 것 중 실제 양성의 비율)](/en/terms/precision-정밀도-양성으로-예측된-것-중-실제-양성의-비율/)
- [recall (재현율: 실제 양성 중 올바르게 양성으로 예측된 비율)](/en/terms/recall-재현율-실제-양성-중-올바르게-양성으로-예측된-비율/)
- [F1 score (F1 점정: 정밀도와 재현율의 조화 평균)](/en/terms/f1-score-f1-점정-정밀도와-재현율의-조화-평균/)
- [ROC curve (ROC 곡선: 민감도와 특이도의 트레이드오프를 시각화한 그래프)](/en/terms/roc-curve-roc-곡선-민감도와-특이도의-트레이드오프를-시각화한-그래프/)
