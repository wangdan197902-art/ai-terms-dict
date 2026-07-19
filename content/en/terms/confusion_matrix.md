---
title: Confusion matrix
term_id: confusion_matrix
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Classification
- metrics
difficulty: 2
weight: 1
slug: confusion_matrix
date: '2026-07-18T09:51:40.829675Z'
lastmod: '2026-07-18T11:44:44.654916Z'
draft: false
source: agnes_llm
status: published
language: en
description: A table used to describe the performance of a classification model on
  a set of test data.
---
## Definition

A confusion matrix is a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one. It shows the counts of true positive, true negative, false positive, and false negative predictions. This structure helps in understanding where the model is making errors, providing insights beyond simple accuracy metrics, especially in imbalanced datasets. It serves as the foundation for calculating precision, recall, and F1 scores.

### Summary

A table used to describe the performance of a classification model on a set of test data.

## Key Concepts

- True Positives
- False Negatives
- Precision
- Recall

## Use Cases

- Evaluating binary classifiers
- Analyzing multi-class classification performance
- Debugging model bias in imbalanced datasets

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision](/en/terms/precision/)
- [recall](/en/terms/recall/)
- [F1 score](/en/terms/f1-score/)
- [ROC curve](/en/terms/roc-curve/)
