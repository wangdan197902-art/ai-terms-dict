---
title: 协同训练
term_id: co_training
category: training_techniques
subcategory: ''
tags:
- Semi Supervised
- algorithm
- Data Efficiency
difficulty: 4
weight: 1
slug: co_training
date: '2026-07-18T11:10:07.300963Z'
lastmod: '2026-07-18T11:44:45.456987Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 协同训练是一种半监督学习算法，利用数据的两个视图训练独立的分类器，这些分类器迭代地为彼此标记未标记数据。
---
## Definition

该方法利用同一数据点的多个不同特征集（视图）。最初，在每个视图的小规模标注数据集上训练两个分类器。随后，它们对未标记数据进行预测，并仅选择高置信度的标签来辅助对方模型的训练。

### Summary

协同训练是一种半监督学习算法，利用数据的两个视图训练独立的分类器，这些分类器迭代地为彼此标记未标记数据。

## Key Concepts

- 半监督学习
- 多视图
- 迭代标记
- 高置信度选择

## Use Cases

- 具有多特征的文本分类
- 网页分类
- 有限标签下的数据增强

## Related Terms

- [Semi-Supervised Learning (半监督学习)](/en/terms/semi-supervised-learning-半监督学习/)
- [Self-Training (自训练)](/en/terms/self-training-自训练/)
- [Multi-view Learning (多视图学习)](/en/terms/multi-view-learning-多视图学习/)
- [Active Learning (主动学习)](/en/terms/active-learning-主动学习/)
