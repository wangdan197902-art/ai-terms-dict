---
title: 特征哈希
term_id: feature_hashing
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- Text Mining
- Optimization
difficulty: 3
weight: 1
slug: feature_hashing
date: '2026-07-18T11:17:13.896071Z'
lastmod: '2026-07-18T11:44:45.498544Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种利用哈希函数将高维稀疏特征映射到固定大小向量的技术。
---
## Definition

特征哈希，也称为哈希技巧（hashing trick），允许机器学习模型处理大型稀疏特征空间，而无需维护特征与索引之间的显式映射。通过应用哈希函数，模型可以直接将任意特征映射到固定的向量维度中，从而节省内存并简化特征工程流程。

### Summary

一种利用哈希函数将高维稀疏特征映射到固定大小向量的技术。

## Key Concepts

- 哈希函数
- 稀疏向量
- 降维
- 内存效率

## Use Cases

- 具有大型词汇表的文本分类
- 拥有海量物品集的推荐系统
- 实时流数据处理

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-hot encoding (独热编码)](/en/terms/one-hot-encoding-独热编码/)
- [Bag of Words (词袋模型)](/en/terms/bag-of-words-词袋模型/)
- [Dimensionality reduction (降维)](/en/terms/dimensionality-reduction-降维/)
- [Sparse matrix (稀疏矩阵)](/en/terms/sparse-matrix-稀疏矩阵/)
