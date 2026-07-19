---
title: "Self-Attention"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T09:36:45.467584Z"
lastmod: "2026-07-18T11:44:44.609144Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A mechanism allowing a neural network to weigh the importance of different parts of the input sequence relative to each other."
---
## Definition

Self-attention enables models to capture dependencies between all positions in a sequence simultaneously, regardless of distance. By computing attention scores between every pair of tokens, it allows the network to dynamically focus on relevant context, forming the foundational layer of Transformer architectures used in modern natural language processing and computer vision tasks.

### Summary

A mechanism allowing a neural network to weigh the importance of different parts of the input sequence relative to each other.

## Key Concepts

- Query-Key-Value
- Attention Scores
- Contextual Weighting
- Parallel Processing

## Use Cases

- Machine translation
- Text summarization
- Image classification via Vision Transformers

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer](/en/terms/transformer/)
- [Multi-Head Attention](/en/terms/multi-head-attention/)
- [Embeddings](/en/terms/embeddings/)
- [Sequence Modeling](/en/terms/sequence-modeling/)
