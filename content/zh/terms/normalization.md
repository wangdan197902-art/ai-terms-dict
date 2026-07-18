---
title: "归一化"
term_id: "normalization"
category: "basic_concepts"
subcategory: ""
tags: ["data_preprocessing", "mathematics", "ml_basics"]
difficulty: 2
weight: 1
slug: "normalization"
aliases:
  - /zh/terms/normalization/
date: "2026-07-18T11:28:24.370574Z"
lastmod: "2026-07-18T11:44:45.537397Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "归一化是一种数据预处理技术，将数值特征缩放到标准范围（通常为0到1之间），以改善模型的收敛速度和性能。"
---

## Definition

常见方法包括最小-最大缩放和Z分数标准化。此过程确保具有较大量级的特征不会主导学习算法，特别是在基于梯度的优化中。

### Summary

归一化是一种数据预处理技术，将数值特征缩放到标准范围（通常为0到1之间），以改善模型的收敛速度和性能。

## Key Concepts

- 最小-最大缩放
- Z分数标准化
- 特征缩放
- 梯度下降稳定性

## Use Cases

- 预处理图像像素值
- 为神经网络准备表格数据
- 提高回归模型的准确性

## Code Example

```python
from sklearn.preprocessing import MinMaxScaler
import numpy as np
data = np.array([[10], [20], [30]])
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)
```

## Related Terms

- [Standardization (标准化)](/en/terms/standardization-标准化/)
- [Data Preprocessing (数据预处理)](/en/terms/data-preprocessing-数据预处理/)
- [Feature Engineering (特征工程)](/en/terms/feature-engineering-特征工程/)
