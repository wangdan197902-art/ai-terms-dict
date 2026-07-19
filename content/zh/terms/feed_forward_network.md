---
title: 前馈网络
term_id: feed_forward_network
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- fundamentals
difficulty: 2
weight: 1
slug: feed_forward_network
date: '2026-07-18T11:17:13.896137Z'
lastmod: '2026-07-18T11:44:45.499747Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一类人工神经网络，节点间的连接不形成循环，信息沿单一方向传播。
---
## Definition

前馈网络（FFN），也称为多层感知机（MLP），通过从输入层到输出层的神经元层顺序处理数据，没有反馈回路。每个神经元接收输入信号的加权总和，并通过激活函数进行处理，将结果传递给下一层。这种架构是许多深度学习模型的基础组件。

### Summary

一类人工神经网络，节点间的连接不形成循环，信息沿单一方向传播。

## Key Concepts

- 无循环
- 层级（输入、隐藏、输出）
- 激活函数
- 加权和

## Use Cases

- 简单回归任务
- 表格数据的分类问题
- 构建更深层次架构的基础模块

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron (多层感知机)](/en/terms/multi-layer-perceptron-多层感知机/)
- [Backpropagation (反向传播)](/en/terms/backpropagation-反向传播/)
- [Activation Function (激活函数)](/en/terms/activation-function-激活函数/)
- [Neural Network (神经网络)](/en/terms/neural-network-神经网络/)
