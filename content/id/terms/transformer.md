---
title: "Transformer"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /id/terms/transformer/
date: "2026-07-18T15:30:34.302239Z"
lastmod: "2026-07-18T16:38:07.405253Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Arsitektur pembelajaran mendalam berbasis mekanisme perhatian-diri (self-attention) yang memproses data sekuensial secara paralel, bukan sekuensial."
---

## Definition

Diperkenalkan dalam makalah 'Attention Is All You Need', arsitektur Transformer merevolusi pemrosesan bahasa alami dan bidang lainnya. Arsitektur ini menggunakan perhatian-diri multi-kepala untuk menimbang signifikansi dari

### Summary

Arsitektur pembelajaran mendalam berbasis mekanisme perhatian-diri (self-attention) yang memproses data sekuensial secara paralel, bukan sekuensial.

## Key Concepts

- Perhatian-Diri (Self-Attention)
- Perhatian Multi-Kepala (Multi-Head Attention)
- Enkoding Posisi (Positional Encoding)
- Struktur Encoder-Decoder

## Use Cases

- Terjemahan mesin
- Pembuatan teks
- Pengenalan gambar (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (mekanisme perhatian)](/en/terms/attention_mechanism-mekanisme-perhatian/)
- [bert (Bidirectional Encoder Representations from Transformers)](/en/terms/bert-bidirectional-encoder-representations-from-transformers/)
- [gpt (Generative Pre-trained Transformer)](/en/terms/gpt-generative-pre-trained-transformer/)
- [self_attention (perhatian-diri)](/en/terms/self_attention-perhatian-diri/)
