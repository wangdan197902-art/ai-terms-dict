---
title: "S型函数"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
aliases:
  - /zh/terms/sigmoid/
date: "2026-07-18T11:33:18.814272Z"
lastmod: "2026-07-18T11:44:45.553793Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种数学函数，将任何实数值映射到零和一之间的值，形成S形曲线。"
---

## Definition

S型函数定义为 σ(z) = 1 / (1 + e^-z)，广泛用于机器学习中对概率进行建模。它将输入值压缩到 (0, 1) 范围内，使其适用于二分类问题的输出层。

### Summary

一种数学函数，将任何实数值映射到零和一之间的值，形成S形曲线。

## Key Concepts

- 逻辑函数
- 概率映射
- 梯度消失
- 非线性

## Use Cases

- 二分类输出
- 逻辑回归
- 浅层神经网络中的激活函数

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Logistic Regression (逻辑回归)](/en/terms/logistic-regression-逻辑回归/)
- [Activation Function (激活函数)](/en/terms/activation-function-激活函数/)
