---
title: "免训练的"
term_id: "training_free"
category: "training_techniques"
subcategory: ""
tags: ["techniques", "efficiency"]
difficulty: 3
weight: 1
slug: "training_free"
aliases:
  - /zh/terms/training_free/
date: "2026-07-18T10:59:01.893967Z"
lastmod: "2026-07-18T11:44:45.395776Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "无需执行基于梯度的参数更新即可适应或增强模型的方法。"
---

## Definition

免训练方法是指在不通过反向传播更新底层权重的情况下修改模型行为或输出的技术。这些方法通常利用提示工程、特征提取或其他非参数化手段来实现适配。

### Summary

无需执行基于梯度的参数更新即可适应或增强模型的方法。

## Key Concepts

- 提示工程
- 无梯度下降
- 参数高效
- 零成本适配

## Use Cases

- 通过提示进行少样本学习
- 无需微调的领域自适应
- 大语言模型应用的快速原型设计

## Related Terms

- [prompting (提示)](/en/terms/prompting-提示/)
- [fine_tuning (微调)](/en/terms/fine_tuning-微调/)
- [in_context_learning (上下文学习)](/en/terms/in_context_learning-上下文学习/)
