---
title: "정규화"
term_id: "regularization"
category: "basic_concepts"
subcategory: ""
tags: ["ML Basics", "Optimization", "Statistics"]
difficulty: 2
weight: 1
slug: "regularization"
aliases:
  - /ko/terms/regularization/
date: "2026-07-18T16:13:19.672860Z"
lastmod: "2026-07-18T16:38:06.903777Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "과적합을 방지하기 위해 손실 함수에 패널티를 추가하거나 모델의 복잡성을 제약하는 등 학습 중에 사용되는 일련의 기법."
---

## Definition

정규화는 기계 학습에서 일반화 오차를 크게 증가시키지 않고 줄이는 것을 목적으로 하는 중요한 개념입니다. 이는 모델이 지나치게 복잡한 패턴(노이즈 포함)을 학습하는 것을 억제함으로써 작동합니다.

### Summary

과적합을 방지하기 위해 손실 함수에 패널티를 추가하거나 모델의 복잡성을 제약하는 등 학습 중에 사용되는 일련의 기법.

## Key Concepts

- 과적합
- 편향-분산 트레이드오프
- L1/L2 패널티
- 드롭아웃

## Use Cases

- 심층 신경망 학습
- 선형 회귀 모델
- 소규모 데이터셋에서의 암기 방지

## Code Example

```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)
```

## Related Terms

- [Overfitting (과적합)](/en/terms/overfitting-과적합/)
- [Underfitting (과소적합)](/en/terms/underfitting-과소적합/)
- [Cross-validation (교차 검증)](/en/terms/cross-validation-교차-검증/)
- [Hyperparameter tuning (초매개변수 튜닝)](/en/terms/hyperparameter-tuning-초매개변수-튜닝/)
