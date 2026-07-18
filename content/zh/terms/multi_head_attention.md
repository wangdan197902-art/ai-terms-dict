---
title: "多头注意力"
term_id: "multi_head_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformer", "nlp", "deep_learning"]
difficulty: 4
weight: 1
slug: "multi_head_attention"
aliases:
  - /zh/terms/multi_head_attention/
date: "2026-07-18T10:53:14.834734Z"
lastmod: "2026-07-18T11:44:45.378267Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "Transformer模型中的一种机制，允许模型同时关注来自不同表示子空间的信息。"
---

## Definition

多头注意力通过并行运行多次标准注意力机制（使用不同的学习到的线性投影）来扩展标准注意力机制。这使得模型能够联合关注来自不同位置的不同表示子空间的信息。

### Summary

Transformer模型中的一种机制，允许模型同时关注来自不同表示子空间的信息。

## Key Concepts

- 自注意力
- 线性投影
- 拼接

## Use Cases

- 自然语言处理 (NLP)
- 机器翻译
- 使用Vision Transformer进行图像分类

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

- [Scaled Dot-Product Attention (缩放点积注意力)](/en/terms/scaled-dot-product-attention-缩放点积注意力/)
- [Transformer (变换器)](/en/terms/transformer-变换器/)
- [Embedding (嵌入)](/en/terms/embedding-嵌入/)
