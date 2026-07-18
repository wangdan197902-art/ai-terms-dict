---
title: "监督微调"
term_id: "supervised_fine_tuning"
category: "training_techniques"
subcategory: ""
tags: ["training", "llm", "fine-tuning"]
difficulty: 4
weight: 1
slug: "supervised_fine_tuning"
aliases:
  - /zh/terms/supervised_fine_tuning/
date: "2026-07-18T11:02:04.102309Z"
lastmod: "2026-07-18T11:44:45.406443Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "在特定数据集上进一步训练预训练模型，使其适应特定任务或领域的过程。"
---

## Definition

监督微调（SFT）涉及采用大型预训练模型（如语言模型），并在较小的高质量、针对特定下游任务标注的数据集上继续训练该模型。

### Summary

在特定数据集上进一步训练预训练模型，使其适应特定任务或领域的过程。

## Key Concepts

- 预训练模型
- 迁移学习
- 指令微调
- 领域适配

## Use Cases

- 定制聊天机器人开发
- 专业医疗问答系统
- 代码生成助手

## Code Example

```python
model.train()
for batch in dataloader:
    inputs, labels = batch
    outputs = model(inputs, labels=labels)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
```

## Related Terms

- [预训练 (Pre-training)](/en/terms/预训练-pre-training/)
- [基于人类反馈的强化学习 (RLHF)](/en/terms/基于人类反馈的强化学习-rlhf/)
- [提示工程 (Prompt Engineering)](/en/terms/提示工程-prompt-engineering/)
- [大语言模型 (LLM)](/en/terms/大语言模型-llm/)
