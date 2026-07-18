---
title: "데이터 증강"
term_id: "data_augmentation"
category: "training_techniques"
subcategory: ""
tags: ["machine_learning", "preprocessing", "cv"]
difficulty: 2
weight: 1
slug: "data_augmentation"
aliases:
  - /ko/terms/data_augmentation/
date: "2026-07-18T15:47:12.733776Z"
lastmod: "2026-07-18T16:38:06.824104Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "기존 데이터 포인트에 변환을 적용하여 훈련 데이터셋의 다양성과 크기를 증가시키는 기법입니다."
---

## Definition

이 방법은 기존 샘플의 수정된 버전(예: 이미지 회전, 오디오 노이즈 추가, 텍스트 동의어 교체 등)을 생성하여 훈련 데이터셋을 인위적으로 확장합니다. 이를 통해 모델의 일반화 능력을 향상시키고 과적합(overfitting)을 방지하며, 제한된 데이터로도 강력한 모델을 학습시킬 수 있습니다.

### Summary

기존 데이터 포인트에 변환을 적용하여 훈련 데이터셋의 다양성과 크기를 증가시키는 기법입니다.

## Key Concepts

- 과적합 방지
- 데이터셋 확장
- 일반화
- 변환

## Use Cases

- 컴퓨터 비전 모델의 강건성 향상
- 제한된 텍스트 데이터로 NLP 모델 성능 개선
- 불균형 데이터셋 균형 맞추기

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularization (정규화)](/en/terms/regularization-정규화/)
- [Synthetic Data (합성 데이터)](/en/terms/synthetic-data-합성-데이터/)
- [Transfer Learning (전이 학습)](/en/terms/transfer-learning-전이-학습/)
- [Overfitting (과적합)](/en/terms/overfitting-과적합/)
