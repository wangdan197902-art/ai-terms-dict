---
title: "Regularization"
term_id: "regularization"
category: "basic_concepts"
subcategory: ""
tags: ["ML Basics", "Optimization", "Statistics"]
difficulty: 2
weight: 1
slug: "regularization"
aliases:
  - /en/terms/regularization/
date: "2026-07-18T10:13:50.501119Z"
lastmod: "2026-07-18T11:44:44.716722Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A set of techniques used during training to prevent overfitting by adding penalties to the loss function or constraining model complexity."
---

## Definition

Regularization is a crucial concept in machine learning designed to reduce generalization error without significantly increasing training error. It works by discouraging models from learning overly complex patterns that fit noise in the training data rather than the underlying signal. Common methods include L1 (Lasso) and L2 (Ridge) regularization, dropout in neural networks, and early stopping. These techniques help ensure that the model performs well on unseen data by maintaining a balance between bias and variance.

### Summary

A set of techniques used during training to prevent overfitting by adding penalties to the loss function or constraining model complexity.

## Key Concepts

- Overfitting
- Bias-variance tradeoff
- L1/L2 penalty
- Dropout

## Use Cases

- Training deep neural networks
- Linear regression models
- Preventing memorization in small datasets

## Code Example

```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)
```

## Related Terms

- [Overfitting](/en/terms/overfitting/)
- [Underfitting](/en/terms/underfitting/)
- [Cross-validation](/en/terms/cross-validation/)
- [Hyperparameter tuning](/en/terms/hyperparameter-tuning/)
