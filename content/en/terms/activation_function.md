---
title: "Activation Function"
term_id: "activation_function"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "mathematics", "deep_learning", "basics"]
difficulty: 3
weight: 1
slug: "activation_function"
aliases:
  - /en/terms/activation_function/
date: "2026-07-18T09:39:58.032332Z"
lastmod: "2026-07-18T11:44:44.620165Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A mathematical equation that determines the output of a neural network node based on its input signal."
---

## Definition

An activation function introduces non-linearity into a neural network, allowing it to learn complex patterns and relationships within data. Without these functions, a multi-layered network would behave like a single linear regression model, severely limiting its expressive power. Common examples include ReLU, Sigmoid, and Tanh. They decide whether a neuron should be activated or not by calculating a weighted sum and possibly adding a bias, effectively filtering signals to propagate only significant information through the network layers during forward propagation.

### Summary

A mathematical equation that determines the output of a neural network node based on its input signal.

## Key Concepts

- Non-linearity
- Gradient Descent
- Neuron Activation
- Backpropagation

## Use Cases

- Enabling deep neural networks to classify images
- Facilitating natural language processing tasks
- Improving convergence speed in training generative models

## Code Example

```python
import torch.nn as nn
relu = nn.ReLU()
output = relu(input_tensor)
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Sigmoid](/en/terms/sigmoid/)
- [Tanh](/en/terms/tanh/)
- [Softmax](/en/terms/softmax/)
