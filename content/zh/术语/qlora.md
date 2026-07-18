---
title: "QLoRA"
term_id: "qlora"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "fine-tuning", "efficiency"]
difficulty: 4
weight: 1
slug: "qlora"
aliases:
  - /zh/terms/qlora/
date: "2026-07-18T11:01:29.499777Z"
lastmod: "2026-07-18T11:44:45.404020Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "量化低秩适应，一种使用 4 位量化和低秩适配器高效微调大型语言模型的方法。"
---

## Definition

QLoRA 将低秩适应（LoRA）与 4 位量化相结合，显著减少了微调大规模模型所需的内存占用。通过将权重存储为 4 位格式并添加训练好的低秩适配器，该方法在保持性能的同时降低了资源需求。

### Summary

量化低秩适应，一种使用 4 位量化和低秩适配器高效微调大型语言模型的方法。

## Key Concepts

- 低秩适应
- 4 位量化
- 内存效率
- 微调

## Use Cases

- 消费级 GPU 微调
- 资源受限环境
- 快速模型迭代

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"])
model = get_peft_model(base_model, config)
```

## Related Terms

- [LoRA](/en/terms/lora/)
- [参数高效微调 (PEFT)](/en/terms/参数高效微调-peft/)
- [量化 (Quantization)](/en/terms/量化-quantization/)
- [参数高效微调 (Parameter-Efficient Fine-Tuning)](/en/terms/参数高效微调-parameter-efficient-fine-tuning/)
