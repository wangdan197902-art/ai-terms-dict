---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
aliases:
  - /en/terms/lora/
date: "2026-07-18T09:33:34.785728Z"
lastmod: "2026-07-18T11:44:44.601249Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Low-Rank Adaptation is a parameter-efficient fine-tuning method that injects trainable rank decomposition matrices into existing model weights."
---

## Definition

LoRA freezes pre-trained model weights and inserts trainable decomposition matrices into each layer of the Transformer architecture. By optimizing only these low-rank matrices, LoRA significantly reduces the number of trainable parameters, memory footprint, and computational cost during fine-tuning. This technique allows for rapid adaptation to specific downstream tasks while maintaining the general knowledge of the base model, making it highly popular for efficient custom model training.

### Summary

Low-Rank Adaptation is a parameter-efficient fine-tuning method that injects trainable rank decomposition matrices into existing model weights.

## Key Concepts

- Parameter-Efficient Fine-Tuning
- Rank Decomposition
- Freezing Weights
- Adapter Modules

## Use Cases

- Customizing LLMs
- Domain-Specific Adaptation
- Resource-Constrained Training

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT](/en/terms/peft/)
- [Fine-Tuning](/en/terms/fine-tuning/)
- [Quantization](/en/terms/quantization/)
