---
title: ReLU
term_id: relu
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Activation Functions
- Deep Learning
difficulty: 3
weight: 1
slug: relu
date: '2026-07-18T11:01:41.442930Z'
lastmod: '2026-07-18T11:44:45.404817Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 修正线性单元（ReLU）是一种激活函数，如果输入为正，则直接输出该输入；否则输出零。
---
## Definition

由于其计算效率高且能缓解梯度消失问题，ReLU 被广泛应用于深度学习的神经网络中。其数学定义为 f(x) = max(0, x)，它引入了非线性特性（原文截断，意为 introduces non-linearity）。

### Summary

修正线性单元（ReLU）是一种激活函数，如果输入为正，则直接输出该输入；否则输出零。

## Key Concepts

- 非线性
- 激活函数
- 梯度消失
- 分段线性

## Use Cases

- 卷积神经网络中的隐藏层
- 深度前馈网络
- 图像识别模型

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (S型函数)](/en/terms/sigmoid-s型函数/)
- [Tanh (双曲正切函数)](/en/terms/tanh-双曲正切函数/)
- [Leaky ReLU (泄漏修正线性单元)](/en/terms/leaky-relu-泄漏修正线性单元/)
- [Neural Network (神经网络)](/en/terms/neural-network-神经网络/)
