---
title: 位置编码
term_id: positional_encoding
category: basic_concepts
subcategory: ''
tags:
- transformers
- NLP
- architecture
difficulty: 3
weight: 1
slug: positional_encoding
date: '2026-07-18T11:01:29.499728Z'
lastmod: '2026-07-18T11:44:45.403772Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种将序列中令牌的相对或绝对位置信息注入 Transformer 模型的技术。
---
## Definition

由于 Transformer 并行处理所有令牌，而不是像循环神经网络（RNN）那样按顺序处理，因此它缺乏对令牌顺序的固有认知。位置编码通过向输入嵌入添加特定的向量来保留这种顺序信息。

### Summary

一种将序列中令牌的相对或绝对位置信息注入 Transformer 模型的技术。

## Key Concepts

- 序列顺序
- 自注意力机制
- 正弦函数
- 令牌嵌入

## Use Cases

- 机器翻译
- 文本摘要
- 语言建模

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

- [Transformer 架构](/en/terms/transformer-架构/)
- [嵌入 (Embedding)](/en/terms/嵌入-embedding/)
- [注意力机制 (Attention Mechanism)](/en/terms/注意力机制-attention-mechanism/)
- [旋转位置编码 (RoPE)](/en/terms/旋转位置编码-rope/)
