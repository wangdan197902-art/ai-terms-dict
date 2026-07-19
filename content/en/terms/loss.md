---
title: Loss
term_id: loss
category: training_techniques
subcategory: ''
tags:
- training
- Optimization
difficulty: 3
weight: 1
slug: loss
date: '2026-07-18T09:33:48.381155Z'
lastmod: '2026-07-18T11:44:44.601868Z'
draft: false
source: agnes_llm
status: published
language: en
description: A numerical value that quantifies the error between a model's predictions
  and the actual target values.
---
## Definition

Loss functions, also known as cost functions, measure how well a machine learning model's predictions match the ground truth during training. The goal of the optimization algorithm is to minimize this loss value. Different tasks require different loss functions; for example, Mean Squared Error (MSE) is common for regression, while Cross-Entropy is standard for classification. Monitoring loss helps diagnose issues like underfitting or overfitting.

### Summary

A numerical value that quantifies the error between a model's predictions and the actual target values.

## Key Concepts

- Cost Function
- Optimization
- Gradient Descent
- Error Metric

## Use Cases

- Training image classifiers
- Optimizing regression models
- Evaluating model convergence

## Code Example

```python
import torch.nn as nn
criterion = nn.CrossEntropyLoss()
loss = criterion(outputs, targets)
```

## Related Terms

- [Accuracy](/en/terms/accuracy/)
- [Gradient Descent](/en/terms/gradient-descent/)
- [Cross-Entropy](/en/terms/cross-entropy/)
- [Overfitting](/en/terms/overfitting/)
