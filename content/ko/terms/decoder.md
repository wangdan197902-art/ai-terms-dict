---
title: "디코더"
term_id: "decoder"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "nlp", "architecture"]
difficulty: 4
weight: 1
slug: "decoder"
aliases:
  - /ko/terms/decoder/
date: "2026-07-18T15:34:04.841847Z"
lastmod: "2026-07-18T16:38:06.793884Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "인코딩된 잠재 표현(latent representations)으로부터 출력 시퀀스를 생성하는 역할을 하는 신경망 구성 요소입니다."
---

## Definition

시퀀스 투 시퀀스(sequence-to-sequence) 모델에서 디코더는 인코더가 생성한 컨텍스트 벡터를 입력받아 대상 출력을 단계별로 생성합니다. 이는 관련 있는 부분에 집중하기 위해 어텐션 메커니즘(attention mechanisms)을 사용합니다.

### Summary

인코딩된 잠재 표현(latent representations)으로부터 출력 시퀀스를 생성하는 역할을 하는 신경망 구성 요소입니다.

## Key Concepts

- 시퀀스 생성
- 어텐션 메커니즘
- 잠재 공간
- 자기회귀 예측

## Use Cases

- 기계 번역(영어에서 프랑스어로)
- 텍스트 요약
- 이미지 캡셔닝

## Related Terms

- [Encoder (인코더)](/en/terms/encoder-인코더/)
- [Transformer (트랜스포머)](/en/terms/transformer-트랜스포머/)
- [RNN (순환 신경망)](/en/terms/rnn-순환-신경망/)
- [Sequence-to-Sequence (시퀀스 투 시퀀스)](/en/terms/sequence-to-sequence-시퀀스-투-시퀀스/)
