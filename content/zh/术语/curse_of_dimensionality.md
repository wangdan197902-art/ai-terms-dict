---
title: "维度灾难"
term_id: "curse_of_dimensionality"
category: "basic_concepts"
subcategory: ""
tags: ["theory", "data-science", "mathematics"]
difficulty: 3
weight: 1
slug: "curse_of_dimensionality"
aliases:
  - /zh/terms/curse_of_dimensionality/
date: "2026-07-18T11:12:12.555440Z"
lastmod: "2026-07-18T11:44:45.470329Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种现象，即空间的体积随维度呈指数级增加，导致数据变得稀疏，距离度量失效。"
---

## Definition

维度灾难是指在高维空间中分析数据时出现的各种现象，这些现象在低维设置中不会出现。随着特征数量的增加，数据点在空间中的分布变得极其稀疏，使得基于距离的算法（如K近邻）难以找到有意义的邻近点，从而导致模型性能下降。

### Summary

一种现象，即空间的体积随维度呈指数级增加，导致数据变得稀疏，距离度量失效。

## Key Concepts

- 高维空间
- 数据稀疏性
- 距离度量退化
- 指数增长

## Use Cases

- 证明使用PCA（主成分分析）的必要性
- 解释文本挖掘中模型失败的原因
- 设计特征选择策略

## Related Terms

- [Dimensionality Reduction (降维)](/en/terms/dimensionality-reduction-降维/)
- [PCA (主成分分析)](/en/terms/pca-主成分分析/)
- [Feature Selection (特征选择)](/en/terms/feature-selection-特征选择/)
