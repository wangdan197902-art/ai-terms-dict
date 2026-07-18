---
title: "Encoding Posisi"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /id/terms/positional_encoding/
date: "2026-07-18T15:35:38.270781Z"
lastmod: "2026-07-18T16:38:07.417321Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Sebuah teknik yang menyuntikkan informasi mengenai posisi relatif atau absolut token dalam sebuah urutan ke dalam model transformer."
---

## Definition

Karena transformer memproses semua token secara paralel daripada secara berurutan seperti RNN, model ini tidak memiliki pengetahuan bawaan tentang urutan token. Encoding posisi menambahkan vektor spesifik ke embedding input untuk memberikan konteks urutan kepada model.

### Summary

Sebuah teknik yang menyuntikkan informasi mengenai posisi relatif atau absolut token dalam sebuah urutan ke dalam model transformer.

## Key Concepts

- Urutan Sekuens
- Perhatian Diri (Self-Attention)
- Fungsi Sinusoidal
- Embedding Token

## Use Cases

- Terjemahan Mesin
- Ringkasan Teks
- Pemodelan Bahasa

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

- [Arsitektur Transformer (Struktur dasar model yang menggunakan mekanisme perhatian)](/en/terms/arsitektur-transformer-struktur-dasar-model-yang-menggunakan-mekanisme-perhatian/)
- [Embedding (Proses mengubah kata menjadi vektor numerik)](/en/terms/embedding-proses-mengubah-kata-menjadi-vektor-numerik/)
- [Mekanisme Perhatian (Cara model memfokuskan pada bagian tertentu dari input)](/en/terms/mekanisme-perhatian-cara-model-memfokuskan-pada-bagian-tertentu-dari-input/)
- [RoPE (Relative Positional Encoding, metode encoding posisi relatif)](/en/terms/rope-relative-positional-encoding-metode-encoding-posisi-relatif/)
