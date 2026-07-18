---
title: "发散"
term_id: "divergence"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "stability", "debugging"]
difficulty: 2
weight: 1
slug: "divergence"
aliases:
  - /zh/terms/divergence/
date: "2026-07-18T10:50:42.926061Z"
lastmod: "2026-07-18T11:44:45.365394Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "发散是指机器学习算法的损失函数在训练过程中未能下降，导致性能不稳定或恶化的现象。"
---

## Definition

在优化的背景下，当模型参数的更新方式导致损失增加而不是减少时，就会发生发散，这通常会导致NaN值或无限梯度。这通常是由于学习率过高或数值不稳定性引起的。

### Summary

发散是指机器学习算法的损失函数在训练过程中未能下降，导致性能不稳定或恶化的现象。

## Key Concepts

- 损失爆炸
- 学习率敏感性
- 梯度不稳定
- 数值精度

## Use Cases

- 调试深度学习框架中的训练循环
- 调整超参数以实现稳定收敛
- 实施梯度裁剪策略以防止发散

## Related Terms

- [梯度消失 (Vanishing Gradient)](/en/terms/梯度消失-vanishing-gradient/)
- [梯度爆炸 (Exploding Gradient)](/en/terms/梯度爆炸-exploding-gradient/)
- [收敛 (Convergence)](/en/terms/收敛-convergence/)
- [稳定性 (Stability)](/en/terms/稳定性-stability/)
