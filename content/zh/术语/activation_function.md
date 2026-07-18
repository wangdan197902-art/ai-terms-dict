---
title: "激活函数"
term_id: "activation_function"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "mathematics", "deep_learning", "basics"]
difficulty: 3
weight: 1
slug: "activation_function"
aliases:
  - /zh/terms/activation_function/
date: "2026-07-18T10:59:15.017978Z"
lastmod: "2026-07-18T11:44:45.396677Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "根据输入信号确定神经网络节点输出的数学方程。"
---

## Definition

激活函数为神经网络引入非线性，使其能够学习数据中的复杂模式和关系。如果没有这些函数，多层网络的行为将退化为线性变换，无法处理复杂任务。

### Summary

根据输入信号确定神经网络节点输出的数学方程。

## Key Concepts

- 非线性
- 梯度下降
- 神经元激活
- 反向传播

## Use Cases

- 使深度神经网络能够进行图像分类
- 促进自然语言处理任务
- 提高生成模型训练时的收敛速度

## Code Example

```python
import torch.nn as nn
relu = nn.ReLU()
output = relu(input_tensor)
```

## Related Terms

- [ReLU (修正线性单元)](/en/terms/relu-修正线性单元/)
- [Sigmoid (S型函数)](/en/terms/sigmoid-s型函数/)
- [Tanh (双曲正切函数)](/en/terms/tanh-双曲正切函数/)
- [Softmax (软最大函数)](/en/terms/softmax-软最大函数/)
