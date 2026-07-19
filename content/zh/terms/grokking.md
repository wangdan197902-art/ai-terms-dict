---
title: "顿悟学习"
term_id: "grokking"
category: "basic_concepts"
subcategory: ""
tags: ["theory", "training", "phenomena"]
difficulty: 4
weight: 1
slug: "grokking"
date: "2026-07-18T11:20:24.485239Z"
lastmod: "2026-07-18T11:44:45.511866Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种现象，指神经网络在小数据集上经过长时间训练后，突然展现出良好的泛化能力，远超记忆训练数据的阶段。"
---
## Definition

顿悟学习（Grokking）是指深度学习中观察到的一种反直觉行为：模型在训练数据上长时间过拟合，表现出较差的泛化能力，但在经过漫长的训练周期后，突然在测试集上实现近乎完美的泛化。这种现象表明，优化过程可能存在两个截然不同的阶段：首先是记忆训练样本，随后是理解数据背后的潜在规律。顿悟学习对于理解神经网络的泛化界限、训练动力学以及记忆与学习之间的关系具有重要意义，尤其是在小数据集场景下。

### Summary

一种现象，指神经网络在小数据集上经过长时间训练后，突然展现出良好的泛化能力，远超记忆训练数据的阶段。

## Key Concepts

- 延迟泛化
- 过拟合
- 小数据集
- 优化动力学

## Use Cases

- 研究模型泛化能力的极限
- 分析训练动力学
- 理解记忆与学习的区别

## Related Terms

- [overfitting (过拟合)](/en/terms/overfitting-过拟合/)
- [generalization (泛化)](/en/terms/generalization-泛化/)
- [deep_learning_theory (深度学习理论)](/en/terms/deep_learning_theory-深度学习理论/)
- [training_dynamics (训练动力学)](/en/terms/training_dynamics-训练动力学/)
