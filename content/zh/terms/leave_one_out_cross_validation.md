---
title: 留一法交叉验证
term_id: leave_one_out_cross_validation
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- evaluation
- statistics
difficulty: 3
weight: 1
slug: leave_one_out_cross_validation
date: '2026-07-18T11:24:07.939906Z'
lastmod: '2026-07-18T11:44:45.524317Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种严格的重采样技术，模型在除一个样本外的所有样本上进行训练，并在该单个保留样本上进行测试，对每个数据点重复此过程。
---
## Definition

留一法交叉验证（LOOCV）是k折交叉验证的一种特殊情况，其中k等于数据集中的样本数量。它提供了对模型性能的近乎无偏的估计，因为每次训练都使用了尽可能多的数据，从而最大限度地减少了偏差。然而，这种方法计算成本较高，因为需要为每个样本重新训练模型。

### Summary

一种严格的重采样技术，模型在除一个样本外的所有样本上进行训练，并在该单个保留样本上进行测试，对每个数据点重复此过程。

## Key Concepts

- 重采样
- 模型评估
- 偏差-方差权衡
- 计算成本

## Use Cases

- 在小规模医疗数据集上评估模型
- 数据稀缺时的超参数调优
- 严格比较算法性能

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (k折交叉验证)](/en/terms/k-fold-cross-validation-k折交叉验证/)
- [train_test_split (训练集-测试集划分)](/en/terms/train_test_split-训练集-测试集划分/)
- [bootstrap (自助法)](/en/terms/bootstrap-自助法/)
- [cross_validation_score (交叉验证得分)](/en/terms/cross_validation_score-交叉验证得分/)
