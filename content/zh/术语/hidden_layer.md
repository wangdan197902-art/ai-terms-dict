---
title: "隐藏层"
term_id: "hidden_layer"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture", "deep_learning"]
difficulty: 3
weight: 1
slug: "hidden_layer"
aliases:
  - /zh/terms/hidden_layer/
date: "2026-07-18T11:20:51.262168Z"
lastmod: "2026-07-18T11:44:45.513290Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "神经网络中输入层和输出层之间的中间层，负责处理特征。"
---

## Definition

隐藏层由神经元组成，这些神经元接收来自前一层层的输入，应用权重和偏置，并通过激活函数将转换后的数据传递到下一层。这些层使神经网络能够...

### Summary

神经网络中输入层和输出层之间的中间层，负责处理特征。

## Key Concepts

- 神经网络
- 特征提取
- 激活函数
- 深度学习

## Use Cases

- 图像识别系统
- 自然语言处理模型
- 预测性分析

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron (神经元)](/en/terms/neuron-神经元/)
- [backpropagation (反向传播)](/en/terms/backpropagation-反向传播/)
- [activation_function (激活函数)](/en/terms/activation_function-激活函数/)
- [deep_learning (深度学习)](/en/terms/deep_learning-深度学习/)
