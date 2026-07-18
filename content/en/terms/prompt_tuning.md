---
title: "Prompt Tuning"
term_id: "prompt_tuning"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "optimization", "efficiency"]
difficulty: 3
weight: 1
slug: "prompt_tuning"
aliases:
  - /en/terms/prompt_tuning/
date: "2026-07-18T10:12:36.195339Z"
lastmod: "2026-07-18T11:44:44.712560Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A parameter-efficient fine-tuning method that optimizes continuous input embeddings rather than updating the entire model weights."
---

## Definition

Prompt tuning involves adding trainable soft prompts (continuous vectors) to the input layer of a pre-trained language model while keeping the underlying model parameters frozen. This approach allows for efficient adaptation to specific downstream tasks with minimal computational cost and storage requirements. It leverages the model's existing knowledge, making it highly effective for few-shot learning scenarios where labeled data is scarce.

### Summary

A parameter-efficient fine-tuning method that optimizes continuous input embeddings rather than updating the entire model weights.

## Key Concepts

- soft prompts
- parameter efficiency
- frozen weights
- few-shot learning

## Use Cases

- Adapting LLMs for specific domains
- Low-resource fine-tuning
- Multi-task learning optimization

## Related Terms

- [PEFT](/en/terms/peft/)
- [LoRA](/en/terms/lora/)
- [in-context learning](/en/terms/in-context-learning/)
- [fine-tuning](/en/terms/fine-tuning/)
