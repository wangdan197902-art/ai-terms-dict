---
title: "损失函数"
term_id: "loss_function"
category: "basic_concepts"
subcategory: ""
tags: ["training", "mathematics", "evaluation"]
difficulty: 3
weight: 1
slug: "loss_function"
date: "2026-07-18T11:00:35.785310Z"
lastmod: "2026-07-18T11:44:45.402477Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "在训练期间量化预测值与实际目标值之间差异的数学函数。"
---
## Definition

损失函数也被称为成本函数或误差函数，它提供一个标量值，指示模型的执行表现。在训练过程中，优化算法利用该值来计算梯度，从而更新模型参数以最小化误差。

### Summary

在训练期间量化预测值与实际目标值之间差异的数学函数。

## Key Concepts

- 反向传播
- 梯度计算
- 优化
- 误差指标

## Use Cases

- 训练监督学习模型
- 评估模型性能
- 超参数调优

## Code Example

```python
import torch.nn as nn
criterion = nn.CrossEntropyLoss()
```

## Related Terms

- [backpropagation (反向传播)](/en/terms/backpropagation-反向传播/)
- [gradient_descent (梯度下降)](/en/terms/gradient_descent-梯度下降/)
- [cross_entropy (交叉熵)](/en/terms/cross_entropy-交叉熵/)
- [mse (均方误差)](/en/terms/mse-均方误差/)
