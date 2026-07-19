---
title: 随机特征
term_id: random_feature
category: basic_concepts
subcategory: ''
tags:
- Kernel Methods
- Feature Engineering
- Optimization
difficulty: 3
weight: 1
slug: random_feature
date: '2026-07-18T11:31:50.443887Z'
lastmod: '2026-07-18T11:44:45.549412Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种利用随机投影将输入数据映射到高维空间的技术，以高效近似核方法。
---
## Definition

随机特征映射将输入转换到新空间，使线性模型能够近似非线性核函数。这种方法通常与 Nyström 方法或傅里叶特征相关联，允许在保持计算效率的同时处理复杂的非线性关系。

### Summary

一种利用随机投影将输入数据映射到高维空间的技术，以高效近似核方法。

## Key Concepts

- 核近似
- 特征映射
- 计算效率
- 线性化

## Use Cases

- 大规模核回归
- 神经切线核 (NTK) 近似
- 可扩展的高斯过程

## Code Example

```python
import numpy as np
from sklearn.kernel_approximation import RBFSampler
X = np.random.rand(100, 5)
transformer = RBFSampler(gamma=1, n_components=50, random_state=42)
X_transformed = transformer.fit_transform(X)
```

## Related Terms

- [核技巧 (Kernel trick)](/en/terms/核技巧-kernel-trick/)
- [傅里叶特征 (Fourier features)](/en/terms/傅里叶特征-fourier-features/)
- [Nyström 方法 (Nystrom method)](/en/terms/nyström-方法-nystrom-method/)
- [降维 (Dimensionality reduction)](/en/terms/降维-dimensionality-reduction/)
