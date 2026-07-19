---
title: 잔차 연결
term_id: residual_connection
category: basic_concepts
subcategory: ''
tags:
- architecture
- Optimization
- Deep Learning
difficulty: 3
weight: 1
slug: residual_connection
date: '2026-07-18T15:36:05.902176Z'
lastmod: '2026-07-18T16:38:06.799845Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 깊은 네트워크에서 기울기 흐름을 원활하게 하기 위해 레이어의 출력에 입력을 직접 더하는 메커니즘입니다.
---
## Definition

스킵 연결(skip connections)이라고도 불리는 잔차 연결은 입력을 후속 레이어의 출력에 직접 추가하여 네트워크 전체에 걸쳐 기울기가 흐르도록 합니다. 이 아키텍처는 매우 깊은 네트워크에서 발생하는 기울기 소실 문제를 해결하고 학습을 용이하게 합니다.

### Summary

깊은 네트워크에서 기울기 흐름을 원활하게 하기 위해 레이어의 출력에 입력을 직접 더하는 메커니즘입니다.

## Key Concepts

- 스킵 연결(Skip Connections)
- 기울기 소실 문제
- 심층 잔차 학습(Deep Residual Learning)
- 기울기 흐름(Gradient Flow)

## Use Cases

- 심층 합성곱 신경망(CNN) 훈련
- 트랜스포머 아키텍처
- 이미지 분류 모델

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (스킵 연결: 중간 레이어 간 직접 연결)](/en/terms/skip_connection-스킵-연결-중간-레이어-간-직접-연결/)
- [vanishing_gradient (기울기 소실: 깊은 네트워크 학습 시 발생하는 문제)](/en/terms/vanishing_gradient-기울기-소실-깊은-네트워크-학습-시-발생하는-문제/)
- [deep_learning (딥러닝: 다층 신경망을 활용한 머신러닝)](/en/terms/deep_learning-딥러닝-다층-신경망을-활용한-머신러닝/)
- [resnet (ResNet: 잔차 연결을 도입한 대표적인 심층 신경망 아키텍처)](/en/terms/resnet-resnet-잔차-연결을-도입한-대표적인-심층-신경망-아키텍처/)
