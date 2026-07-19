---
title: 特征缩放
term_id: feature_scaling
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- statistics
- Optimization
difficulty: 2
weight: 1
slug: feature_scaling
date: '2026-07-18T11:17:13.896121Z'
lastmod: '2026-07-18T11:44:45.498954Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 将数据的独立变量或特征的范围进行归一化，以确保量级一致性的过程。
---
## Definition

特征缩放通过标准化输入变量的范围，防止量级较大的特征主导学习过程。常见方法包括归一化（最小-最大缩放）和标准化（Z-score标准化）。这一预处理步骤对于基于距离的算法和梯度下降优化至关重要，能加速收敛并提高模型性能。

### Summary

将数据的独立变量或特征的范围进行归一化，以确保量级一致性的过程。

## Key Concepts

- 归一化
- 标准化
- 梯度下降
- 数据预处理

## Use Cases

- 神经网络训练
- K-means聚类
- 支持向量机 (SVM)

## Code Example

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
```

## Related Terms

- [Min-Max Scaling (最小-最大缩放)](/en/terms/min-max-scaling-最小-最大缩放/)
- [Z-score Normalization (Z-score标准化)](/en/terms/z-score-normalization-z-score标准化/)
- [Data preprocessing (数据预处理)](/en/terms/data-preprocessing-数据预处理/)
- [Gradient Descent (梯度下降)](/en/terms/gradient-descent-梯度下降/)
