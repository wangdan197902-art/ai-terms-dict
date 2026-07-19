---
title: 裁剪
term_id: clip
category: engineering_practice
subcategory: ''
tags:
- Optimization
- stability
- engineering
difficulty: 3
weight: 1
slug: clip
date: '2026-07-18T11:10:07.300954Z'
lastmod: '2026-07-18T11:44:45.456720Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 裁剪是一种限制数值（如梯度或输出概率）幅度的技术，旨在防止训练过程中的数值不稳定。
---
## Definition

在深度学习工程中，裁剪通常应用于梯度以缓解梯度爆炸问题，确保反向传播的稳定性。它也可以指在应用激活函数之前限制输出 logits 的范围。

### Summary

裁剪是一种限制数值（如梯度或输出概率）幅度的技术，旨在防止训练过程中的数值不稳定。

## Key Concepts

- 梯度裁剪
- 数值稳定性
- 梯度爆炸
- 正则化

## Use Cases

- 循环神经网络训练
- 稳定 Transformer 训练
- 防止损失发散

## Related Terms

- [Learning Rate (学习率)](/en/terms/learning-rate-学习率/)
- [Backpropagation (反向传播)](/en/terms/backpropagation-反向传播/)
- [Vanishing Gradient (梯度消失)](/en/terms/vanishing-gradient-梯度消失/)
- [Normalization (归一化)](/en/terms/normalization-归一化/)
