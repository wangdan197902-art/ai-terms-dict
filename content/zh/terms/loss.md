---
title: 损失
term_id: loss
category: training_techniques
subcategory: ''
tags:
- training
- Optimization
difficulty: 3
weight: 1
slug: loss
date: '2026-07-18T10:52:50.832676Z'
lastmod: '2026-07-18T11:44:45.375955Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一个数值，用于量化模型预测值与实际目标值之间的误差。
---
## Definition

损失函数（也称为成本函数）衡量机器学习模型的预测结果与真实标签在训练期间的匹配程度。优化算法的目标是最小化这个损失值，从而提高模型的准确性。

### Summary

一个数值，用于量化模型预测值与实际目标值之间的误差。

## Key Concepts

- 成本函数
- 优化
- 梯度下降
- 误差指标

## Use Cases

- 训练图像分类器
- 优化回归模型
- 评估模型收敛性

## Code Example

```python
import torch.nn as nn
criterion = nn.CrossEntropyLoss()
loss = criterion(outputs, targets)
```

## Related Terms

- [Accuracy (准确率)](/en/terms/accuracy-准确率/)
- [Gradient Descent (梯度下降)](/en/terms/gradient-descent-梯度下降/)
- [Cross-Entropy (交叉熵)](/en/terms/cross-entropy-交叉熵/)
- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
