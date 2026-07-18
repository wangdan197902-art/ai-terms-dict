---
title: "梯度累积"
term_id: "gradient_accumulation"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Deep Learning", "Hardware"]
difficulty: 4
weight: 1
slug: "gradient_accumulation"
aliases:
  - /zh/terms/gradient_accumulation/
date: "2026-07-18T11:19:45.206397Z"
lastmod: "2026-07-18T11:44:45.510866Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "梯度累积是一种通过在前向/反向传播过程中累加多个步骤的梯度，从而模拟更大批量大小的技术，之后才更新权重。"
---

## Definition

这种优化策略允许深度学习模型使用超出 GPU 显存容量的有效批量大小进行训练。通过从多个小批量中累积梯度并执行权重更新，可以实现这一目标。

### Summary

梯度累积是一种通过在前向/反向传播过程中累加多个步骤的梯度，从而模拟更大批量大小的技术，之后才更新权重。

## Key Concepts

- 批量大小模拟
- 内存优化
- 随机梯度下降
- 权重更新

## Use Cases

- 微调大模型
- 在有限显存下训练
- 稳定损失收敛

## Related Terms

- [批归一化](/en/terms/批归一化/)
- [学习率缩放](/en/terms/学习率缩放/)
- [优化器](/en/terms/优化器/)
- [反向传播](/en/terms/反向传播/)
