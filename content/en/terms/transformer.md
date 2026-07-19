---
title: Transformer
term_id: transformer
category: basic_concepts
subcategory: ''
tags:
- architecture
- NLP
- attention
difficulty: 4
weight: 1
slug: transformer
date: '2026-07-18T09:37:37.820415Z'
lastmod: '2026-07-18T11:44:44.612156Z'
draft: false
source: agnes_llm
status: published
language: en
description: A deep learning architecture based on self-attention mechanisms that
  processes sequential data in parallel rather than sequentially.
---
## Definition

Introduced in the 'Attention Is All You Need' paper, the Transformer architecture revolutionized natural language processing and beyond. It uses multi-head self-attention to weigh the significance of different parts of the input data simultaneously, enabling efficient parallelization during training. This structure allows models to capture long-range dependencies effectively, forming the backbone of modern large language models like BERT and GPT series.

### Summary

A deep learning architecture based on self-attention mechanisms that processes sequential data in parallel rather than sequentially.

## Key Concepts

- Self-Attention
- Multi-Head Attention
- Positional Encoding
- Encoder-Decoder Structure

## Use Cases

- Machine translation
- Text generation
- Image recognition (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism](/en/terms/attention_mechanism/)
- [bert](/en/terms/bert/)
- [gpt](/en/terms/gpt/)
- [self_attention](/en/terms/self_attention/)
