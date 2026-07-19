---
title: "Grok 1"
term_id: "grok_1"
category: "basic_concepts"
subcategory: ""
tags: ["models", "architecture", "history"]
difficulty: 3
weight: 1
slug: "grok_1"
date: "2026-07-18T11:20:24.485229Z"
lastmod: "2026-07-18T11:44:45.511750Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "xAI发布的首个版本的Grok语言模型，采用混合专家（MoE）架构，参数量约为330亿。"
---
## Definition

Grok-1是xAI于2023年11月发布的开创性产品。它是一个仅解码器（decoder-only）的基于Transformer架构的大型语言模型，拥有约330亿个参数。值得注意的是，它采用了混合专家（Mixture-of-Experts, MoE）架构，这意味着在每次推理过程中，并非所有参数都被激活，而是根据输入动态选择特定的“专家”子网络进行处理。这种设计提高了计算效率，允许模型在处理复杂任务时保持较高的性能，同时减少了资源消耗。

### Summary

xAI发布的首个版本的Grok语言模型，采用混合专家（MoE）架构，参数量约为330亿。

## Key Concepts

- 混合专家架构
- Transformer架构
- 参数量
- 仅解码器模型

## Use Cases

- 文本生成与补全
- 代码合成
- 复杂推理任务

## Related Terms

- [grok (Grok系列)](/en/terms/grok-grok系列/)
- [moe_architecture (混合专家架构)](/en/terms/moe_architecture-混合专家架构/)
- [transformer (Transformer架构)](/en/terms/transformer-transformer架构/)
- [large_language_model (大型语言模型)](/en/terms/large_language_model-大型语言模型/)
