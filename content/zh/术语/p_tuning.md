---
title: "P-Tuning"
term_id: "p_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "nlp"]
difficulty: 4
weight: 1
slug: "p_tuning"
aliases:
  - /zh/terms/p_tuning/
date: "2026-07-18T11:29:14.184533Z"
lastmod: "2026-07-18T11:44:45.539913Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "P-Tuning 是一种参数高效微调方法，它通过优化连续的提示嵌入（prompt embeddings）来适应任务，而不是更新整个预训练模型的权重。"
---

## Definition

P-Tuning（提示微调）是一种旨在以最低计算成本将大型预训练语言模型适配到特定下游任务的技术。与微调所有模型参数不同，P-Tuning 仅优化少量可学习的提示向量，同时保持预训练模型的权重冻结，从而显著降低资源消耗并防止灾难性遗忘。

### Summary

P-Tuning 是一种参数高效微调方法，它通过优化连续的提示嵌入（prompt embeddings）来适应任务，而不是更新整个预训练模型的权重。

## Key Concepts

- 参数高效微调
- 虚拟令牌
- 冻结权重
- 嵌入优化

## Use Cases

- 少样本学习适配
- 资源受限环境
- 大语言模型应用的快速原型开发

## Related Terms

- [LoRA (低秩适应)](/en/terms/lora-低秩适应/)
- [Adapter Modules (适配器模块)](/en/terms/adapter-modules-适配器模块/)
- [Prompt Engineering (提示工程)](/en/terms/prompt-engineering-提示工程/)
- [Transfer Learning (迁移学习)](/en/terms/transfer-learning-迁移学习/)
