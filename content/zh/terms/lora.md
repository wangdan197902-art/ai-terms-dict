---
title: "低秩自适应 (LoRA)"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
aliases:
  - /zh/terms/lora/
date: "2026-07-18T10:52:16.307004Z"
lastmod: "2026-07-18T11:44:45.374829Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "低秩自适应是一种参数高效的微调方法，它将可训练的秩分解矩阵注入现有模型权重中。"
---

## Definition

LoRA冻结预训练模型的权重，并在Transformer架构的每一层中插入可训练的分解矩阵。通过仅优化这些低秩矩阵，LoRA显著减少

### Summary

低秩自适应是一种参数高效的微调方法，它将可训练的秩分解矩阵注入现有模型权重中。

## Key Concepts

- 参数高效微调
- 秩分解
- 权重冻结
- 适配器模块

## Use Cases

- 定制大语言模型
- 领域特定适配
- 资源受限的训练环境

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (参数高效微调技术)](/en/terms/peft-参数高效微调技术/)
- [微调 (Fine-Tuning)](/en/terms/微调-fine-tuning/)
- [量化 (Quantization)](/en/terms/量化-quantization/)
