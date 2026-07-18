---
title: "Batch Size"
term_id: "batch_size"
category: "training_techniques"
subcategory: ""
tags: ["hyperparameters", "optimization", "memory"]
difficulty: 2
weight: 1
slug: "batch_size"
aliases:
  - /en/terms/batch_size/
date: "2026-07-18T09:47:51.703269Z"
lastmod: "2026-07-18T11:44:44.646921Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "The number of training examples utilized in one iteration of the stochastic gradient descent algorithm."
---

## Definition

Batch size is a critical hyperparameter that determines how many samples are processed before the model's internal parameters are updated. A larger batch size provides a more accurate estimate of the gradient, leading to stable convergence but requiring more memory and potentially generalizing poorly. Conversely, smaller batch sizes introduce noise into the gradient estimation, which can help escape local minima but may result in noisier convergence paths and longer training times due to frequent updates.

### Summary

The number of training examples utilized in one iteration of the stochastic gradient descent algorithm.

## Key Concepts

- Gradient Estimation
- Memory Constraints
- Convergence Stability
- Hyperparameter Tuning

## Use Cases

- Tuning model convergence speed
- Managing GPU memory limits during training
- Improving generalization via noisy gradients

## Related Terms

- [learning_rate](/en/terms/learning_rate/)
- [stochastic_gradient_descent](/en/terms/stochastic_gradient_descent/)
- [mini_batch](/en/terms/mini_batch/)
- [memory_usage](/en/terms/memory_usage/)
