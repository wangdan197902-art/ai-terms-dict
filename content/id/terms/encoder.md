---
title: "Encoder"
term_id: "encoder"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Network Architecture", "Feature Engineering", "Transformers"]
difficulty: 3
weight: 1
slug: "encoder"
aliases:
  - /id/terms/encoder/
date: "2026-07-18T15:34:15.539809Z"
lastmod: "2026-07-18T16:38:07.413053Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Encoder adalah komponen jaringan saraf yang mengubah data input menjadi representasi yang terkompresi dan bermakna."
---

## Definition

Encoder memproses urutan atau struktur data mentah dan mengubahnya menjadi representasi ruang laten, sering disebut sebagai embedding atau kode. Encoder merupakan pusat arsitektur seperti Transformer dan Autoencoder.

### Summary

Encoder adalah komponen jaringan saraf yang mengubah data input menjadi representasi yang terkompresi dan bermakna.

## Key Concepts

- Ekstraksi Fitur
- Ruang Laten
- Pemrosesan Urutan
- Kompresi

## Use Cases

- Memproses teks input dalam model Transformer
- Mengompresi gambar dalam autoencoder untuk penghilangan derau
- Mengekstrak fitur sentimen dari ulasan

## Code Example

```python
import torch.nn as nn

class SimpleEncoder(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.fc = nn.Linear(input_dim, hidden_dim)
    
    def forward(self, x):
        return torch.relu(self.fc(x))
```

## Related Terms

- [Decoder (Dekoder)](/en/terms/decoder-dekoder/)
- [Transformer (Arsitektur Transformer)](/en/terms/transformer-arsitektur-transformer/)
- [Autoencoder (Autoencoder)](/en/terms/autoencoder-autoencoder/)
- [Latent Variable (Variabel laten)](/en/terms/latent-variable-variabel-laten/)
