---
title: "Knowledge Distillation"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /en/terms/knowledge_distillation/
date: "2026-07-18T10:03:41.614718Z"
lastmod: "2026-07-18T11:44:44.688551Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Knowledge distillation is a model compression technique where a smaller student model learns to mimic the behavior of a larger teacher model."
---

## Definition

Knowledge distillation is a machine learning method used to compress a large, complex neural network (the teacher) into a smaller, more efficient network (the student). The student model is trained to replicate the output probabilities of the teacher model rather than just the ground truth labels. This process allows the student to capture nuanced patterns and relationships learned by the teacher, resulting in a model that maintains high accuracy while requiring fewer computational resources and memory for deployment.

### Summary

Knowledge distillation is a model compression technique where a smaller student model learns to mimic the behavior of a larger teacher model.

## Key Concepts

- Teacher-Student Model
- Model Compression
- Soft Targets
- Efficiency

## Use Cases

- Deploying models on edge devices
- Reducing inference latency
- Lowering cloud computing costs

## Code Example

```python
import torch
import torch.nn as nn

def distillation_loss(student_logits, teacher_logits, temperature=2.0):
    T = temperature
    student_probs = nn.functional.softmax(student_logits / T, dim=1)
    teacher_probs = nn.functional.softmax(teacher_logits / T, dim=1)
    return nn.functional.kl_div(
        nn.functional.log_softmax(student_logits / T, dim=1),
        teacher_probs,
        reduction='batchmean'
    ) * (T * T)
```

## Related Terms

- [Model Compression](/en/terms/model-compression/)
- [Pruning](/en/terms/pruning/)
- [Quantization](/en/terms/quantization/)
- [Neural Networks](/en/terms/neural-networks/)
