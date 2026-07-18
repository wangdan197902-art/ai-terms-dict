---
title: "用于学习的近端梯度方法"
term_id: "proximal_gradient_methods_for_learning"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "mathematics", "regression"]
difficulty: 4
weight: 1
slug: "proximal_gradient_methods_for_learning"
aliases:
  - /zh/terms/proximal_gradient_methods_for_learning/
date: "2026-07-18T11:30:52.811066Z"
lastmod: "2026-07-18T11:44:45.546484Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "旨在最小化包含平滑和非平滑分量的复合目标函数的优化算法。"
---

## Definition

近端梯度方法是一种迭代优化技术，当损失函数包含可微分的平滑项和不可微分的正则项（如L1范数）时使用。该算法通过将平滑部分的梯度下降步骤与非平滑部分的近端算子（proximal operator）相结合，有效地处理非光滑优化问题。

### Summary

旨在最小化包含平滑和非平滑分量的复合目标函数的优化算法。

## Key Concepts

- 复合优化
- 近端算子
- L1正则化
- 非光滑凸性

## Use Cases

- 稀疏特征选择
- Lasso回归
- 结构化预测模型

## Related Terms

- [梯度下降 (Gradient Descent)](/en/terms/梯度下降-gradient-descent/)
- [Lasso (Least Absolute Shrinkage and Selection Operator)](/en/terms/lasso-least-absolute-shrinkage-and-selection-operator/)
- [凸优化 (Convex Optimization)](/en/terms/凸优化-convex-optimization/)
- [正则化 (Regularization)](/en/terms/正则化-regularization/)
