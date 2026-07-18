---
title: "피처 엔지니어링 (Feature Engineering)"
term_id: "feature_engineering"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "technique", "optimization"]
difficulty: 3
weight: 1
slug: "feature_engineering"
aliases:
  - /ko/terms/feature_engineering/
date: "2026-07-18T15:55:33.510310Z"
lastmod: "2026-07-18T16:38:06.839958Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "도메인 지식을 활용하여 새로운 피처를 생성하거나 기존 피처를 수정하여 머신러닝 모델의 성능을 향상시키는 관행입니다."
---

## Definition

피처 엔지니어링은 도메인 전문 지식을 활용하여 원시 데이터를 머신러닝 알고리즘이 하위 패턴을 더 잘 파악할 수 있는 형태로 변환하는 기술입니다. 이 과정에는 기존 변수의 조합, 변환, 생성 등이 포함되며, 모델의 예측 능력을 결정하는 핵심 단계입니다.

### Summary

도메인 지식을 활용하여 새로운 피처를 생성하거나 기존 피처를 수정하여 머신러닝 모델의 성능을 향상시키는 관행입니다.

## Key Concepts

- 도메인 지식
- 데이터 변환
- 모델 성능
- 변수 생성

## Use Cases

- 회귀 모델 정확도 향상
- 분류 경계 강화
- 시계열 예측 최적화

## Code Example

```python
df['new_feature'] = df['feature_a'] * df['feature_b']
```

## Related Terms

- [Feature Extraction (피처 추출)](/en/terms/feature-extraction-피처-추출/)
- [Data Preprocessing (데이터 전처리)](/en/terms/data-preprocessing-데이터-전처리/)
- [Model Tuning (모델 튜닝)](/en/terms/model-tuning-모델-튜닝/)
- [Domain Expertise (도메인 전문성)](/en/terms/domain-expertise-도메인-전문성/)
