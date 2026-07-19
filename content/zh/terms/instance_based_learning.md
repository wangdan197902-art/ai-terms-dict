---
title: 基于实例的学习
term_id: instance_based_learning
category: training_techniques
subcategory: ''
tags:
- algorithm
- Lazy Learning
- Classification
difficulty: 2
weight: 1
slug: instance_based_learning
date: '2026-07-18T11:22:25.518478Z'
lastmod: '2026-07-18T11:44:45.518222Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种惰性学习方法，通过将新输入与存储的训练实例进行比较来进行预测。
---
## Definition

也称为基于记忆的学习，该技术不在训练期间构建泛化模型。相反，它存储整个训练数据集。当需要预测时，它会找到最相似的。

### Summary

一种惰性学习方法，通过将新输入与存储的训练实例进行比较来进行预测。

## Key Concepts

- 惰性学习
- 相似度度量
- K近邻 (K-Nearest Neighbors)
- 基于记忆

## Use Cases

- 推荐系统
- 模式识别
- 中小型数据集

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```

## Related Terms

- [KNN (K-Nearest Neighbors)](/en/terms/knn-k-nearest-neighbors/)
- [相似度搜索 (Similarity search)](/en/terms/相似度搜索-similarity-search/)
- [惰性学习 (Lazy learning)](/en/terms/惰性学习-lazy-learning/)
- [核方法 (Kernel methods)](/en/terms/核方法-kernel-methods/)
