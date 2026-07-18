---
title: "Prefix Tuning"
term_id: "prefix_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "transformers"]
difficulty: 4
weight: 1
slug: "prefix_tuning"
aliases:
  - /en/terms/prefix_tuning/
date: "2026-07-18T10:11:14.173198Z"
lastmod: "2026-07-18T11:44:44.710561Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A parameter-efficient fine-tuning method that adds trainable continuous vectors to the input of transformer layers."
---

## Definition

Prefix Tuning is a parameter-efficient adaptation technique for pre-trained transformers. Instead of updating all model weights, it prepends a sequence of trainable continuous vectors (the prefix) to the input embeddings of each layer. These prefixes act as soft prompts that guide the model's behavior for specific downstream tasks while keeping the base model frozen. This approach significantly reduces memory and computational costs compared to full fine-tuning, making it suitable for resource-constrained environments.

### Summary

A parameter-efficient fine-tuning method that adds trainable continuous vectors to the input of transformer layers.

## Key Concepts

- Parameter-efficient tuning
- Soft prompts
- Transformer layers
- Frozen backbone

## Use Cases

- Few-shot learning adaptation
- Multi-task learning with limited resources
- Customizing LLMs for niche domains

## Related Terms

- [prompt_tuning](/en/terms/prompt_tuning/)
- [p_tuning](/en/terms/p_tuning/)
- [adapter_modules](/en/terms/adapter_modules/)
- [peft](/en/terms/peft/)
