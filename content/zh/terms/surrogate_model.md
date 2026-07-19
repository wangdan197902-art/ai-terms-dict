---
title: 代理模型
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T11:35:31.276932Z'
lastmod: '2026-07-18T11:44:45.560176Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种简化的数学模型，用于近似更复杂、计算成本高或不可访问的黑盒模型的行为。
---
## Definition

在机器学习和优化中，代理模型作为难以直接评估的目标函数的代理。它通过原始模型的输入-输出对进行训练，以预测目标函数的行为。

### Summary

一种简化的数学模型，用于近似更复杂、计算成本高或不可访问的黑盒模型的行为。

## Key Concepts

- 模型近似
- 黑盒优化
- 计算效率
- 代理模型

## Use Cases

- 超参数优化
- 工程设计模拟加速
- 复杂系统的敏感性分析

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Bayesian Optimization (贝叶斯优化)](/en/terms/bayesian-optimization-贝叶斯优化/)
- [Gaussian Process (高斯过程)](/en/terms/gaussian-process-高斯过程/)
- [Black-Box Function (黑盒函数)](/en/terms/black-box-function-黑盒函数/)
- [Emulator (模拟器)](/en/terms/emulator-模拟器/)
