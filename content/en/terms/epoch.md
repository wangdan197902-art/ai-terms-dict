---
title: Epoch
term_id: epoch
category: training_techniques
subcategory: ''
tags:
- training
- Neural Networks
- basics
difficulty: 2
weight: 1
slug: epoch
date: '2026-07-18T09:57:09.537599Z'
lastmod: '2026-07-18T11:44:44.670012Z'
draft: false
source: agnes_llm
status: published
language: en
description: One complete pass of the training dataset through the machine learning
  algorithm during model training.
---
## Definition

In machine learning, an epoch represents a single iteration over the entire training dataset. During each epoch, the model processes all training examples, updates its weights via backpropagation, and minimizes the loss function. Multiple epochs are typically required for the model to converge to optimal parameters. The number of epochs is a hyperparameter that must be tuned; too few may lead to underfitting, while too many can cause overfitting, where the model memorizes noise rather than learning general patterns.

### Summary

One complete pass of the training dataset through the machine learning algorithm during model training.

## Key Concepts

- Training Iteration
- Backpropagation
- Convergence
- Hyperparameter Tuning

## Use Cases

- Configuring neural network training loops
- Monitoring validation loss per cycle
- Implementing early stopping strategies

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Batch Size](/en/terms/batch-size/)
- [Iteration](/en/terms/iteration/)
- [Learning Rate](/en/terms/learning-rate/)
- [Overfitting](/en/terms/overfitting/)
