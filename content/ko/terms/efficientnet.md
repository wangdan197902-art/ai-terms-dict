---
title: EfficientNet
term_id: efficientnet
category: basic_concepts
subcategory: ''
tags:
- architecture
- Computer Vision
- Optimization
difficulty: 4
weight: 1
slug: efficientnet
date: '2026-07-18T15:54:09.943618Z'
lastmod: '2026-07-18T16:38:06.835951Z'
draft: false
source: agnes_llm
status: published
language: ko
description: EfficientNet은 깊이, 너비, 해상도를 균일하게 스케일링하여 더 적은 매개변수로 더 높은 정확도를 달성하는 합성곱
  신경망(CNN) 아키텍처 계열입니다.
---
## Definition

구글(Google)에서 개발된 EfficientNet은 네트워크의 깊이(depth), 너비(width), 입력 이미지 해상도(resolution) 사이의 균형을 맞추기 위해 복합 스케일링(compound scaling) 방법을 사용합니다. 이 접근 방식은 모델이 최첨단 정확도를 달성하면서도 계산 자원과 매개변수 수를 효율적으로 관리할 수 있게 해줍니다. MobileNetV2 블록과 SE(Squeeze-and-Excitation) 어텐션 메커니즘을 활용하여 성능과 효율성을 극대화합니다.

### Summary

EfficientNet은 깊이, 너비, 해상도를 균일하게 스케일링하여 더 적은 매개변수로 더 높은 정확도를 달성하는 합성곱 신경망(CNN) 아키텍처 계열입니다.

## Key Concepts

- 복합 스케일링(Compound scaling)
- MobileNetV2 블록
- SE 어텐션(SE attention)
- 매개변수 효율성(Parameter efficiency)

## Use Cases

- 모바일 기기에서의 이미지 분류
- 자원 제약 환경에서의 객체 감지
- 대규모 시각 데이터셋을 위한 특징 추출

## Related Terms

- [ResNet (잔여 신경망)](/en/terms/resnet-잔여-신경망/)
- [MobileNet (모바일 친화적 CNN)](/en/terms/mobilenet-모바일-친화적-cnn/)
- [Convolutional Neural Network (합성곱 신경망)](/en/terms/convolutional-neural-network-합성곱-신경망/)
- [Neural Architecture Search (신경망 아키텍처 탐색)](/en/terms/neural-architecture-search-신경망-아키텍처-탐색/)
