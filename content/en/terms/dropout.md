---
title: "Dropout"
term_id: "dropout"
category: "basic_concepts"
subcategory: ""
tags: ["Deep Learning", "Regularization", "Model Training"]
difficulty: 3
weight: 1
slug: "dropout"
date: "2026-07-18T09:40:59.277019Z"
lastmod: "2026-07-18T11:44:44.623894Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Dropout is a regularization technique that randomly ignores neurons during training to prevent overfitting."
---
## Definition

In neural networks, dropout prevents overfitting by temporarily removing a random subset of neurons during each training step. This forces the network to learn robust features that are useful in conjunction with many other random subsets of neurons, rather than relying on specific local patterns. During inference, all neurons are used, but their outputs are scaled to account for the increased activity compared to training time.

### Summary

Dropout is a regularization technique that randomly ignores neurons during training to prevent overfitting.

## Key Concepts

- Regularization
- Overfitting Prevention
- Neural Networks
- Random Suppression

## Use Cases

- Training deep feedforward neural networks
- Improving generalization in large language models
- Reducing computational dependency on specific neuron pathways

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(100, 50),
    nn.Dropout(0.5),
    nn.ReLU(),
    nn.Linear(50, 10)
)
```

## Related Terms

- [L2 Regularization](/en/terms/l2-regularization/)
- [Batch Normalization](/en/terms/batch-normalization/)
- [Overfitting](/en/terms/overfitting/)
- [Generalization](/en/terms/generalization/)
