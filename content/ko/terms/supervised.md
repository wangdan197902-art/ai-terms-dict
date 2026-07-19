---
title: "지도(Supervised)"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
date: "2026-07-18T15:29:16.430343Z"
lastmod: "2026-07-18T16:38:06.784993Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델이 레이블이 지정된 입력-출력 쌍으로 학습하는 머신러닝 패러다임입니다."
---
## Definition

지도 학습은 알고리즘에 입력과 정답(레이블)이 모두 포함된 데이터를 공급하는 과정을 포함합니다. 모델은 예측 오차를 최소화함으로써 입력을 출력으로 매핑하는 방법을 학습합니다. 이 기술은

### Summary

모델이 레이블이 지정된 입력-출력 쌍으로 학습하는 머신러닝 패러다임입니다.

## Key Concepts

- 레이블 데이터(Labeled data)
- 매핑(Mapping)
- 손실 최소화(Loss minimization)

## Use Cases

- 이미지 분류(Image classification)
- 스팸 감지(Spam detection)
- 가격 예측(Price prediction)

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (비지도)](/en/terms/unsupervised-비지도/)
- [Label (레이블)](/en/terms/label-레이블/)
- [Regression (회귀)](/en/terms/regression-회귀/)
