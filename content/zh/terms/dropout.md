---
title: "Dropout"
term_id: "dropout"
category: "basic_concepts"
subcategory: ""
tags: ["Deep Learning", "Regularization", "Model Training"]
difficulty: 3
weight: 1
slug: "dropout"
aliases:
  - /zh/terms/dropout/
date: "2026-07-18T10:59:51.920733Z"
lastmod: "2026-07-18T11:44:45.399256Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "Dropout 是一种正则化技术，通过在训练过程中随机忽略神经元来防止过拟合。"
---

## Definition

在神经网络中，Dropout 通过在每次训练步骤中临时移除随机子集的神经元来防止过拟合。这迫使网络学习在联合使用时有用的鲁棒特征。

### Summary

Dropout 是一种正则化技术，通过在训练过程中随机忽略神经元来防止过拟合。

## Key Concepts

- 正则化
- 防止过拟合
- 神经网络
- 随机抑制

## Use Cases

- 训练深层前馈神经网络
- 提高大型语言模型的泛化能力
- 减少对特定神经元路径的计算依赖

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(100, 50),
    nn.Dropout(0.5),
    nn.ReLU(),
    nn.Linear(50, 10)
)
```

## Related Terms

- [L2 Regularization (L2正则化，权重衰减)](/en/terms/l2-regularization-l2正则化-权重衰减/)
- [Batch Normalization (批归一化)](/en/terms/batch-normalization-批归一化/)
- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
- [Generalization (泛化)](/en/terms/generalization-泛化/)
