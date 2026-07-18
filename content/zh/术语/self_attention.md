---
title: "自注意力机制"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /zh/terms/self_attention/
date: "2026-07-18T10:54:51.109424Z"
lastmod: "2026-07-18T11:44:45.384788Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种允许神经网络根据彼此之间的相对重要性来权衡输入序列不同部分的机制。"
---

## Definition

自注意力使模型能够同时捕捉序列中所有位置之间的依赖关系，无论距离远近。通过计算每对标记之间的注意力分数，它使得……

### Summary

一种允许神经网络根据彼此之间的相对重要性来权衡输入序列不同部分的机制。

## Key Concepts

- 查询-键-值 (Query-Key-Value)
- 注意力分数
- 上下文加权
- 并行处理

## Use Cases

- 机器翻译
- 文本摘要
- 通过视觉Transformer进行图像分类

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (变换器)](/en/terms/transformer-变换器/)
- [Multi-Head Attention (多头注意力)](/en/terms/multi-head-attention-多头注意力/)
- [Embeddings (嵌入向量)](/en/terms/embeddings-嵌入向量/)
- [Sequence Modeling (序列建模)](/en/terms/sequence-modeling-序列建模/)
