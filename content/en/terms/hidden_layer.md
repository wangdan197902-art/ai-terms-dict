---
title: "Hidden Layer"
term_id: "hidden_layer"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture", "deep_learning"]
difficulty: 3
weight: 1
slug: "hidden_layer"
aliases:
  - /en/terms/hidden_layer/
date: "2026-07-18T10:00:57.230697Z"
lastmod: "2026-07-18T11:44:44.680990Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "An intermediate layer in a neural network between the input and output layers that processes features."
---

## Definition

A hidden layer consists of neurons that receive inputs from previous layers, apply weights and biases, and pass transformed data forward through an activation function. These layers enable neural networks to learn complex, non-linear relationships in data. The depth and width of hidden layers determine the model's capacity to abstract features, making them fundamental to deep learning architectures like multilayer perceptrons and convolutional networks.

### Summary

An intermediate layer in a neural network between the input and output layers that processes features.

## Key Concepts

- Neural Networks
- Feature Extraction
- Activation Functions
- Deep Learning

## Use Cases

- Image recognition systems
- Natural language processing models
- Predictive analytics

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron](/en/terms/neuron/)
- [backpropagation](/en/terms/backpropagation/)
- [activation_function](/en/terms/activation_function/)
- [deep_learning](/en/terms/deep_learning/)
