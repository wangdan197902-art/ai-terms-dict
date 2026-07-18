---
title: "셀프 어텐션(Self-Attention)"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /ko/terms/self_attention/
date: "2026-07-18T15:29:04.033569Z"
lastmod: "2026-07-18T16:38:06.784161Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "신경망이 입력 시퀀스의 서로 다른 부분들 간의 상대적 중요도를 가중치로 부여할 수 있도록 하는 메커니즘."
---

## Definition

셀프 어텐션은 거리의长短에 상관없이 시퀀스 내 모든 위치 간의 의존성을 동시에 포착할 수 있게 합니다. 모든 토큰 쌍 사이에 어텐션 점수를 계산함으로써, 모델은 입력 데이터의 전역적 맥락을 이해하고 중요한 정보에 집중할 수 있습니다.

### Summary

신경망이 입력 시퀀스의 서로 다른 부분들 간의 상대적 중요도를 가중치로 부여할 수 있도록 하는 메커니즘.

## Key Concepts

- 쿼리-키-값(Query-Key-Value)
- 어텐션 점수(Attention Scores)
- 맥락적 가중치(Contextual Weighting)
- 병렬 처리(Parallel Processing)

## Use Cases

- 기계 번역(Machine translation)
- 텍스트 요약(Text summarization)
- 비전 트랜스포머(Vision Transformers)를 통한 이미지 분류

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (트랜스포머 아키텍처)](/en/terms/transformer-트랜스포머-아키텍처/)
- [Multi-Head Attention (멀티 헤드 어텐션)](/en/terms/multi-head-attention-멀티-헤드-어텐션/)
- [Embeddings (임베딩)](/en/terms/embeddings-임베딩/)
- [Sequence Modeling (시퀀스 모델링)](/en/terms/sequence-modeling-시퀀스-모델링/)
