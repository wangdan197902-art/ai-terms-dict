---
title: "稳定性"
term_id: "stability"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "theory", "robustness"]
difficulty: 2
weight: 1
slug: "stability"
aliases:
  - /zh/terms/stability/
date: "2026-07-18T11:35:05.879823Z"
lastmod: "2026-07-18T11:44:45.558523Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "机器学习模型在训练数据发生微小变化时，仍能产生一致预测结果的属性。"
---

## Definition

在机器学习中，稳定性（Stability）指模型的性能和参数在面对训练数据的微小扰动时保持稳健的程度。一个稳定的算法即使输入数据略有不同，也能生成相似的模型或预测结果。稳定性是评估模型可靠性和泛化能力的重要指标，通常与方差（Variance）密切相关，高稳定性意味着低方差。

### Summary

机器学习模型在训练数据发生微小变化时，仍能产生一致预测结果的属性。

## Key Concepts

- 鲁棒性
- 泛化能力
- 方差
- 重采样

## Use Cases

- 评估模型可靠性
- 为关键应用选择算法
- 交叉验证策略设计

## Related Terms

- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
- [Bias-Variance Tradeoff (偏差-方差权衡)](/en/terms/bias-variance-tradeoff-偏差-方差权衡/)
- [Bootstrap Aggregating (Bagging/自助聚合)](/en/terms/bootstrap-aggregating-bagging-自助聚合/)
- [Regularization (正则化)](/en/terms/regularization-正则化/)
