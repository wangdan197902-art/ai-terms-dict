---
title: "Adam"
term_id: "adam"
category: "basic_concepts"
subcategory: ""
tags: ["Optimization", "Deep Learning", "Algorithms"]
difficulty: 3
weight: 1
slug: "adam"
aliases:
  - /zh/terms/adam/
date: "2026-07-18T10:49:06.484463Z"
lastmod: "2026-07-18T11:44:45.361358Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种为每个参数计算自适应学习率的优化算法。"
---

## Definition

Adam（自适应矩估计）是一种流行的基于一阶梯度的优化算法，用于训练深度神经网络。它结合了两种其他随机梯度下降扩展的优势。

### Summary

一种为每个参数计算自适应学习率的优化算法。

## Key Concepts

- 梯度下降
- 学习率
- 动量
- 方差估计

## Use Cases

- 深度学习训练
- 计算机视觉模型
- 自然语言处理

## Code Example

```python
import torch.optim as optim
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

## Related Terms

- [SGD (随机梯度下降)](/en/terms/sgd-随机梯度下降/)
- [RMSProp (均方根传播)](/en/terms/rmsprop-均方根传播/)
- [Optimizer (优化器)](/en/terms/optimizer-优化器/)
- [Backpropagation (反向传播)](/en/terms/backpropagation-反向传播/)
