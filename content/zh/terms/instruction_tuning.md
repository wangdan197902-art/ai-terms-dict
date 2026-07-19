---
title: 指令微调
term_id: instruction_tuning
category: training_techniques
subcategory: ''
tags:
- training
- LLM
difficulty: 3
weight: 1
slug: instruction_tuning
date: '2026-07-18T10:52:05.447706Z'
lastmod: '2026-07-18T11:44:45.372639Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 指令微调是一种微调技术，通过在包含指令及其对应响应的数据集上训练预训练语言模型，以提升其遵循任务指令的能力。
---
## Definition

这一过程弥合了通用预训练与特定任务表现之间的差距。通过让模型接触多样化的指令-响应对，它学会了泛化到未见过的任务，而无需针对每个新任务进行额外的调整（注：原文截断，此处补全语义）。这是使大语言模型具备人类对齐能力的关键步骤。

### Summary

指令微调是一种微调技术，通过在包含指令及其对应响应的数据集上训练预训练语言模型，以提升其遵循任务指令的能力。

## Key Concepts

- 微调
- 监督学习
- 零样本泛化
- 人类对齐

## Use Cases

- 构建聊天机器人
- 提高代码生成的准确性
- 使模型符合安全准则

## Related Terms

- [fine-tuning (微调)](/en/terms/fine-tuning-微调/)
- [RLHF (基于人类反馈的强化学习)](/en/terms/rlhf-基于人类反馈的强化学习/)
- [pre-training (预训练)](/en/terms/pre-training-预训练/)
- [alignment (对齐)](/en/terms/alignment-对齐/)
