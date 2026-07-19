---
title: 惰性学习
term_id: lazy_learning
category: training_techniques
subcategory: ''
tags:
- algorithms
- Training Methods
- Machine Learning
difficulty: 2
weight: 1
slug: lazy_learning
date: '2026-07-18T11:23:41.252135Z'
lastmod: '2026-07-18T11:44:45.523325Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种学习方法，将泛化推迟到分类时才进行，存储训练实例而不是构建显式模型。
---
## Definition

惰性学习者（如k近邻算法）会记住整个训练数据集，仅在做出预测时才进行计算。这与急切学习形成对比，后者会在训练阶段构建一个通用模型。

### Summary

一种学习方法，将泛化推迟到分类时才进行，存储训练实例而不是构建显式模型。

## Key Concepts

- 基于实例的学习
- k近邻算法
- 推理成本
- 泛化

## Use Cases

- 推荐系统
- 小数据集的模式识别
- 预测模型的原型设计

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)
```

## Related Terms

- [instance_based_learning (基于实例的学习)](/en/terms/instance_based_learning-基于实例的学习/)
- [knn (k近邻算法)](/en/terms/knn-k近邻算法/)
- [eager_learning (急切学习)](/en/terms/eager_learning-急切学习/)
- [generalization (泛化)](/en/terms/generalization-泛化/)
