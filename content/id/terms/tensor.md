---
title: Tensor
term_id: tensor
category: basic_concepts
subcategory: ''
tags:
- math
- Data Structures
- pytorch
difficulty: 2
weight: 1
slug: tensor
date: '2026-07-18T16:10:44.135690Z'
lastmod: '2026-07-18T16:38:07.513222Z'
draft: false
source: agnes_llm
status: published
language: id
description: Array multidimensi yang berfungsi sebagai struktur data fundamental untuk
  kerangka kerja pembelajaran mendalam.
---
## Definition

Dalam ilmu komputer dan pembelajaran mendalam, tensor adalah objek matematika yang menggeneralisasi skalar, vektor, dan matriks ke dimensi yang lebih tinggi. Tensor ini dicirikan oleh rank-nya (jumlah dimensi) dan bentuknya.

### Summary

Array multidimensi yang berfungsi sebagai struktur data fundamental untuk kerangka kerja pembelajaran mendalam.

## Key Concepts

- Rank
- Bentuk (Shape)
- Dimensi
- Broadcasting

## Use Cases

- Pemrosesan gambar (tensor 4D)
- Penyimpanan bobot jaringan saraf
- Input data batch

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix (Matriks)](/en/terms/matrix-matriks/)
- [Vector (Vektor)](/en/terms/vector-vektor/)
- [Deep Learning (Pembelajaran Mendalam)](/en/terms/deep-learning-pembelajaran-mendalam/)
- [NumPy](/en/terms/numpy/)
