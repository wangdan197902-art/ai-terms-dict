---
title: Feed-Forward Network
term_id: feed_forward_network
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- fundamentals
difficulty: 2
weight: 1
slug: feed_forward_network
date: '2026-07-18T09:58:07.186359Z'
lastmod: '2026-07-18T11:44:44.673179Z'
draft: false
source: agnes_llm
status: published
language: en
description: A class of artificial neural network where connections between nodes
  do not form cycles, propagating information in one direction.
---
## Definition

Feed-Forward Networks (FFNs), also known as Multi-Layer Perceptrons (MLPs), process data sequentially through layers of neurons from input to output without feedback loops. Each neuron receives inputs, applies weights and biases, and passes the result through an activation function. This architecture is fundamental for static input-output mappings, forming the basis for more complex architectures like Convolutional Neural Networks (CNNs) when combined with specific layer types.

### Summary

A class of artificial neural network where connections between nodes do not form cycles, propagating information in one direction.

## Key Concepts

- No cycles
- Layers (Input, Hidden, Output)
- Activation functions
- Weighted sums

## Use Cases

- Simple regression tasks
- Classification problems with tabular data
- Building blocks for deeper architectures

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron](/en/terms/multi-layer-perceptron/)
- [Backpropagation](/en/terms/backpropagation/)
- [Activation Function](/en/terms/activation-function/)
- [Neural Network](/en/terms/neural-network/)
