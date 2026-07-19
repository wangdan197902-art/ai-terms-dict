---
title: 课程学习
term_id: curriculum_learning
category: training_techniques
subcategory: ''
tags:
- Optimization
- Training Strategy
difficulty: 3
weight: 1
slug: curriculum_learning
date: '2026-07-18T11:38:39.318172Z'
lastmod: '2026-07-18T11:44:45.570396Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种训练策略，模型先学习简单的示例，然后再逐步过渡到更难的示例。
---
## Definition

课程学习模仿人类教育过程，以结构化的顺序呈现训练数据，通常从简单样本开始，并逐渐增加复杂度。这种方法有助于神经网络更好地收敛并提高泛化能力。

### Summary

一种训练策略，模型先学习简单的示例，然后再逐步过渡到更难的示例。

## Key Concepts

- 渐进式难度
- 样本排序
- 收敛速度
- 泛化能力

## Use Cases

- 在复杂图像数据集上训练深度神经网络
- 针对不同句子复杂度的语言建模
- 具有稀疏奖励的强化学习任务

## Related Terms

- [Transfer Learning (迁移学习)](/en/terms/transfer-learning-迁移学习/)
- [Hard Negative Mining (难例挖掘)](/en/terms/hard-negative-mining-难例挖掘/)
- [Data Augmentation (数据增强)](/en/terms/data-augmentation-数据增强/)
- [Self-Paced Learning (自步学习)](/en/terms/self-paced-learning-自步学习/)
