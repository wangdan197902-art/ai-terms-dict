---
title: "Lazy learning"
term_id: "lazy_learning"
category: "training_techniques"
subcategory: ""
tags: ["algorithms", "training_methods", "machine_learning"]
difficulty: 2
weight: 1
slug: "lazy_learning"
aliases:
  - /en/terms/lazy_learning/
date: "2026-07-18T10:04:23.636115Z"
lastmod: "2026-07-18T11:44:44.691205Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A learning approach that delays generalization until classification time, storing training instances rather than building an explicit model."
---

## Definition

Lazy learners, such as k-Nearest Neighbors (k-NN), memorize the entire training dataset and perform computations only when making predictions. This contrasts with eager learning, which builds a generalized model upfront. While lazy learning can adapt quickly to new data without retraining, it suffers from high computational costs during inference and large memory requirements due to storing all training examples.

### Summary

A learning approach that delays generalization until classification time, storing training instances rather than building an explicit model.

## Key Concepts

- Instance-Based Learning
- k-Nearest Neighbors
- Inference Cost
- Generalization

## Use Cases

- Recommendation systems
- Pattern recognition in small datasets
- Prototyping predictive models

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)
```

## Related Terms

- [instance_based_learning](/en/terms/instance_based_learning/)
- [knn](/en/terms/knn/)
- [eager_learning](/en/terms/eager_learning/)
- [generalization](/en/terms/generalization/)
