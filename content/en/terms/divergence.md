---
title: "Divergence"
term_id: "divergence"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "stability", "debugging"]
difficulty: 2
weight: 1
slug: "divergence"
aliases:
  - /en/terms/divergence/
date: "2026-07-18T09:31:32.608891Z"
lastmod: "2026-07-18T11:44:44.595829Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Divergence refers to the failure of a machine learning algorithm's loss function to decrease during training, resulting in unstable or worsening performance."
---

## Definition

In the context of optimization, divergence occurs when the parameters of a model update in a way that causes the loss to increase rather than decrease, often leading to NaN values or infinite gradients. This is frequently caused by excessively high learning rates, poor weight initialization, or numerical instability in the computation graph. Detecting divergence early is crucial for debugging training pipelines, as it prevents wasted computational resources and ensures the model can converge to a meaningful solution. Techniques like gradient clipping or reducing the learning rate are common remedies.

### Summary

Divergence refers to the failure of a machine learning algorithm's loss function to decrease during training, resulting in unstable or worsening performance.

## Key Concepts

- Loss Explosion
- Learning Rate Sensitivity
- Gradient Instability
- Numerical Precision

## Use Cases

- Debugging training loops in deep learning frameworks
- Tuning hyperparameters for stable convergence
- Implementing gradient clipping strategies

## Related Terms

- [Vanishing Gradient](/en/terms/vanishing-gradient/)
- [Exploding Gradient](/en/terms/exploding-gradient/)
- [Convergence](/en/terms/convergence/)
- [Stability](/en/terms/stability/)
