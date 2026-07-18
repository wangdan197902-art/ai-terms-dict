---
title: "멀티 헤드 어텐션(Multi-Head Attention)"
term_id: "multi_head_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformer", "nlp", "deep_learning"]
difficulty: 4
weight: 1
slug: "multi_head_attention"
aliases:
  - /ko/terms/multi_head_attention/
date: "2026-07-18T15:27:21.460584Z"
lastmod: "2026-07-18T16:38:06.779476Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델이 서로 다른 표현 부분 공간(subspace)의 정보를 동시에 주시(attend)할 수 있게 하는 트랜스포머 모델의 메커니즘."
---

## Definition

멀티 헤드 어텐션은 표준 어텐션 메커니즘을 서로 다른 학습된 선형 투영(linear projections)을 사용하여 병렬로 여러 번 실행함으로써 이를 확장합니다. 이를 통해 모델은 다양한 정보에 대해 공동으로 주시할 수 있게 됩니다.

### Summary

모델이 서로 다른 표현 부분 공간(subspace)의 정보를 동시에 주시(attend)할 수 있게 하는 트랜스포머 모델의 메커니즘.

## Key Concepts

- 셀프 어텐션(Self-Attention)
- 선형 투영(Linear Projections)
- 결합(Concatenation)

## Use Cases

- 자연어 처리(NLP)
- 기계 번역
- 비전 트랜스포머(Vision Transformers)를 이용한 이미지 분류

## Code Example

```python
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        # Simplified forward pass logic
        pass
```

## Related Terms

- [Scaled Dot-Product Attention (스케일드 닷 프로덕트 어텐션)](/en/terms/scaled-dot-product-attention-스케일드-닷-프로덕트-어텐션/)
- [Transformer (트랜스포머)](/en/terms/transformer-트랜스포머/)
- [Embedding (임베딩)](/en/terms/embedding-임베딩/)
