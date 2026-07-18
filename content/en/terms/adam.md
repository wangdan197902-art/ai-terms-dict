---
title: "Adam"
term_id: "adam"
category: "basic_concepts"
subcategory: ""
tags: ["Optimization", "Deep Learning", "Algorithms"]
difficulty: 3
weight: 1
slug: "adam"
aliases:
  - /en/terms/adam/
date: "2026-07-18T09:30:04.900910Z"
lastmod: "2026-07-18T11:44:44.592607Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "An optimization algorithm that computes adaptive learning rates for each parameter."
---

## Definition

Adam (Adaptive Moment Estimation) is a popular first-order gradient-based optimization algorithm used in training deep neural networks. It combines the advantages of two other extensions of stochastic gradient descent: AdaGrad, which works well with sparse gradients, and RMSProp, which works well in online and non-stationary settings. Adam maintains exponential moving averages of both the gradient and the squared gradient to adapt the learning rate for each weight individually.

### Summary

An optimization algorithm that computes adaptive learning rates for each parameter.

## Key Concepts

- Gradient Descent
- Learning Rate
- Momentum
- Variance Estimation

## Use Cases

- Deep Learning Training
- Computer Vision Models
- Natural Language Processing

## Code Example

```python
import torch.optim as optim
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

## Related Terms

- [SGD](/en/terms/sgd/)
- [RMSProp](/en/terms/rmsprop/)
- [Optimizer](/en/terms/optimizer/)
- [Backpropagation](/en/terms/backpropagation/)
