---
title: 数据泄露
term_id: leakage
category: basic_concepts
subcategory: ''
tags:
- Data Integrity
- evaluation
- Best Practices
difficulty: 3
weight: 1
slug: leakage
date: '2026-07-18T11:23:53.060610Z'
lastmod: '2026-07-18T11:44:45.523580Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 当训练数据集之外的信息无意中影响模型时，就会发生数据泄露，导致性能评估过于乐观。
---
## Definition

数据泄露是机器学习中的一个关键错误，指模型在训练过程中获取了在预测时无法获得的信息。这通常是由于不恰当的数据处理（如未正确划分训练集和测试集）造成的。

### Summary

当训练数据集之外的信息无意中影响模型时，就会发生数据泄露，导致性能评估过于乐观。

## Key Concepts

- 目标泄露
- 训练-测试污染
- 正确的数据分割

## Use Cases

- 调试模型过拟合问题
- 验证特征工程流程
- 确保模型评估的稳健性

## Related Terms

- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
- [Cross-validation (交叉验证)](/en/terms/cross-validation-交叉验证/)
- [Feature engineering (特征工程)](/en/terms/feature-engineering-特征工程/)
