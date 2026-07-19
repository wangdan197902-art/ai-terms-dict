---
title: Learning Rate
term_id: learning_rate
category: training_techniques
subcategory: ''
tags:
- training
- Optimization
- hyperparameters
difficulty: 3
weight: 1
slug: learning_rate
date: '2026-07-18T09:41:26.871051Z'
lastmod: '2026-07-18T11:44:44.626992Z'
draft: false
source: agnes_llm
status: published
language: en
description: A hyperparameter that controls the step size during model optimization
  to minimize the loss function.
---
## Definition

The learning rate determines how much the model's weights are updated relative to the calculated gradient during each training iteration. A rate that is too high may cause the model to overshoot optimal solutions, while a rate that is too low leads to slow convergence or getting stuck in local minima. Tuning this parameter is essential for efficient training, often involving schedulers that decay the rate over time to fine-tune the model near the end of the training process.

### Summary

A hyperparameter that controls the step size during model optimization to minimize the loss function.

## Key Concepts

- Gradient Descent
- Hyperparameter Tuning
- Convergence
- Optimizer

## Use Cases

- Neural network training
- Deep learning model optimization
- Reinforcement learning policy updates

## Code Example

```python
import torch.optim as optim
model = MyModel()
optimizer = optim.SGD(model.parameters(), lr=0.01)
```

## Related Terms

- [gradient_descent](/en/terms/gradient_descent/)
- [optimizer](/en/terms/optimizer/)
- [hyperparameter](/en/terms/hyperparameter/)
- [convergence](/en/terms/convergence/)
