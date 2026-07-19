---
title: Leave-one-out cross-validation
term_id: leave_one_out_cross_validation
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- evaluation
- statistics
difficulty: 3
weight: 1
slug: leave_one_out_cross_validation
date: '2026-07-18T10:04:58.088973Z'
lastmod: '2026-07-18T11:44:44.691888Z'
draft: false
source: agnes_llm
status: published
language: en
description: A rigorous resampling technique where the model is trained on all but
  one sample and tested on that single held-out sample, repeated for every data point.
---
## Definition

Leave-one-out cross-validation (LOOCV) is a specific case of k-fold cross-validation where k equals the number of samples in the dataset. It provides a nearly unbiased estimate of model performance because each observation serves as the test set exactly once. While computationally expensive due to the need to train the model n times, it is highly effective for small datasets where maximizing training data usage is critical for robust evaluation.

### Summary

A rigorous resampling technique where the model is trained on all but one sample and tested on that single held-out sample, repeated for every data point.

## Key Concepts

- Resampling
- Model Evaluation
- Bias-Variance Tradeoff
- Computational Cost

## Use Cases

- Evaluating models on small medical datasets
- Hyperparameter tuning when data is scarce
- Comparing algorithm performance rigorously

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation](/en/terms/k-fold-cross-validation/)
- [train_test_split](/en/terms/train_test_split/)
- [bootstrap](/en/terms/bootstrap/)
- [cross_validation_score](/en/terms/cross_validation_score/)
