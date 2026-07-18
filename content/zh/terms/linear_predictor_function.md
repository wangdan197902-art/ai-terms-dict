---
title: "线性预测函数"
term_id: "linear_predictor_function"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "linear_models", "mathematics"]
difficulty: 2
weight: 1
slug: "linear_predictor_function"
aliases:
  - /zh/terms/linear_predictor_function/
date: "2026-07-18T11:24:20.005981Z"
lastmod: "2026-07-18T11:44:45.525056Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种计算输入变量的线性组合以预测结果的数学函数。"
---

## Definition

在统计建模和机器学习中，线性预测函数表示输入特征的加权和加上偏置项。它是广义线性模型（GLM）的核心组成部分。

### Summary

一种计算输入变量的线性组合以预测结果的数学函数。

## Key Concepts

- 加权和
- 偏置项
- 广义线性模型
- 特征系数

## Use Cases

- 线性回归分析
- 逻辑回归分类
- 支持向量机（核技巧上下文）

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (回归系数)](/en/terms/regression_coefficients-回归系数/)
- [bias_intercept (偏置/截距)](/en/terms/bias_intercept-偏置-截距/)
- [feature_engineering (特征工程)](/en/terms/feature_engineering-特征工程/)
- [generalized_linear_model (广义线性模型)](/en/terms/generalized_linear_model-广义线性模型/)
