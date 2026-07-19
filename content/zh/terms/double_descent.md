---
title: "双重下降"
term_id: "double_descent"
category: "basic_concepts"
subcategory: ""
tags: ["Theory", "Deep Learning", "Generalization"]
difficulty: 5
weight: 1
slug: "double_descent"
date: "2026-07-18T11:15:33.977837Z"
lastmod: "2026-07-18T11:44:45.491809Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "随着模型复杂度超过插值阈值，测试误差先下降、后上升、再次下降的现象。"
---
## Definition

双重下降挑战了传统的偏差-方差权衡理论，表明高度过参数化的模型即使插值了训练数据，也能实现较低的测试误差。起初，随着模型复杂度的增加，误差会上升，但在越过插值阈值后，误差会再次下降。

### Summary

随着模型复杂度超过插值阈值，测试误差先下降、后上升、再次下降的现象。

## Key Concepts

- 插值阈值
- 过参数化
- 偏差-方差权衡
- 测试误差

## Use Cases

- 分析神经网络缩放定律
- 理解深度学习中的泛化能力
- 大规模AI系统中的模型选择

## Related Terms

- [Overfitting (过拟合)](/en/terms/overfitting-过拟合/)
- [Underfitting (欠拟合)](/en/terms/underfitting-欠拟合/)
- [Neural Tangent Kernel (神经切线核)](/en/terms/neural-tangent-kernel-神经切线核/)
- [Regularization (正则化)](/en/terms/regularization-正则化/)
