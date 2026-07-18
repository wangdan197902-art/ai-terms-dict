---
title: "Tensor"
term_id: "tensor"
category: "basic_concepts"
subcategory: ""
tags: ["math", "data-structures", "pytorch"]
difficulty: 2
weight: 1
slug: "tensor"
aliases:
  - /en/terms/tensor/
date: "2026-07-18T10:17:39.734469Z"
lastmod: "2026-07-18T11:44:44.726719Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A multi-dimensional array that serves as the fundamental data structure for deep learning frameworks."
---

## Definition

In computer science and deep learning, a tensor is a mathematical object that generalizes scalars, vectors, and matrices to higher dimensions. It is characterized by its rank (number of dimensions) and shape (size along each dimension). Tensors allow efficient computation of linear algebra operations on GPUs and TPUs, forming the backbone of neural network data flow and parameter storage in frameworks like PyTorch and TensorFlow.

### Summary

A multi-dimensional array that serves as the fundamental data structure for deep learning frameworks.

## Key Concepts

- Rank
- Shape
- Dimensionality
- Broadcasting

## Use Cases

- Image processing (4D tensors)
- Neural network weights storage
- Batched data input

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix](/en/terms/matrix/)
- [Vector](/en/terms/vector/)
- [Deep Learning](/en/terms/deep-learning/)
- [NumPy](/en/terms/numpy/)
