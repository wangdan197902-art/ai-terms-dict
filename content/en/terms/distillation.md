---
title: Distillation
term_id: distillation
category: training_techniques
subcategory: ''
tags:
- Optimization
- compression
- Model Efficiency
difficulty: 3
weight: 1
slug: distillation
date: '2026-07-18T09:31:32.608867Z'
lastmod: '2026-07-18T11:44:44.595716Z'
draft: false
source: agnes_llm
status: published
language: en
description: Knowledge distillation is a model compression technique where a smaller
  student model learns to mimic the behavior of a larger teacher model.
---
## Definition

This process involves transferring knowledge from a complex, high-performance 'teacher' neural network to a simpler, more efficient 'student' network. The student learns not just from hard labels but also from the soft probability distributions output by the teacher, which contain richer information about class relationships. This allows the student to achieve comparable accuracy with significantly fewer parameters, enabling faster inference and lower computational costs, making it ideal for deployment on resource-constrained devices like mobile phones or edge hardware.

### Summary

Knowledge distillation is a model compression technique where a smaller student model learns to mimic the behavior of a larger teacher model.

## Key Concepts

- Teacher-Student Architecture
- Soft Targets
- Model Compression
- Inference Efficiency

## Use Cases

- Deploying large language models on mobile devices
- Reducing latency in real-time computer vision applications
- Optimizing deep learning models for edge computing environments

## Related Terms

- [Quantization](/en/terms/quantization/)
- [Pruning](/en/terms/pruning/)
- [Transfer Learning](/en/terms/transfer-learning/)
- [Neural Architecture Search](/en/terms/neural-architecture-search/)
