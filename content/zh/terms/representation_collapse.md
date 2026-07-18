---
title: "表征坍塌"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /zh/terms/representation_collapse/
date: "2026-07-18T11:32:14.210909Z"
lastmod: "2026-07-18T11:44:45.550612Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "自监督学习中的一种失效模式，模型对所有输入输出相同的表征，导致判别能力丧失。"
---

## Definition

当神经网络（特别是在自监督对比学习框架中）将所有输入数据点映射到同一个固定的输出向量时，就会发生表征坍塌。这种平凡解虽然最小化了损失函数，但未能学习到有用的特征表示。

### Summary

自监督学习中的一种失效模式，模型对所有输入输出相同的表征，导致判别能力丧失。

## Key Concepts

- 自监督学习
- 对比损失
- 平凡解
- 特征学习

## Use Cases

- 调试 SimCLR 或 MoCo 模型
- 改进对比损失函数
- 分析模型收敛性

## Related Terms

- [对比学习](/en/terms/对比学习/)
- [批归一化](/en/terms/批归一化/)
- [动量编码器](/en/terms/动量编码器/)
- [特征提取](/en/terms/特征提取/)
