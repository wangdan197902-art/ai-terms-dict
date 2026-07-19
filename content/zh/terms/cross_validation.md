---
title: 交叉验证
term_id: cross_validation
category: training_techniques
subcategory: ''
tags:
- evaluation
- Machine Learning
- statistics
difficulty: 2
weight: 1
slug: cross_validation
date: '2026-07-18T11:12:12.555415Z'
lastmod: '2026-07-18T11:44:45.469954Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种重采样程序，通过将数据划分为子集进行训练和测试，用于在有限数据样本上评估机器学习模型。
---
## Definition

交叉验证是一种用于估计机器学习模型性能的统计方法。最常见的形式是k折交叉验证，即将数据分为k个相等的部分。模型在k-1个部分上进行训练，并在剩余的一个部分上进行测试，此过程重复k次，每次使用不同的部分作为测试集。

### Summary

一种重采样程序，通过将数据划分为子集进行训练和测试，用于在有限数据样本上评估机器学习模型。

## Key Concepts

- K折划分
- 模型泛化能力
- 过拟合检测
- 性能估计

## Use Cases

- 超参数调优
- 比较不同算法
- 在小数据集上验证模型稳定性

## Code Example

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X, y, cv=5)
```

## Related Terms

- [Train-Test Split (训练-测试集划分)](/en/terms/train-test-split-训练-测试集划分/)
- [Leave-One-Out (留一法)](/en/terms/leave-one-out-留一法/)
- [Bootstrap (自助法)](/en/terms/bootstrap-自助法/)
