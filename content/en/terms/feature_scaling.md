---
title: Feature scaling
term_id: feature_scaling
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- statistics
- Optimization
difficulty: 2
weight: 1
slug: feature_scaling
date: '2026-07-18T09:58:07.186353Z'
lastmod: '2026-07-18T11:44:44.672924Z'
draft: false
source: agnes_llm
status: published
language: en
description: The process of normalizing the range of independent variables or features
  of data to ensure uniformity in magnitude.
---
## Definition

Feature scaling standardizes the range of input variables to prevent features with larger magnitudes from dominating the learning process. Common methods include normalization (min-max scaling) and standardization (z-score scaling). This step is crucial for algorithms sensitive to the scale of input data, such as gradient descent-based optimizers, support vector machines, and k-nearest neighbors, ensuring faster convergence and more stable model training.

### Summary

The process of normalizing the range of independent variables or features of data to ensure uniformity in magnitude.

## Key Concepts

- Normalization
- Standardization
- Gradient descent
- Data preprocessing

## Use Cases

- Training neural networks
- K-means clustering
- Support Vector Machines (SVM)

## Code Example

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
```

## Related Terms

- [Min-Max Scaling](/en/terms/min-max-scaling/)
- [Z-score Normalization](/en/terms/z-score-normalization/)
- [Data preprocessing](/en/terms/data-preprocessing/)
- [Gradient Descent](/en/terms/gradient-descent/)
