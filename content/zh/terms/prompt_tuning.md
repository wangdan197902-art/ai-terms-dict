---
title: 提示微调
term_id: prompt_tuning
category: training_techniques
subcategory: ''
tags:
- LLM
- Optimization
- efficiency
difficulty: 3
weight: 1
slug: prompt_tuning
date: '2026-07-18T11:30:52.811051Z'
lastmod: '2026-07-18T11:44:45.546342Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种参数高效的微调方法，通过优化连续的输入嵌入（embeddings）而非更新整个模型权重来调整模型。
---
## Definition

提示微调涉及在预训练语言模型的输入层添加可训练的软提示（连续向量），同时保持底层模型参数冻结。这种方法允许在几乎不增加计算成本的情况下，使模型适应特定任务或领域，特别适用于资源受限的场景。

### Summary

一种参数高效的微调方法，通过优化连续的输入嵌入（embeddings）而非更新整个模型权重来调整模型。

## Key Concepts

- 软提示 (Soft Prompts)
- 参数效率
- 冻结权重
- 少样本学习 (Few-shot Learning)

## Use Cases

- 针对特定领域适配大语言模型
- 低资源环境下的微调
- 多任务学习优化

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning, 参数高效微调)](/en/terms/peft-parameter-efficient-fine-tuning-参数高效微调/)
- [LoRA (Low-Rank Adaptation, 低秩自适应)](/en/terms/lora-low-rank-adaptation-低秩自适应/)
- [上下文学习 (In-context Learning)](/en/terms/上下文学习-in-context-learning/)
- [微调 (Fine-tuning)](/en/terms/微调-fine-tuning/)
