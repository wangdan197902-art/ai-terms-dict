---
title: "자동 머신러닝(AutoML)"
term_id: "automated_machine_learning"
category: "training_techniques"
subcategory: ""
tags: ["automation", "efficiency", "workflow"]
difficulty: 3
weight: 1
slug: "automated_machine_learning"
aliases:
  - /ko/terms/automated_machine_learning/
date: "2026-07-18T15:42:50.870747Z"
lastmod: "2026-07-18T16:38:06.811363Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "실제 문제에 머신러닝을 적용하는 전체 과정을 자동화하여 수동 노력을 줄이는 방법론입니다."
---

## Definition

AutoML(자동 머신러닝)은 데이터 전처리, 특징 공학, 모델 선택 및 하이퍼파라미터 튜닝 등의 작업을 자동화하여 ML 모델 개발을 간소화합니다. 이는...

### Summary

실제 문제에 머신러닝을 적용하는 전체 과정을 자동화하여 수동 노력을 줄이는 방법론입니다.

## Key Concepts

- 하이퍼파라미터 튜닝
- 특징 공학
- 모델 선택
- 민주화(Democratization)

## Use Cases

- 비즈니스 분석가를 위한 신속한 프로토타이핑
- 대규모 생산 파이프라인 최적화
- 여러 알고리즘의 자동 비교

## Code Example

```python
from auto_ml import Predictor
predictor = Predictor(type_of_estimator='classifier')
predictor.fit(dataframe, target='label')
```

## Related Terms

- [Hyperparameter Optimization (하이퍼파라미터 최적화)](/en/terms/hyperparameter-optimization-하이퍼파라미터-최적화/)
- [Neural Architecture Search (신경망 아키텍처 탐색)](/en/terms/neural-architecture-search-신경망-아키텍처-탐색/)
- [MLOps (머신러닝 운영)](/en/terms/mlops-머신러닝-운영/)
- [No-Code AI (노코드 AI)](/en/terms/no-code-ai-노코드-ai/)
