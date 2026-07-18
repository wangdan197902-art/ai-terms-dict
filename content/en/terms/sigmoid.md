---
title: "Sigmoid"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
aliases:
  - /en/terms/sigmoid/
date: "2026-07-18T10:15:20.591896Z"
lastmod: "2026-07-18T11:44:44.721190Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A mathematical function that maps any real-valued number into a value between zero and one, forming an S-shaped curve."
---

## Definition

The sigmoid function, defined as σ(z) = 1 / (1 + e^-z), is widely used in machine learning to model probabilities. It squashes input values into the range (0, 1), making it suitable for binary classification output layers. While historically popular in logistic regression and early neural networks, it suffers from the vanishing gradient problem during backpropagation, which can slow down training in deep networks compared to alternatives like ReLU or Leaky ReLU.

### Summary

A mathematical function that maps any real-valued number into a value between zero and one, forming an S-shaped curve.

## Key Concepts

- Logistic function
- Probability mapping
- Vanishing gradient
- Non-linearity

## Use Cases

- Binary classification output
- Logistic regression
- Activation in shallow neural networks

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Logistic Regression](/en/terms/logistic-regression/)
- [Activation Function](/en/terms/activation-function/)
