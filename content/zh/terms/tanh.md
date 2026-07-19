---
title: 双曲正切 (Tanh)
term_id: tanh
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- mathematics
difficulty: 2
weight: 1
slug: tanh
date: '2026-07-18T11:35:43.087239Z'
lastmod: '2026-07-18T11:44:45.561267Z'
draft: false
source: agnes_llm
status: published
language: zh
description: Tanh（双曲正切）是一种激活函数，将输入值映射到-1到1的范围之间。
---
## Definition

双曲正切（Tanh）函数是一种非线性激活函数，常用于神经网络。它将输入值压缩到(-1, 1)区间内，提供零中心的输出，这有助于加速收敛。

### Summary

Tanh（双曲正切）是一种激活函数，将输入值映射到-1到1的范围之间。

## Key Concepts

- 激活函数
- 非线性
- 零中心输出
- 反向传播

## Use Cases

- 循环神经网络
- LSTM单元门控
- 多层感知机中的隐藏层

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (Sigmoid函数)](/en/terms/sigmoid-sigmoid函数/)
- [relu (ReLU激活函数)](/en/terms/relu-relu激活函数/)
- [neural_networks (神经网络)](/en/terms/neural_networks-神经网络/)
