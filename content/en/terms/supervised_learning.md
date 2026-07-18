---
title: "Supervised Learning"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /en/terms/supervised_learning/
date: "2026-07-18T09:42:48.759018Z"
lastmod: "2026-07-18T11:44:44.633794Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A machine learning paradigm where a model learns to map inputs to outputs based on labeled training examples."
---

## Definition

In supervised learning, the algorithm is trained on a labeled dataset, meaning each input example is paired with the correct output. The goal is for the model to learn the underlying relationship between inputs and outputs so it can accurately predict labels for unseen data. Common tasks include classification, where discrete categories are predicted, and regression, where continuous values are estimated.

### Summary

A machine learning paradigm where a model learns to map inputs to outputs based on labeled training examples.

## Key Concepts

- Labeled Data
- Input-Output Mapping
- Classification
- Regression

## Use Cases

- Spam email detection
- House price prediction
- Image recognition

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning](/en/terms/unsupervised-learning/)
- [Training Set](/en/terms/training-set/)
- [Validation Set](/en/terms/validation-set/)
- [Model Accuracy](/en/terms/model-accuracy/)
