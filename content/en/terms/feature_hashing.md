---
title: Feature hashing
term_id: feature_hashing
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- Text Mining
- Optimization
difficulty: 3
weight: 1
slug: feature_hashing
date: '2026-07-18T09:58:07.186335Z'
lastmod: '2026-07-18T11:44:44.672550Z'
draft: false
source: agnes_llm
status: published
language: en
description: A technique that maps high-dimensional sparse features to a fixed-size
  vector using a hash function.
---
## Definition

Feature hashing, also known as the hashing trick, allows machine learning models to handle large, sparse feature spaces without maintaining an explicit mapping between features and indices. By applying a hash function to each feature, it deterministically assigns them to a fixed number of buckets. This reduces memory usage and eliminates the need for preprocessing steps like vocabulary building, making it highly efficient for text classification and recommendation systems with massive input dimensions.

### Summary

A technique that maps high-dimensional sparse features to a fixed-size vector using a hash function.

## Key Concepts

- Hash function
- Sparse vectors
- Dimensionality reduction
- Memory efficiency

## Use Cases

- Text classification with large vocabularies
- Recommendation systems with huge item sets
- Real-time streaming data processing

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-hot encoding](/en/terms/one-hot-encoding/)
- [Bag of Words](/en/terms/bag-of-words/)
- [Dimensionality reduction](/en/terms/dimensionality-reduction/)
- [Sparse matrix](/en/terms/sparse-matrix/)
