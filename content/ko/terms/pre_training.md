---
title: "사전 학습"
term_id: "pre_training"
category: "training_techniques"
subcategory: ""
tags: ["deep-learning", "nlp", "training"]
difficulty: 4
weight: 1
slug: "pre_training"
aliases:
  - /ko/terms/pre_training/
date: "2026-07-18T15:27:55.305857Z"
lastmod: "2026-07-18T16:38:06.781173Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "특정 작업에 대한 파인튜닝(fine-tuning) 전에 일반적 표현을 학습하기 위해 대규모 비라벨 데이터셋으로 머신러닝 모델을 초기 단계에서 훈련하는 과정입니다."
---

## Definition

사전 학습(pre-training)은 딥러닝의 기초 기술로, 모델이 레이블이 없는 방대한 양의 데이터로부터 광범위한 특징과 패턴을 학습하는 과정을 말합니다. 이 과정을 통해 모델은 특정 작업에 적응할 수 있는 기반 능력을 갖추게 됩니다.

### Summary

특정 작업에 대한 파인튜닝(fine-tuning) 전에 일반적 표현을 학습하기 위해 대규모 비라벨 데이터셋으로 머신러닝 모델을 초기 단계에서 훈련하는 과정입니다.

## Key Concepts

- 전이 학습(Transfer Learning)
- 특징 추출(Feature Extraction)
- 대규모 데이터(Large-Scale Data)
- 파인튜닝(Fine-Tuning)

## Use Cases

- BERT 또는 GPT 언어 모델 훈련
- ImageNet 가중치를 이용한 CNN 초기화
- 멀티모달 AI를 위한 파운데이션 모델 구축

## Code Example

```python
from transformers import BertModel
model = BertModel.from_pretrained('bert-base-uncased')
# Model is now pre-trained and ready for fine-tuning
```

## Related Terms

- [Fine-tuning (파인튜닝)](/en/terms/fine-tuning-파인튜닝/)
- [Foundation Model (파운데이션 모델)](/en/terms/foundation-model-파운데이션-모델/)
- [Unsupervised Learning (비지도 학습)](/en/terms/unsupervised-learning-비지도-학습/)
- [Transfer Learning (전이 학습)](/en/terms/transfer-learning-전이-학습/)
