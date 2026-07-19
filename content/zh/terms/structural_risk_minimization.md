---
title: 结构风险最小化
term_id: structural_risk_minimization
category: basic_concepts
subcategory: ''
tags:
- Optimization
- theory
- Regularization
difficulty: 3
weight: 1
slug: structural_risk_minimization
date: '2026-07-18T11:35:19.163136Z'
lastmod: '2026-07-18T11:44:45.559640Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 统计学习中的一项原则，旨在通过平衡模型拟合度和复杂度来最小化泛化误差的上界。
---
## Definition

结构风险最小化（SRM）是一种通过控制模型复杂度来防止过拟合、从而最小化期望风险的方法。它在经验风险最小化的基础上增加了正则化项，以惩罚过于复杂的模型。

### Summary

统计学习中的一项原则，旨在通过平衡模型拟合度和复杂度来最小化泛化误差的上界。

## Key Concepts

- VC维
- 正则化
- 泛化误差
- 模型复杂度惩罚

## Use Cases

- 支持向量机（SVM）训练
- 回归分析中多项式阶数的选择
- 剪枝决策树以避免过拟合

## Related Terms

- [经验风险最小化 (Empirical risk minimization，最小化训练误差)](/en/terms/经验风险最小化-empirical-risk-minimization-最小化训练误差/)
- [奥卡姆剃刀 (Occam's razor，如无必要勿增实体的简约原则)](/en/terms/奥卡姆剃刀-occam-s-razor-如无必要勿增实体的简约原则/)
- [正则化 (Regularization，通过添加约束防止过拟合)](/en/terms/正则化-regularization-通过添加约束防止过拟合/)
- [偏差-方差权衡 (Bias-variance tradeoff，平衡模型误差来源)](/en/terms/偏差-方差权衡-bias-variance-tradeoff-平衡模型误差来源/)
