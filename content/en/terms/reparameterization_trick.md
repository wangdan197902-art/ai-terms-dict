---
title: Reparameterization trick
term_id: reparameterization_trick
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- Probabilistic Models
- Optimization
difficulty: 4
weight: 1
slug: reparameterization_trick
date: '2026-07-18T10:14:07.773912Z'
lastmod: '2026-07-18T11:44:44.717264Z'
draft: false
source: agnes_llm
status: published
language: en
description: A technique that separates stochastic variables from learnable parameters
  to enable gradient-based optimization in variational inference.
---
## Definition

The reparameterization trick is a fundamental method used in variational autoencoders and other probabilistic models. It allows gradients to flow through stochastic nodes by expressing a random variable z as a differentiable function of distribution parameters and an independent noise variable epsilon. This enables the use of backpropagation to optimize the expected log-likelihood, making training of latent variable models efficient and stable via Monte Carlo estimation.

### Summary

A technique that separates stochastic variables from learnable parameters to enable gradient-based optimization in variational inference.

## Key Concepts

- Variational Inference
- Gradient Estimation
- Stochastic Nodes
- Differentiable Simulation

## Use Cases

- Training Variational Autoencoders (VAEs)
- Bayesian Neural Networks
- Probabilistic Graphical Models

## Code Example

```python
import torch
epsilon = torch.randn(100, 10)
mu = torch.zeros(100, 10)
sigma = torch.ones(100, 10)
z = mu + sigma * epsilon  # Reparameterized sampling
```

## Related Terms

- [ELBO](/en/terms/elbo/)
- [Latent Variables](/en/terms/latent-variables/)
- [Backpropagation](/en/terms/backpropagation/)
- [Monte Carlo Estimation](/en/terms/monte-carlo-estimation/)
