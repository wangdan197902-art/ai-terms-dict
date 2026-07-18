---
title: "Supervised Fine-tuning"
term_id: "supervised_fine_tuning"
category: "training_techniques"
subcategory: ""
tags: ["training", "llm", "fine-tuning"]
difficulty: 4
weight: 1
slug: "supervised_fine_tuning"
aliases:
  - /en/terms/supervised_fine_tuning/
date: "2026-07-18T09:42:48.759015Z"
lastmod: "2026-07-18T11:44:44.633700Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "The process of further training a pre-trained model on a specific dataset to adapt it to a particular task or domain."
---

## Definition

Supervised Fine-tuning (SFT) involves taking a large pre-trained model, such as a language model, and continuing its training on a smaller, high-quality dataset labeled for a specific downstream task. Unlike initial pre-training which learns general patterns, SFT aligns the model's behavior with human preferences or specific instructions, significantly improving performance on niche tasks without requiring training from scratch.

### Summary

The process of further training a pre-trained model on a specific dataset to adapt it to a particular task or domain.

## Key Concepts

- Pre-trained Models
- Transfer Learning
- Instruction Tuning
- Domain Adaptation

## Use Cases

- Custom chatbot development
- Specialized medical Q&A systems
- Code generation assistants

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

- [Pre-training](/en/terms/pre-training/)
- [Reinforcement Learning from Human Feedback](/en/terms/reinforcement-learning-from-human-feedback/)
- [Prompt Engineering](/en/terms/prompt-engineering/)
- [LLM](/en/terms/llm/)
