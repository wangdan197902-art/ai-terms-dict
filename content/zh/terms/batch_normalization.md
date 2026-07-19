---
title: 批归一化
term_id: batch_normalization
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- Optimization
- Neural Networks
difficulty: 3
weight: 1
slug: batch_normalization
date: '2026-07-18T11:08:27.713000Z'
lastmod: '2026-07-18T11:44:45.449458Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 批归一化是一种技术，通过对小批量数据上的层输入进行归一化，以稳定并加速神经网络的训练。
---
## Definition

该方法在训练期间调整并缩放激活值，使其在每个小批量中具有零均值和单位方差。它减少了内部协变量偏移，允许使用更高的学习率和更快的收敛速度。

### Summary

批归一化是一种技术，通过对小批量数据上的层输入进行归一化，以稳定并加速神经网络的训练。

## Key Concepts

- 内部协变量偏移
- 小批量统计量
- 梯度稳定
- 正则化效应

## Use Cases

- 深度神经网络
- 卷积神经网络
- 训练优化

## Code Example

```python
import torch.nn as nn
layer = nn.Sequential(
    nn.Linear(10, 20),
    nn.BatchNorm1d(20),
    nn.ReLU()
)
```

## Related Terms

- [Layer Normalization (层归一化)](/en/terms/layer-normalization-层归一化/)
- [Gradient Descent (梯度下降)](/en/terms/gradient-descent-梯度下降/)
- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
