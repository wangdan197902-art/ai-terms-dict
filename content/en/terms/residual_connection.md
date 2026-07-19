---
title: Residual Connection
term_id: residual_connection
category: basic_concepts
subcategory: ''
tags:
- architecture
- Optimization
- Deep Learning
difficulty: 3
weight: 1
slug: residual_connection
date: '2026-07-18T09:42:48.752459Z'
lastmod: '2026-07-18T11:44:44.632226Z'
draft: false
source: agnes_llm
status: published
language: en
description: A mechanism that adds input directly to the output of a layer to facilitate
  gradient flow in deep networks.
---
## Definition

Residual connections, also known as skip connections, allow gradients to flow through a network by directly adding an input to a subsequent layer's output. This architecture solves the vanishing gradient problem, enabling the training of very deep neural networks like ResNet. By learning residual functions rather than unreferenced mappings, models can capture subtle changes while preserving original information, significantly improving convergence speed and accuracy in complex tasks.

### Summary

A mechanism that adds input directly to the output of a layer to facilitate gradient flow in deep networks.

## Key Concepts

- Skip Connections
- Vanishing Gradient Problem
- Deep Residual Learning
- Gradient Flow

## Use Cases

- Training deep convolutional neural networks
- Transformer architectures
- Image classification models

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection](/en/terms/skip_connection/)
- [vanishing_gradient](/en/terms/vanishing_gradient/)
- [deep_learning](/en/terms/deep_learning/)
- [resnet](/en/terms/resnet/)
