---
title: ReLU
term_id: relu
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Activation Functions
- Deep Learning
difficulty: 3
weight: 1
slug: relu
date: '2026-07-18T09:42:48.752152Z'
lastmod: '2026-07-18T11:44:44.630363Z'
draft: false
source: agnes_llm
status: published
language: en
description: Rectified Linear Unit is an activation function that outputs the input
  directly if positive, otherwise zero.
---
## Definition

ReLU is widely used in deep learning neural networks due to its computational efficiency and ability to mitigate the vanishing gradient problem. Mathematically defined as f(x) = max(0, x), it introduces non-linearity into the model without saturating neurons for positive inputs. Despite potential issues like dying ReLUs, it remains a standard choice for hidden layers in convolutional and fully connected networks.

### Summary

Rectified Linear Unit is an activation function that outputs the input directly if positive, otherwise zero.

## Key Concepts

- Non-linearity
- Activation Function
- Vanishing Gradient
- Piecewise Linear

## Use Cases

- Hidden layers in CNNs
- Deep Feedforward Networks
- Image Recognition Models

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid](/en/terms/sigmoid/)
- [Tanh](/en/terms/tanh/)
- [Leaky ReLU](/en/terms/leaky-relu/)
- [Neural Network](/en/terms/neural-network/)
