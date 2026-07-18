---
title: "轮次 (Epoch)"
term_id: "epoch"
category: "training_techniques"
subcategory: ""
tags: ["training", "neural_networks", "basics"]
difficulty: 2
weight: 1
slug: "epoch"
aliases:
  - /zh/terms/epoch/
date: "2026-07-18T11:16:25.619836Z"
lastmod: "2026-07-18T11:44:45.495531Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "在模型训练期间，整个训练数据集通过机器学习算法的一次完整遍历。"
---

## Definition

在机器学习中，一个轮次代表对整个训练数据集的一次单遍迭代。在每个轮次中，模型处理所有训练样本，通过反向传播更新其权重，并评估损失函数。增加轮次数通常可以提高模型性能，但过多轮次可能导致过拟合。因此，监控验证集上的表现对于确定最佳轮次数至关重要。

### Summary

在模型训练期间，整个训练数据集通过机器学习算法的一次完整遍历。

## Key Concepts

- 训练迭代
- 反向传播
- 收敛
- 超参数调优

## Use Cases

- 配置神经网络训练循环
- 监控每个周期的验证损失
- 实施早停策略

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Batch Size (批次大小)](/en/terms/batch-size-批次大小/)
- [Iteration (迭代)](/en/terms/iteration-迭代/)
- [Learning Rate (学习率)](/en/terms/learning-rate-学习率/)
- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
