---
title: "위치 인코딩"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /ko/terms/positional_encoding/
date: "2026-07-18T15:35:37.491242Z"
lastmod: "2026-07-18T16:38:06.798490Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "트랜스포머 모델에 시퀀스 내 토큰의 상대적 또는 절대적 위치에 대한 정보를 주입하는 기법."
---

## Definition

트랜스포머는 RNN과 달리 시퀀스가 아닌 병렬로 모든 토큰을 처리하므로 토큰 순서에 대한 고유한 지식이 부족합니다. 위치 인코딩은 입력 임베딩에 특정 벡터를 추가하여 토큰의 순서 정보를 보존합니다.

### Summary

트랜스포머 모델에 시퀀스 내 토큰의 상대적 또는 절대적 위치에 대한 정보를 주입하는 기법.

## Key Concepts

- 시퀀스 순서
- 자기 주의 메커니즘(Self-Attention)
- 사인-코사인 함수(Sinusoidal Functions)
- 토큰 임베딩

## Use Cases

- 기계 번역
- 텍스트 요약
- 언어 모델링

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Transformer Architecture (트랜스포머 아키텍처)](/en/terms/transformer-architecture-트랜스포머-아키텍처/)
- [Embedding (임베딩)](/en/terms/embedding-임베딩/)
- [Attention Mechanism (주의 메커니즘)](/en/terms/attention-mechanism-주의-메커니즘/)
- [RoPE (회전 위치 인코딩)](/en/terms/rope-회전-위치-인코딩/)
