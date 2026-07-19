---
title: Softmax
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T15:36:17.841108Z'
lastmod: '2026-07-18T16:38:07.419529Z'
draft: false
source: agnes_llm
status: published
language: id
description: Fungsi matematika yang mengubah vektor skor bernilai riil menjadi distribusi
  probabilitas.
---
## Definition

Softmax banyak digunakan pada lapisan output jaringan saraf untuk tugas klasifikasi multi-kelas. Fungsi ini mengambil vektor logit mentah dan menormalisasinya sehingga setiap elemen mewakili probabilitas.

### Summary

Fungsi matematika yang mengubah vektor skor bernilai riil menjadi distribusi probabilitas.

## Key Concepts

- Distribusi Probabilitas
- Logit
- Normalisasi
- Klasifikasi Multi-kelas

## Use Cases

- Lapisan output klasifikasi gambar
- Prediksi token model bahasa
- Kategorisasi multi-label

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (Fungsi untuk menemukan indeks nilai maksimum)](/en/terms/argmax-fungsi-untuk-menemukan-indeks-nilai-maksimum/)
- [Cross-Entropy Loss (Fungsi kerugian untuk klasifikasi)](/en/terms/cross-entropy-loss-fungsi-kerugian-untuk-klasifikasi/)
- [Logits (Skor mentah sebelum aktivasi)](/en/terms/logits-skor-mentah-sebelum-aktivasi/)
- [Neural Network (Jaringan Saraf)](/en/terms/neural-network-jaringan-saraf/)
