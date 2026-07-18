---
title: "知识蒸馏"
term_id: "distillation"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "compression", "model_efficiency"]
difficulty: 3
weight: 1
slug: "distillation"
aliases:
  - /zh/terms/distillation/
date: "2026-07-18T10:50:42.926016Z"
lastmod: "2026-07-18T11:44:45.365243Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "知识蒸馏是一种模型压缩技术，其中较小的学生模型通过学习模仿较大的教师模型的行为来工作。"
---

## Definition

这一过程涉及将知识从复杂的高性能“教师”神经网络转移到更简单、高效的“学生”网络中。学生不仅从硬标签中学习，还从软标签（即教师模型的输出概率分布）中学习，从而捕捉更丰富的信息。

### Summary

知识蒸馏是一种模型压缩技术，其中较小的学生模型通过学习模仿较大的教师模型的行为来工作。

## Key Concepts

- 师生架构
- 软目标
- 模型压缩
- 推理效率

## Use Cases

- 在移动设备上部署大型语言模型
- 降低实时计算机视觉应用中的延迟
- 优化边缘计算环境中的深度学习模型

## Related Terms

- [量化 (Quantization)](/en/terms/量化-quantization/)
- [剪枝 (Pruning)](/en/terms/剪枝-pruning/)
- [迁移学习 (Transfer Learning)](/en/terms/迁移学习-transfer-learning/)
- [神经架构搜索 (Neural Architecture Search)](/en/terms/神经架构搜索-neural-architecture-search/)
