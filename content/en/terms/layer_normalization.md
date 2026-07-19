---
title: Layer Normalization
term_id: layer_normalization
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Optimization
- architecture
difficulty: 3
weight: 1
slug: layer_normalization
date: '2026-07-18T10:04:23.636112Z'
lastmod: '2026-07-18T11:44:44.690954Z'
draft: false
source: agnes_llm
status: published
language: en
description: A technique that normalizes the activations of a neural network layer
  across the feature dimension for each individual sample.
---
## Definition

Layer Normalization stabilizes training by reducing internal covariate shift, particularly effective in recurrent and transformer architectures. Unlike Batch Normalization, which depends on batch statistics, Layer Normalization computes mean and variance across all features of a single training example. This makes it robust to small batch sizes and sequential data processing, leading to faster convergence and improved model stability.

### Summary

A technique that normalizes the activations of a neural network layer across the feature dimension for each individual sample.

## Key Concepts

- Normalization
- Internal Covariate Shift
- Transformer Models
- RNNs

## Use Cases

- Training Transformer models like BERT
- Stabilizing RNN/LSTM training
- Deep learning with small batch sizes

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization](/en/terms/batch_normalization/)
- [transformer](/en/terms/transformer/)
- [normalization](/en/terms/normalization/)
- [deep_learning](/en/terms/deep_learning/)
