---
title: "核密度估计"
term_id: "kernel_density_estimation"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "probability", "data-analysis"]
difficulty: 3
weight: 1
slug: "kernel_density_estimation"
aliases:
  - /zh/terms/kernel_density_estimation/
date: "2026-07-18T11:22:59.294449Z"
lastmod: "2026-07-18T11:44:45.520254Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种非参数方法，用于根据有限的数据样本来估计随机变量的概率密度函数。"
---

## Definition

核密度估计（KDE）是一种基本的统计技术，通过对离散数据点进行平滑处理，生成连续的概率分布曲线。它在每个数据点处放置一个核函数（通常为高斯核），并将这些核函数叠加起来，从而估计出潜在的概率密度函数。

### Summary

一种非参数方法，用于根据有限的数据样本来估计随机变量的概率密度函数。

## Key Concepts

- 概率密度函数
- 非参数统计
- 平滑处理
- 高斯核

## Use Cases

- 探索性数据分析 (EDA)
- 单变量数据中的异常检测
- 可视化数据集中的特征分布

## Code Example

```python
from scipy.stats import gaussian_kde
import numpy as np

data = np.random.normal(0, 1, 100)
kde = gaussian_kde(data)
x_vals = np.linspace(-3, 3, 100)
y_vals = kde(x_vals)
```

## Related Terms

- [直方图 (Histogram)](/en/terms/直方图-histogram/)
- [帕尔泽窗 (Parzen Window)](/en/terms/帕尔泽窗-parzen-window/)
- [带宽选择 (Bandwidth Selection)](/en/terms/带宽选择-bandwidth-selection/)
- [SciPy统计模块 (Scipy Stats)](/en/terms/scipy统计模块-scipy-stats/)
