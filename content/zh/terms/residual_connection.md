---
title: "残差连接"
term_id: "residual_connection"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "optimization", "deep_learning"]
difficulty: 3
weight: 1
slug: "residual_connection"
aliases:
  - /zh/terms/residual_connection/
date: "2026-07-18T11:01:52.849059Z"
lastmod: "2026-07-18T11:44:45.405716Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种将输入直接加到层输出上的机制，以促进深层网络中的梯度流动。"
---

## Definition

残差连接（也称为跳跃连接）通过将输入直接添加到后续层的输出来允许梯度在网络中流动。这种架构解决了深层网络中的梯度消失问题。

### Summary

一种将输入直接加到层输出上的机制，以促进深层网络中的梯度流动。

## Key Concepts

- 跳跃连接
- 梯度消失问题
- 深度残差学习
- 梯度流

## Use Cases

- 训练深层卷积神经网络
- Transformer 架构
- 图像分类模型

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (跳跃连接)](/en/terms/skip_connection-跳跃连接/)
- [vanishing_gradient (梯度消失)](/en/terms/vanishing_gradient-梯度消失/)
- [deep_learning (深度学习)](/en/terms/deep_learning-深度学习/)
- [resnet (残差网络)](/en/terms/resnet-残差网络/)
