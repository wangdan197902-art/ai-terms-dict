---
title: "Transformer"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /zh/terms/transformer/
date: "2026-07-18T10:55:40.663789Z"
lastmod: "2026-07-18T11:44:45.387433Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种基于自注意力机制的深度学习架构，能够并行而非顺序地处理序列数据。"
---

## Definition

Transformer架构在《Attention Is All You Need》论文中被提出，彻底革新了自然语言处理及更多领域。它使用多头自注意力机制来权衡输入序列中不同部分的重要性。

### Summary

一种基于自注意力机制的深度学习架构，能够并行而非顺序地处理序列数据。

## Key Concepts

- 自注意力
- 多头注意力
- 位置编码
- 编码器-解码器结构

## Use Cases

- 机器翻译
- 文本生成
- 图像识别（ViT）

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (注意力机制)](/en/terms/attention_mechanism-注意力机制/)
- [bert (BERT模型)](/en/terms/bert-bert模型/)
- [gpt (GPT模型)](/en/terms/gpt-gpt模型/)
- [self_attention (自注意力)](/en/terms/self_attention-自注意力/)
