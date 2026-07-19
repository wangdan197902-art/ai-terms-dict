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
date: '2026-07-18T15:27:35.896171Z'
lastmod: '2026-07-18T16:38:07.397948Z'
draft: false
source: agnes_llm
status: published
language: id
description: Mekanisme dalam model transformer yang memungkinkan model memperhatikan
  informasi dari berbagai subruang representasi secara bersamaan.
---
## Definition

Multi-Head Attention memperluas mekanisme perhatian standar dengan menjalankannya beberapa kali secara paralel menggunakan proyeksi linear yang berbeda. Hal ini memungkinkan model untuk secara bersama-sama memperhatikan informasi dari berbagai perspektif.

### Summary

Mekanisme dalam model transformer yang memungkinkan model memperhatikan informasi dari berbagai subruang representasi secara bersamaan.

## Key Concepts

- Self-Attention (Perhatian Diri)
- Proyeksi Linear
- Penggabungan (Concatenation)

## Use Cases

- Pemrosesan Bahasa Alamiah (NLP)
- Terjemahan Mesin
- Klasifikasi Gambar dengan Vision Transformers

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

- [Scaled Dot-Product Attention (Perhatian Hasil Kali Titik Skala)](/en/terms/scaled-dot-product-attention-perhatian-hasil-kali-titik-skala/)
- [Transformer (Transformator)](/en/terms/transformer-transformator/)
- [Embedding (Penyematan)](/en/terms/embedding-penyematan/)
