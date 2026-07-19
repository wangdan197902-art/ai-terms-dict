---
title: Overfitting
term_id: overfitting
category: training_techniques
subcategory: ''
tags:
- Model Evaluation
- Training Dynamics
- generalization
difficulty: 2
weight: 1
slug: overfitting
date: '2026-07-18T09:41:54.086126Z'
lastmod: '2026-07-18T11:44:44.628980Z'
draft: false
source: agnes_llm
status: published
language: en
description: A modeling error where a machine learning algorithm captures noise instead
  of the underlying signal, harming generalization.
---
## Definition

Overfitting occurs when a model learns the training data too well, including its random noise and outliers, resulting in excellent performance on training data but poor performance on new, unseen test data. This happens because the model becomes overly complex relative to the amount of training data available. Techniques like regularization, dropout, early stopping, and cross-validation are commonly employed to mitigate overfitting and improve the model's ability to generalize.

### Summary

A modeling error where a machine learning algorithm captures noise instead of the underlying signal, harming generalization.

## Key Concepts

- High variance
- Poor generalization
- Training vs test error gap
- Model complexity

## Use Cases

- Diagnosing model performance issues
- Selecting regularization strength
- Determining optimal model depth

## Related Terms

- [underfitting](/en/terms/underfitting/)
- [regularization](/en/terms/regularization/)
- [cross_validation](/en/terms/cross_validation/)
- [bias_variance_tradeoff](/en/terms/bias_variance_tradeoff/)
