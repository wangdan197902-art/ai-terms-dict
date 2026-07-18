---
title: "Cross-validation"
term_id: "cross_validation"
category: "training_techniques"
subcategory: ""
tags: ["evaluation", "machine-learning", "statistics"]
difficulty: 2
weight: 1
slug: "cross_validation"
aliases:
  - /en/terms/cross_validation/
date: "2026-07-18T09:52:18.249992Z"
lastmod: "2026-07-18T11:44:44.658106Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A resampling procedure used to evaluate machine learning models on a limited data sample by partitioning data into subsets for training and testing."
---

## Definition

Cross-validation is a statistical method used to estimate the skill of machine learning models. The most common form is k-fold cross-validation, where the data is split into k equal parts. The model is trained on k-1 folds and validated on the remaining fold, repeating this process k times so each fold serves as the validation set once. This approach provides a more robust estimate of model performance than a single train-test split, helping to detect overfitting and ensuring the model generalizes well to unseen data.

### Summary

A resampling procedure used to evaluate machine learning models on a limited data sample by partitioning data into subsets for training and testing.

## Key Concepts

- K-Fold Split
- Model Generalization
- Overfitting Detection
- Performance Estimation

## Use Cases

- Hyperparameter tuning
- Comparing different algorithms
- Validating model stability on small datasets

## Code Example

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X, y, cv=5)
```

## Related Terms

- [Train-Test Split](/en/terms/train-test-split/)
- [Leave-One-Out](/en/terms/leave-one-out/)
- [Bootstrap](/en/terms/bootstrap/)
