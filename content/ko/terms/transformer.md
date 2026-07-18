---
title: "트랜스포머"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /ko/terms/transformer/
date: "2026-07-18T15:30:34.141649Z"
lastmod: "2026-07-18T16:38:06.786759Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "순차적 데이터가 순차적으로가 아니라 병렬로 처리되도록 하는 자기 주의 메커니즘(self-attention) 기반의 딥러닝 아키텍처입니다."
---

## Definition

'Attention Is All You Need' 논문에서 소개된 트랜스포머 아키텍처는 자연어 처리 및 그 이상의 분야를 혁신했습니다. 이는 다중 헤드 자기 주의(multi-head self-attention)를 사용하여 각 요소의 중요도에 가중치를 부여합니다.

### Summary

순차적 데이터가 순차적으로가 아니라 병렬로 처리되도록 하는 자기 주의 메커니즘(self-attention) 기반의 딥러닝 아키텍처입니다.

## Key Concepts

- 자기 주의(Self-Attention)
- 다중 헤드 주의(Multi-Head Attention)
- 위치 인코딩(Positional Encoding)
- 인코더-디코더 구조

## Use Cases

- 기계 번역
- 텍스트 생성
- 이미지 인식(ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (주의 메커니즘)](/en/terms/attention_mechanism-주의-메커니즘/)
- [bert (비트)](/en/terms/bert-비트/)
- [gpt (지피티)](/en/terms/gpt-지피티/)
- [self_attention (자기 주의)](/en/terms/self_attention-자기-주의/)
