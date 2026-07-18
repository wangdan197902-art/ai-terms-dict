---
title: "学习率"
term_id: "learning_rate"
category: "training_techniques"
subcategory: ""
tags: ["training", "optimization", "hyperparameters"]
difficulty: 3
weight: 1
slug: "learning_rate"
aliases:
  - /zh/terms/learning_rate/
date: "2026-07-18T11:00:35.785291Z"
lastmod: "2026-07-18T11:44:45.402158Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "控制模型优化过程中步长的超参数，旨在最小化损失函数。"
---

## Definition

学习率决定了在每次训练迭代中，模型权重相对于计算出的梯度更新了多少。如果学习率过高，可能导致模型在优化过程中越过最优解；如果过低，则可能导致训练收敛缓慢。

### Summary

控制模型优化过程中步长的超参数，旨在最小化损失函数。

## Key Concepts

- 梯度下降
- 超参数调优
- 收敛
- 优化器

## Use Cases

- 神经网络训练
- 深度学习模型优化
- 强化学习策略更新

## Code Example

```python
import torch.optim as optim
model = MyModel()
optimizer = optim.SGD(model.parameters(), lr=0.01)
```

## Related Terms

- [gradient_descent (梯度下降)](/en/terms/gradient_descent-梯度下降/)
- [optimizer (优化器)](/en/terms/optimizer-优化器/)
- [hyperparameter (超参数)](/en/terms/hyperparameter-超参数/)
- [convergence (收敛)](/en/terms/convergence-收敛/)
