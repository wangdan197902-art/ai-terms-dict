---
title: "Perhatian Diri"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
aliases:
  - /id/terms/self_attention/
date: "2026-07-18T15:29:37.018551Z"
lastmod: "2026-07-18T16:38:07.402863Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Sebuah mekanisme yang memungkinkan jaringan saraf menimbang pentingnya bagian-bagian berbeda dari urutan input relatif satu sama lain."
---

## Definition

Perhatian diri memungkinkan model menangkap ketergantungan antara semua posisi dalam suatu urutan secara bersamaan, terlepas dari jaraknya. Dengan menghitung skor perhatian antara setiap pasangan token, mekanisme ini memungkinkan...

### Summary

Sebuah mekanisme yang memungkinkan jaringan saraf menimbang pentingnya bagian-bagian berbeda dari urutan input relatif satu sama lain.

## Key Concepts

- Query-Key-Value (Kueri-Kunci-Nilai)
- Skor Perhatian
- Pemberatan Kontekstual
- Pemrosesan Paralel

## Use Cases

- Terjemahan mesin
- Ringkasan teks
- Klasifikasi gambar melalui Transformer Visi

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer](/en/terms/transformer/)
- [Multi-Head Attention (Perhatian Multi-Kepala)](/en/terms/multi-head-attention-perhatian-multi-kepala/)
- [Embeddings (Penyematan)](/en/terms/embeddings-penyematan/)
- [Sequence Modeling (Pemodelan Urutan)](/en/terms/sequence-modeling-pemodelan-urutan/)
