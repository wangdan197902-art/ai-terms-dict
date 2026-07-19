---
title: 전이 학습
term_id: transfer_learning
category: training_techniques
subcategory: ''
tags:
- Optimization
- efficiency
- Deep Learning
difficulty: 3
weight: 1
slug: transfer_learning
date: '2026-07-18T15:30:34.141633Z'
lastmod: '2026-07-18T16:38:06.786643Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 하나의 작업 위해 개발된 모델을 재사용하여 두 번째 작업의 모델 시작점으로 사용하는 머신러닝 기법입니다.
---
## Definition

전이 학습은 사전 훈련된 모델을 활용하여 새로운 관련 작업에서 성능을 향상시키고 훈련 시간을 단축합니다. 처음부터 훈련하는 대신, 개발자는 기존 가중치를 미세 조정(fine-tune)하여 효율성을 높입니다.

### Summary

하나의 작업 위해 개발된 모델을 재사용하여 두 번째 작업의 모델 시작점으로 사용하는 머신러닝 기법입니다.

## Key Concepts

- 사전 훈련된 모델
- 미세 조정(Fine-tuning)
- 도메인 적응(Domain Adaptation)
- 특징 추출(Feature Extraction)

## Use Cases

- 제한된 데이터가 있는 이미지 분류
- 니치 주제에 대한 감성 분석
- 의료 진단 보조

## Code Example

```python
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
```

## Related Terms

- [fine_tuning (미세 조정)](/en/terms/fine_tuning-미세-조정/)
- [pre_training (사전 훈련)](/en/terms/pre_training-사전-훈련/)
- [domain_adaptation (도메인 적응)](/en/terms/domain_adaptation-도메인-적응/)
- [few_shot_learning (소수 학습)](/en/terms/few_shot_learning-소수-학습/)
