---
title: Instance-based learning
term_id: instance_based_learning
category: training_techniques
subcategory: ''
tags:
- algorithm
- Lazy Learning
- Classification
difficulty: 2
weight: 1
slug: instance_based_learning
date: '2026-07-18T10:02:49.698944Z'
lastmod: '2026-07-18T11:44:44.686068Z'
draft: false
source: agnes_llm
status: published
language: en
description: A lazy learning approach where predictions are made by comparing new
  inputs to stored training instances.
---
## Definition

Also known as memory-based learning, this technique does not build a generalized model during training. Instead, it stores the entire training dataset. When a prediction is needed, it finds the most similar instances (neighbors) in the stored data and uses their labels to determine the output. K-Nearest Neighbors (KNN) is the most common algorithm in this category.

### Summary

A lazy learning approach where predictions are made by comparing new inputs to stored training instances.

## Key Concepts

- Lazy learning
- Similarity metric
- K-Nearest Neighbors
- Memory-based

## Use Cases

- Recommendation systems
- Pattern recognition
- Small to medium datasets

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```

## Related Terms

- [KNN](/en/terms/knn/)
- [Similarity search](/en/terms/similarity-search/)
- [Lazy learning](/en/terms/lazy-learning/)
- [Kernel methods](/en/terms/kernel-methods/)
