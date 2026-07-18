---
title: "Evaluation of binary classifiers"
term_id: "evaluation_of_binary_classifiers"
category: "basic_concepts"
subcategory: ""
tags: ["metrics", "classification", "evaluation"]
difficulty: 2
weight: 1
slug: "evaluation_of_binary_classifiers"
aliases:
  - /en/terms/evaluation_of_binary_classifiers/
date: "2026-07-18T09:57:25.048465Z"
lastmod: "2026-07-18T11:44:44.670250Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "The process of assessing the performance of machine learning models that predict one of two possible outcomes."
---

## Definition

This field involves analyzing metrics such as accuracy, precision, recall, F1-score, and the Area Under the Receiver Operating Characteristic Curve (AUC-ROC). It helps determine how well a model distinguishes between positive and negative classes, particularly when class distributions are imbalanced. Proper evaluation is critical for deploying reliable predictive systems in high-stakes environments like medical diagnosis or fraud detection.

### Summary

The process of assessing the performance of machine learning models that predict one of two possible outcomes.

## Key Concepts

- Confusion Matrix
- Precision-Recall Tradeoff
- ROC Curve
- F1-Score

## Use Cases

- Medical disease screening
- Spam email filtering
- Credit risk assessment

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix](/en/terms/confusion_matrix/)
- [roc_auc](/en/terms/roc_auc/)
- [precision_recall](/en/terms/precision_recall/)
- [cross_validation](/en/terms/cross_validation/)
