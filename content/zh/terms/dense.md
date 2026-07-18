---
title: "稠密层"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /zh/terms/dense/
date: "2026-07-18T11:14:15.624765Z"
lastmod: "2026-07-18T11:44:45.486703Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种层或张量，其中每个元素都与前一层或维度的每个元素相连。"
---

## Definition

在神经网络中，“稠密”指的是全连接层，其中每个神经元都接收来自前一层所有神经元的输入。这与卷积层或稀疏连接中常见的稀疏连接形成对比。

### Summary

一种层或张量，其中每个元素都与前一层或维度的每个元素相连。

## Key Concepts

- 全连接
- 权重矩阵
- 激活函数
- 特征整合

## Use Cases

- 多层感知机（MLP）中的最终分类层
- 混合模型中的特征融合
- 简单回归任务

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (前馈神经网络)](/en/terms/feedforward-neural-network-前馈神经网络/)
- [Backpropagation (反向传播)](/en/terms/backpropagation-反向传播/)
- [ReLU (整流线性单元)](/en/terms/relu-整流线性单元/)
- [Bias Term (偏置项)](/en/terms/bias-term-偏置项/)
