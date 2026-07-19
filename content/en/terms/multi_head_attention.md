---
title: Multi-Head Attention
term_id: multi_head_attention
category: basic_concepts
subcategory: ''
tags:
- transformer
- NLP
- Deep Learning
difficulty: 4
weight: 1
slug: multi_head_attention
date: '2026-07-18T09:34:16.089546Z'
lastmod: '2026-07-18T11:44:44.603099Z'
draft: false
source: agnes_llm
status: published
language: en
description: A mechanism in transformer models that allows the model to attend to
  information from different representation subspaces simultaneously.
---
## Definition

Multi-Head Attention extends the standard attention mechanism by running it multiple times in parallel with different learned linear projections. This enables the model to jointly attend to information from different positional subspaces at different positions. By capturing diverse relationships within the input sequence, such as syntactic and semantic dependencies, it significantly enhances the model's ability to understand context. It is a foundational component of modern Large Language Models (LLMs) and vision transformers, providing robust feature extraction capabilities.

### Summary

A mechanism in transformer models that allows the model to attend to information from different representation subspaces simultaneously.

## Key Concepts

- Self-Attention
- Linear Projections
- Concatenation

## Use Cases

- Natural Language Processing (NLP)
- Machine Translation
- Image Classification with Vision Transformers

## Code Example

```python
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        # Simplified forward pass logic
        pass
```

## Related Terms

- [Scaled Dot-Product Attention](/en/terms/scaled-dot-product-attention/)
- [Transformer](/en/terms/transformer/)
- [Embedding](/en/terms/embedding/)
