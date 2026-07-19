---
title: "正则化"
term_id: "regularization"
category: "basic_concepts"
subcategory: ""
tags: ["ML Basics", "Optimization", "Statistics"]
difficulty: 2
weight: 1
slug: "regularization"
date: "2026-07-18T11:32:02.609270Z"
lastmod: "2026-07-18T11:44:45.550128Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一组在训练过程中使用的技术，通过对损失函数添加惩罚项或限制模型复杂度来防止过拟合。"
---
## Definition

正则化是机器学习中一个关键概念，旨在不显著增加训练误差的情况下减少泛化误差。它通过阻止模型学习过于复杂的模式来发挥作用。

### Summary

一组在训练过程中使用的技术，通过对损失函数添加惩罚项或限制模型复杂度来防止过拟合。

## Key Concepts

- 过拟合
- 偏差-方差权衡
- L1/L2 惩罚
- 丢弃法 (Dropout)

## Use Cases

- 深度神经网络训练
- 线性回归模型
- 防止小数据集上的记忆效应

## Code Example

```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)
```

## Related Terms

- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
- [Underfitting (欠拟合)](/en/terms/underfitting-欠拟合/)
- [Cross-validation (交叉验证)](/en/terms/cross-validation-交叉验证/)
- [Hyperparameter tuning (超参数调优)](/en/terms/hyperparameter-tuning-超参数调优/)
