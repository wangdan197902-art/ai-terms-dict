---
title: "微调"
term_id: "fine_tuning"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Optimization", "Deep Learning"]
difficulty: 3
weight: 1
slug: "fine_tuning"
aliases:
  - /zh/terms/fine_tuning/
date: "2026-07-18T07:44:46.533403Z"
lastmod: "2026-07-18T11:44:44.591805Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "使用较小的数据集将预训练模型适配到特定下游任务的过程。"
---

## Definition

微调涉及在一个已在大而通用数据集上训练好的模型基础上，继续在专业化数据集上进行训练。这使得模型在保留通用知识的同时，能够习得特定任务的技能。

### Summary

使用较小的数据集将预训练模型适配到特定下游任务的过程。

## Key Concepts

- 迁移学习
- 预训练模型
- 任务特定适配
- 学习率

## Use Cases

- 适配大语言模型以构建客户服务聊天机器人
- 专门化图像分类器用于医疗诊断
- 定制语音识别以针对特定口音

## Code Example

```python
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased')
# Freeze base layers
for param in model.bert.parameters():
    param.requires_grad = False
# Train only classification head
```

## Related Terms

- [预训练](/en/terms/预训练/)
- [提示工程](/en/terms/提示工程/)
- [LoRA (低秩适应)](/en/terms/lora-低秩适应/)
- [监督学习](/en/terms/监督学习/)
