---
title: "Supervised"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
date: "2026-07-18T09:36:52.558080Z"
lastmod: "2026-07-18T11:44:44.610378Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A machine learning paradigm where models are trained on labeled input-output pairs."
---
## Definition

Supervised learning involves feeding an algorithm with data that includes both inputs and correct answers (labels). The model learns to map inputs to outputs by minimizing prediction errors. This technique is foundational for classification and regression tasks, requiring high-quality labeled datasets for effective training.

### Summary

A machine learning paradigm where models are trained on labeled input-output pairs.

## Key Concepts

- Labeled data
- Mapping
- Loss minimization

## Use Cases

- Image classification
- Spam detection
- Price prediction

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised](/en/terms/unsupervised/)
- [Label](/en/terms/label/)
- [Regression](/en/terms/regression/)
