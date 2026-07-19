---
title: Softmax
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T09:42:48.759008Z'
lastmod: '2026-07-18T11:44:44.633382Z'
draft: false
source: agnes_llm
status: published
language: en
description: A mathematical function that converts a vector of arbitrary real-valued
  scores into a probability distribution.
---
## Definition

Softmax is widely used in the output layer of neural networks for multi-class classification tasks. It takes a vector of raw logits and normalizes them so that each element represents a probability between 0 and 1, and all elements sum to 1. This allows the model to express confidence levels across mutually exclusive classes, making it essential for interpreting final predictions in classification models.

### Summary

A mathematical function that converts a vector of arbitrary real-valued scores into a probability distribution.

## Key Concepts

- Probability Distribution
- Logits
- Normalization
- Multi-class Classification

## Use Cases

- Image classification output layers
- Language model token prediction
- Multi-label categorization

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax](/en/terms/argmax/)
- [Cross-Entropy Loss](/en/terms/cross-entropy-loss/)
- [Logits](/en/terms/logits/)
- [Neural Network](/en/terms/neural-network/)
