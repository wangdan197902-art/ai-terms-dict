---
title: Adapter
term_id: adapter
category: training_techniques
subcategory: ''
tags:
- Fine-Tuning
- efficiency
- transformers
- Optimization
difficulty: 4
weight: 1
slug: adapter
date: '2026-07-18T09:39:58.032342Z'
lastmod: '2026-07-18T11:44:44.620430Z'
draft: false
source: agnes_llm
status: published
language: en
description: A lightweight module inserted into pre-trained models to enable efficient
  fine-tuning for specific downstream tasks.
---
## Definition

Adapters are a parameter-efficient fine-tuning technique used primarily in large language models and transformers. Instead of updating all model weights, which is computationally expensive, adapters introduce small, task-specific neural network layers between existing layers. This allows the model to retain its general knowledge while adapting to new tasks with minimal additional parameters. It significantly reduces memory usage and storage requirements, making it feasible to deploy multiple specialized models on top of a single base model without catastrophic forgetting.

### Summary

A lightweight module inserted into pre-trained models to enable efficient fine-tuning for specific downstream tasks.

## Key Concepts

- Parameter-Efficient Fine-Tuning
- Transfer Learning
- Modular Architecture
- Catastrophic Forgetting

## Use Cases

- Fine-tuning LLMs for customer service chatbots
- Adapting vision models for medical image analysis
- Deploying multiple domain-specific models efficiently

## Related Terms

- [LoRA](/en/terms/lora/)
- [Prompt Tuning](/en/terms/prompt-tuning/)
- [Fine-Tuning](/en/terms/fine-tuning/)
- [Transformer](/en/terms/transformer/)
