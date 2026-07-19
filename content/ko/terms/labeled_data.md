---
title: 라벨 데이터
term_id: labeled_data
category: basic_concepts
subcategory: ''
tags:
- data
- Supervised Learning
- fundamentals
difficulty: 1
weight: 1
slug: labeled_data
date: '2026-07-18T16:01:36.612965Z'
lastmod: '2026-07-18T16:38:06.859230Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 입력 특징과 함께 정답 출력이나 대상 값이 제공된 데이터입니다.
---
## Definition

라벨 데이터는 입력 샘플에 해당하는 정답(Ground Truth) 라벨과 쌍을 이루어, 지도 기계 학습의 기초를 형성합니다. 이를 통해 알고리즘은 입력과 출력 간의 매핑 관계를 학습할 수 있습니다.

### Summary

입력 특징과 함께 정답 출력이나 대상 값이 제공된 데이터입니다.

## Key Concepts

- 지도 학습(Supervised Learning)
- 정답(Ground Truth)
- 애노테이션(Annotation)
- 대상 변수(Target Variable)

## Use Cases

- 이미지 분류기 훈련
- 음성 인식 시스템 구축
- 금융 분야의 예측 모델링

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (비라벨 데이터)](/en/terms/unlabeled_data-비라벨-데이터/)
- [supervised_learning (지도 학습)](/en/terms/supervised_learning-지도-학습/)
- [data_annotation (데이터 애노테이션)](/en/terms/data_annotation-데이터-애노테이션/)
- [training_set (훈련 세트)](/en/terms/training_set-훈련-세트/)
