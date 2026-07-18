---
title: "Tanh"
term_id: "tanh"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "mathematics"]
difficulty: 2
weight: 1
slug: "tanh"
aliases:
  - /en/terms/tanh/
date: "2026-07-18T10:17:26.261612Z"
lastmod: "2026-07-18T11:44:44.726373Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Tanh, or hyperbolic tangent, is an activation function that maps input values to a range between -1 and 1."
---

## Definition

The hyperbolic tangent (Tanh) function is a non-linear activation function commonly used in neural networks. It squashes input values into the interval (-1, 1), providing zero-centered outputs which can help mitigate the vanishing gradient problem compared to sigmoid functions. Tanh is differentiable everywhere, making it suitable for backpropagation. It is frequently used in recurrent neural networks (RNNs) and LSTM cells to regulate information flow within the network architecture.

### Summary

Tanh, or hyperbolic tangent, is an activation function that maps input values to a range between -1 and 1.

## Key Concepts

- Activation function
- Non-linearity
- Zero-centered output
- Backpropagation

## Use Cases

- Recurrent neural networks
- LSTM cell gates
- Hidden layers in MLPs

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid](/en/terms/sigmoid/)
- [relu](/en/terms/relu/)
- [neural_networks](/en/terms/neural_networks/)
