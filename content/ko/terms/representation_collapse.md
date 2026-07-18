---
title: "표현 붕괴"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /ko/terms/representation_collapse/
date: "2026-07-18T16:13:19.672944Z"
lastmod: "2026-07-18T16:38:06.904303Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델이 모든 입력에 대해 동일한 표현을 출력하여 판별력을 잃는 자기지도학습의 실패 모드."
---

## Definition

표현 붕괴는 특히 자기지도 대조 학습 프레임워크에서 신경망이 모든 입력 데이터 포인트를 동일한 고정 출력 벡터로 매핑하도록 학습할 때 발생합니다. 이는 모델이 입력 데이터의 차이를 구별하지 못하게 만드는 자명한 해(trivial solution)입니다.

### Summary

모델이 모든 입력에 대해 동일한 표현을 출력하여 판별력을 잃는 자기지도학습의 실패 모드.

## Key Concepts

- 자기지도학습
- 대조 손실
- 자명한 해
- 특징 학습

## Use Cases

- SimCLR 또는 MoCo 모델 디버깅
- 대조 손실 함수 개선
- 모델 수렴 분석

## Related Terms

- [Contrastive Learning (대조 학습)](/en/terms/contrastive-learning-대조-학습/)
- [Batch Normalization (배치 정규화)](/en/terms/batch-normalization-배치-정규화/)
- [Momentum Encoder (모멘텀 인코더)](/en/terms/momentum-encoder-모멘텀-인코더/)
- [Feature Extraction (특징 추출)](/en/terms/feature-extraction-특징-추출/)
