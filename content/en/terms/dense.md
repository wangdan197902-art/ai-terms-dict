---
title: "Dense"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /en/terms/dense/
date: "2026-07-18T09:55:14.213499Z"
lastmod: "2026-07-18T11:44:44.664470Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A layer or tensor where every element is connected to every element of the previous layer or dimension."
---

## Definition

In neural networks, 'dense' refers to fully connected layers where each neuron receives input from all neurons in the preceding layer. This contrasts with sparse connections found in convolutional or recurrent architectures. Dense layers are fundamental for learning complex non-linear mappings between inputs and outputs, serving as the primary mechanism for feature integration and decision-making in feedforward networks.

### Summary

A layer or tensor where every element is connected to every element of the previous layer or dimension.

## Key Concepts

- Fully Connected
- Weight Matrix
- Activation Function
- Feature Integration

## Use Cases

- Final classification layers in MLPs
- Feature fusion in hybrid models
- Simple regression tasks

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network](/en/terms/feedforward-neural-network/)
- [Backpropagation](/en/terms/backpropagation/)
- [ReLU](/en/terms/relu/)
- [Bias Term](/en/terms/bias-term/)
