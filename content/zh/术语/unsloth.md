---
title: "Unsloth"
term_id: "unsloth"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "LLM", "training", "library"]
difficulty: 3
weight: 1
slug: "unsloth"
aliases:
  - /zh/terms/unsloth/
date: "2026-07-18T11:37:39.249101Z"
lastmod: "2026-07-18T11:44:45.566393Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "Unsloth 是一个开源库，通过优化的内存管理和内核实现，将大语言模型（LLM）的训练和推理速度提升高达 2 倍。"
---

## Definition

Unsloth 是一款专为优化大语言模型（LLM）的微调和部署而设计的工具。它通过替换标准的 PyTorch 操作，实现了显著的速度提升和内存占用减少。

### Summary

Unsloth 是一个开源库，通过优化的内存管理和内核实现，将大语言模型（LLM）的训练和推理速度提升高达 2 倍。

## Key Concepts

- 内存优化
- 自定义内核
- LLM 微调
- 加速推理

## Use Cases

- 在有限的 GPU 资源下微调 LLM
- 加速推理流水线
- 降低训练时的云计算成本

## Code Example

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-2-7b-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True
)
```

## Related Terms

- [LoRA (低秩适应)](/en/terms/lora-低秩适应/)
- [PyTorch (深度学习框架)](/en/terms/pytorch-深度学习框架/)
- [Hugging Face (模型社区平台)](/en/terms/hugging-face-模型社区平台/)
- [Flash Attention (高效注意力机制)](/en/terms/flash-attention-高效注意力机制/)
