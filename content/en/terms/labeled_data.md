---
title: Labeled data
term_id: labeled_data
category: basic_concepts
subcategory: ''
tags:
- data
- Supervised Learning
- fundamentals
difficulty: 1
weight: 1
slug: labeled_data
date: '2026-07-18T10:04:23.636077Z'
lastmod: '2026-07-18T11:44:44.690640Z'
draft: false
source: agnes_llm
status: published
language: en
description: Data where the correct output or target value is provided alongside the
  input features.
---
## Definition

Labeled data consists of input samples paired with corresponding ground truth labels, serving as the foundation for supervised machine learning. It allows algorithms to learn the mapping between inputs and outputs by minimizing prediction errors during training. High-quality labeled data is critical for model accuracy, but its creation often requires significant human effort and domain expertise to ensure correctness and consistency across the dataset.

### Summary

Data where the correct output or target value is provided alongside the input features.

## Key Concepts

- Supervised Learning
- Ground Truth
- Annotation
- Target Variable

## Use Cases

- Training image classifiers
- Building speech recognition systems
- Predictive modeling in finance

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data](/en/terms/unlabeled_data/)
- [supervised_learning](/en/terms/supervised_learning/)
- [data_annotation](/en/terms/data_annotation/)
- [training_set](/en/terms/training_set/)
