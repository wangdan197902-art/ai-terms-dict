---
title: "지도 학습"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /ko/terms/supervised_learning/
date: "2026-07-18T15:36:33.155994Z"
lastmod: "2026-07-18T16:38:06.800783Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델이 레이블이 지정된 훈련 예제를 기반으로 입력을 출력으로 매핑하도록 학습하는 머신러닝 패러다임입니다."
---

## Definition

지도 학습에서는 알고리즘이 레이블이 지정된 데이터셋으로 훈련되며, 각 입력 예제는 올바른 출력과 짝을 이룹니다. 목표는 모델이 입력과 출력 사이의 근본적인 관계를 학습하도록 하는 것입니다.

### Summary

모델이 레이블이 지정된 훈련 예제를 기반으로 입력을 출력으로 매핑하도록 학습하는 머신러닝 패러다임입니다.

## Key Concepts

- 레이블 데이터
- 입출력 매핑
- 분류
- 회귀

## Use Cases

- 스팸 이메일 감지
- 주택 가격 예측
- 이미지 인식

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (비지도 학습)](/en/terms/unsupervised-learning-비지도-학습/)
- [Training Set (훈련 세트)](/en/terms/training-set-훈련-세트/)
- [Validation Set (검증 세트)](/en/terms/validation-set-검증-세트/)
- [Model Accuracy (모델 정확도)](/en/terms/model-accuracy-모델-정확도/)
