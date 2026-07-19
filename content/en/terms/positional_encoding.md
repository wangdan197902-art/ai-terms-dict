---
title: Positional Encoding
term_id: positional_encoding
category: basic_concepts
subcategory: ''
tags:
- transformers
- NLP
- architecture
difficulty: 3
weight: 1
slug: positional_encoding
date: '2026-07-18T09:42:48.751671Z'
lastmod: '2026-07-18T11:44:44.629349Z'
draft: false
source: agnes_llm
status: published
language: en
description: A technique that injects information about the relative or absolute position
  of tokens in a sequence into transformer models.
---
## Definition

Since transformers process all tokens in parallel rather than sequentially like RNNs, they lack inherent knowledge of token order. Positional encoding adds specific vectors to input embeddings to preserve sequence information. Common methods include sinusoidal functions learned during training or learned embeddings. This allows the self-attention mechanism to weigh the importance of different tokens based on their position, enabling the model to understand syntax and context effectively.

### Summary

A technique that injects information about the relative or absolute position of tokens in a sequence into transformer models.

## Key Concepts

- Sequence Order
- Self-Attention
- Sinusoidal Functions
- Token Embeddings

## Use Cases

- Machine Translation
- Text Summarization
- Language Modeling

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Transformer Architecture](/en/terms/transformer-architecture/)
- [Embedding](/en/terms/embedding/)
- [Attention Mechanism](/en/terms/attention-mechanism/)
- [RoPE](/en/terms/rope/)
