---
title: Random feature
term_id: random_feature
category: basic_concepts
subcategory: ''
tags:
- Kernel Methods
- Feature Engineering
- Optimization
difficulty: 3
weight: 1
slug: random_feature
date: '2026-07-18T10:13:36.396610Z'
lastmod: '2026-07-18T11:44:44.715922Z'
draft: false
source: agnes_llm
status: published
language: en
description: A technique that maps input data into a higher-dimensional space using
  random projections to approximate kernel methods efficiently.
---
## Definition

Random feature maps transform inputs into a new space where linear models can approximate non-linear kernel functions. This approach, often associated with the Nystrom method or Fourier features, allows for scalable kernel regression and classification. By avoiding the explicit computation of large kernel matrices, it reduces computational complexity from quadratic to linear in the number of samples, making it suitable for large-scale datasets.

### Summary

A technique that maps input data into a higher-dimensional space using random projections to approximate kernel methods efficiently.

## Key Concepts

- Kernel approximation
- Feature mapping
- Computational efficiency
- Linearization

## Use Cases

- Large-scale kernel regression
- Neural tangent kernel approximation
- Scalable Gaussian processes

## Code Example

```python
import numpy as np
from sklearn.kernel_approximation import RBFSampler
X = np.random.rand(100, 5)
transformer = RBFSampler(gamma=1, n_components=50, random_state=42)
X_transformed = transformer.fit_transform(X)
```

## Related Terms

- [Kernel trick](/en/terms/kernel-trick/)
- [Fourier features](/en/terms/fourier-features/)
- [Nystrom method](/en/terms/nystrom-method/)
- [Dimensionality reduction](/en/terms/dimensionality-reduction/)
