---
title: 에포크
term_id: epoch
category: training_techniques
subcategory: ''
tags:
- training
- Neural Networks
- basics
difficulty: 2
weight: 1
slug: epoch
date: '2026-07-18T15:54:50.648646Z'
lastmod: '2026-07-18T16:38:06.837593Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 모델 학습 중 기계 학습 알고리즘이 훈련 데이터셋을 한 번 완전히 통과하는 과정입니다.
---
## Definition

기계 학습에서 에포크는 전체 훈련 데이터셋에 대한 단일 반복(iteration)을 의미합니다. 각 에포크 동안 모델은 모든 훈련 예제를 처리하고 역전파를 통해 가중치를 업데이트하며,

### Summary

모델 학습 중 기계 학습 알고리즘이 훈련 데이터셋을 한 번 완전히 통과하는 과정입니다.

## Key Concepts

- 훈련 반복
- 역전파
- 수렴
- 하이퍼파라미터 튜닝

## Use Cases

- 신경망 학습 루프 구성
- 주기별 검증 손실 모니터링
- 조기 종료 전략 구현

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Batch Size (배치 크기)](/en/terms/batch-size-배치-크기/)
- [Iteration (반복)](/en/terms/iteration-반복/)
- [Learning Rate (학습률)](/en/terms/learning-rate-학습률/)
- [Overfitting (과적합)](/en/terms/overfitting-과적합/)
