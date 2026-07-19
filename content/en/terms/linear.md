---
title: "Linear"
term_id: "linear"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Foundations"]
difficulty: 2
weight: 1
slug: "linear"
date: "2026-07-18T09:33:34.785720Z"
lastmod: "2026-07-18T11:44:44.601147Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Describes operations or relationships where output is directly proportional to input, forming the basis of affine transformations in neural layers."
---
## Definition

Linear operations involve multiplication and addition without non-linear activations. In neural networks, linear layers (or dense layers) apply a weight matrix transformation to input vectors. While linear alone cannot model complex patterns, they are crucial components combined with non-linear activation functions to create universal approximators. Understanding linearity is key to grasping how information flows and transforms through network layers.

### Summary

Describes operations or relationships where output is directly proportional to input, forming the basis of affine transformations in neural layers.

## Key Concepts

- Weight Matrix
- Affine Transformation
- Dot Product
- Superposition

## Use Cases

- Feature Projection
- Logistic Regression
- Attention Mechanisms

## Code Example

```python
import torch.nn as nn
layer = nn.Linear(10, 5)
output = layer(input_tensor)
```

## Related Terms

- [Activation Function](/en/terms/activation-function/)
- [Dense Layer](/en/terms/dense-layer/)
- [Matrix Multiplication](/en/terms/matrix-multiplication/)
