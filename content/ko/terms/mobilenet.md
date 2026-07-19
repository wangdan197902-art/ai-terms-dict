---
title: "MobileNet"
term_id: "mobilenet"
category: "basic_concepts"
subcategory: ""
tags: ["CNN", "Optimization", "Mobile AI"]
difficulty: 2
weight: 1
slug: "mobilenet"
date: "2026-07-18T16:05:51.405483Z"
lastmod: "2026-07-18T16:38:06.885696Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모바일 및 임베디드 비전 애플리케이션을 위해 설계된 경량 심층 신경망 패밀리를 의미합니다."
---
## Definition

MobileNet은 표준 합성곱 연산에 비해 계산 비용과 모델 크기를 획기적으로 줄이기 위해 깊이별 분리 가능 합성곱(Depthwise Separable Convolutions)을 활용합니다. 이 아키텍처는 모바일 장치와 같은 리소스가 제한된 환경에서도 효율적인 특징 추출을 가능하게 합니다.

### Summary

모바일 및 임베디드 비전 애플리케이션을 위해 설계된 경량 심층 신경망 패밀리를 의미합니다.

## Key Concepts

- 깊이별 분리 가능 합성곱
- 모델 효율성
- 엣지 컴퓨팅
- 전이 학습

## Use Cases

- 스마트폰에서의 실시간 객체 감지
- IoT 기기에서의 이미지 분류
- 모바일 앱 내 얼굴 인식

## Code Example

```python
from tensorflow.keras.applications import MobileNetV2
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
```

## Related Terms

- [ShuffleNet (셔플넷)](/en/terms/shufflenet-셔플넷/)
- [SqueezeNet (스크리즈넷)](/en/terms/squeezenet-스크리즈넷/)
- [EfficientNet (에피션트넷)](/en/terms/efficientnet-에피션트넷/)
- [Convolutional Neural Network (합성곱 신경망)](/en/terms/convolutional-neural-network-합성곱-신경망/)
