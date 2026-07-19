---
title: 适配器
term_id: adapter
category: training_techniques
subcategory: ''
tags:
- Fine-Tuning
- efficiency
- transformers
- Optimization
difficulty: 4
weight: 1
slug: adapter
date: '2026-07-18T10:59:15.017987Z'
lastmod: '2026-07-18T11:44:45.396805Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 插入预训练模型中的轻量级模块，用于针对特定下游任务进行高效微调。
---
## Definition

适配器是一种参数高效的微调技术，主要用于大型语言模型和Transformer架构中。与计算成本高昂的更新所有模型权重不同，适配器仅训练少量新增参数，从而保留预训练知识并降低资源消耗。

### Summary

插入预训练模型中的轻量级模块，用于针对特定下游任务进行高效微调。

## Key Concepts

- 参数高效微调
- 迁移学习
- 模块化架构
- 灾难性遗忘

## Use Cases

- 为客服聊天机器人微调大型语言模型
- 适配视觉模型以进行医学图像分析
- 高效部署多个领域特定的模型

## Related Terms

- [LoRA (低秩适应)](/en/terms/lora-低秩适应/)
- [Prompt Tuning (提示微调)](/en/terms/prompt-tuning-提示微调/)
- [Fine-Tuning (微调)](/en/terms/fine-tuning-微调/)
- [Transformer (Transformer架构)](/en/terms/transformer-transformer架构/)
