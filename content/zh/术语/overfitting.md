---
title: "过拟合"
term_id: "overfitting"
category: "training_techniques"
subcategory: ""
tags: ["model_evaluation", "training_dynamics", "generalization"]
difficulty: 2
weight: 1
slug: "overfitting"
aliases:
  - /zh/terms/overfitting/
date: "2026-07-18T11:01:16.765858Z"
lastmod: "2026-07-18T11:44:45.403556Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种建模误差，机器学习算法捕捉到了噪声而非潜在信号，从而损害了泛化能力。"
---

## Definition

当模型对训练数据学习得过于完美，包括其随机噪声和异常值时，就会发生过拟合。这导致模型在训练数据上表现优异，但在新的、未见过的测试数据上表现糟糕。

### Summary

一种建模误差，机器学习算法捕捉到了噪声而非潜在信号，从而损害了泛化能力。

## Key Concepts

- 高方差
- 泛化能力差
- 训练误差与测试误差差距大
- 模型复杂度

## Use Cases

- 诊断模型性能问题
- 选择正则化强度
- 确定最佳模型深度

## Related Terms

- [underfitting (欠拟合)](/en/terms/underfitting-欠拟合/)
- [regularization (正则化)](/en/terms/regularization-正则化/)
- [cross_validation (交叉验证)](/en/terms/cross_validation-交叉验证/)
- [bias_variance_tradeoff (偏差-方差权衡)](/en/terms/bias_variance_tradeoff-偏差-方差权衡/)
