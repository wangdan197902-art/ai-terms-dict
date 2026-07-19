---
title: TensorFlow Hub
term_id: tensorflow_hub
category: basic_concepts
subcategory: ''
tags:
- tensorflow
- libraries
- Transfer Learning
difficulty: 3
weight: 1
slug: tensorflow_hub
date: '2026-07-18T16:18:04.373223Z'
lastmod: '2026-07-18T16:38:06.913751Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 재사용 가능한 머신러닝 모듈을 위한 저장소로, 사전 훈련된 모델을 통해 전이 학습을 가능하게 합니다.
---
## Definition

TensorFlow Hub는 머신러닝 구성 요소를 게시하고 재사용하기 위한 플랫폼입니다. 이미지 분류, 텍스트 임베딩 등 다양한 작업에 대한 사전 훈련된 모델에 개발자가 접근할 수 있도록 지원합니다.

### Summary

재사용 가능한 머신러닝 모듈을 위한 저장소로, 사전 훈련된 모델을 통해 전이 학습을 가능하게 합니다.

## Key Concepts

- 전이 학습
- 모듈 재사용
- 사전 훈련된 모델
- 효율성

## Use Cases

- 모델 프로토타이핑 가속화
- 훈련 비용 절감
- 최신 NLP/CV 구현

## Code Example

```python
import tensorflow_hub as hub
module = hub.load('https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5')
```

## Related Terms

- [Hugging Face (인기 있는 오픈 소스 머신러닝 커뮤니티 및 라이브러리)](/en/terms/hugging-face-인기-있는-오픈-소스-머신러닝-커뮤니티-및-라이브러리/)
- [Keras Applications (Keras에서 제공하는 사전 훈련된 모델 모음)](/en/terms/keras-applications-keras에서-제공하는-사전-훈련된-모델-모음/)
- [Transfer Learning (전이 학습)](/en/terms/transfer-learning-전이-학습/)
- [Model Zoo (모델 저장소)](/en/terms/model-zoo-모델-저장소/)
