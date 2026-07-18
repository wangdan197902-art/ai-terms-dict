---
title: "드롭아웃"
term_id: "dropout"
category: "basic_concepts"
subcategory: ""
tags: ["Deep Learning", "Regularization", "Model Training"]
difficulty: 3
weight: 1
slug: "dropout"
aliases:
  - /ko/terms/dropout/
date: "2026-07-18T15:34:04.841976Z"
lastmod: "2026-07-18T16:38:06.794421Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "과적합을 방지하기 위해 학습 중에 무작위로 일부 뉴런을 무시하는 정규화 기법입니다."
---

## Definition

신경망에서 드롭아웃은 각 학습 단계마다 무작위로 선택된 뉴런의 하위 집합을 임시로 제거하여 과적합을 방지합니다. 이는 네트워크가 결합된 상황에서 유용한 견고한 특징을 학습하도록 강제합니다.

### Summary

과적합을 방지하기 위해 학습 중에 무작위로 일부 뉴런을 무시하는 정규화 기법입니다.

## Key Concepts

- 정규화
- 과적합 방지
- 신경망
- 무작위 억제

## Use Cases

- 심층 순방향 신경망 학습
- 대형 언어 모델의 일반화 성능 향상
- 특정 뉴런 경로에 대한 계산 의존성 감소

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(100, 50),
    nn.Dropout(0.5),
    nn.ReLU(),
    nn.Linear(50, 10)
)
```

## Related Terms

- [L2 Regularization (L2 정규화)](/en/terms/l2-regularization-l2-정규화/)
- [Batch Normalization (배치 정규화)](/en/terms/batch-normalization-배치-정규화/)
- [Overfitting (과적합)](/en/terms/overfitting-과적합/)
- [Generalization (일반화)](/en/terms/generalization-일반화/)
