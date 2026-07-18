---
title: "保留的（数据）"
term_id: "held_out"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "data_splitting", "validation"]
difficulty: 2
weight: 1
slug: "held_out"
aliases:
  - /zh/terms/held_out/
date: "2026-07-18T10:56:36.042490Z"
lastmod: "2026-07-18T11:44:45.390999Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "从训练集中预留的数据样本，用于评估模型性能并在开发过程中防止过拟合。"
---

## Definition

“保留的”数据集由故意排除在机器学习模型训练阶段之外的示例组成。该子集用于评估模型对未见数据的泛化能力，为开发者提供关于模型在真实场景中表现的无偏估计，从而辅助超参数调整和模型选择。

### Summary

从训练集中预留的数据样本，用于评估模型性能并在开发过程中防止过拟合。

## Key Concepts

- 泛化
- 过拟合
- 验证集
- 无偏评估

## Use Cases

- 调整超参数
- 比较不同的模型架构
- 生产部署前的最终性能估算

## Related Terms

- [training_set (训练集)](/en/terms/training_set-训练集/)
- [test_set (测试集)](/en/terms/test_set-测试集/)
- [cross_validation (交叉验证)](/en/terms/cross_validation-交叉验证/)
- [generalization (泛化)](/en/terms/generalization-泛化/)
