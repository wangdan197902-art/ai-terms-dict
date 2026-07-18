---
title: "自动化机器学习"
term_id: "automated_machine_learning"
category: "training_techniques"
subcategory: ""
tags: ["automation", "efficiency", "workflow"]
difficulty: 3
weight: 1
slug: "automated_machine_learning"
aliases:
  - /zh/terms/automated_machine_learning/
date: "2026-07-18T11:07:26.676095Z"
lastmod: "2026-07-18T11:44:45.447844Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种自动化将机器学习应用于现实世界问题端到端过程的方法论，从而减少人工工作量。"
---

## Definition

AutoML（自动化机器学习）通过自动化数据预处理、特征工程、模型选择和超参数调整等任务，简化了ML模型的开发。它使得非专家也能使用。

### Summary

一种自动化将机器学习应用于现实世界问题端到端过程的方法论，从而减少人工工作量。

## Key Concepts

- 超参数调优
- 特征工程
- 模型选择
- 民主化

## Use Cases

- 业务分析师的快速原型设计
- 优化大规模生产管道
- 自动比较多种算法

## Code Example

```python
from auto_ml import Predictor
predictor = Predictor(type_of_estimator='classifier')
predictor.fit(dataframe, target='label')
```

## Related Terms

- [超参数优化 (Hyperparameter Optimization)](/en/terms/超参数优化-hyperparameter-optimization/)
- [神经架构搜索 (Neural Architecture Search)](/en/terms/神经架构搜索-neural-architecture-search/)
- [MLOps (MLOps)](/en/terms/mlops-mlops/)
- [无代码AI (No-Code AI)](/en/terms/无代码ai-no-code-ai/)
