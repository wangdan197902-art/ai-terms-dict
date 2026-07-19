---
title: ReLU
term_id: relu
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Activation Functions
- Deep Learning
difficulty: 3
weight: 1
slug: relu
date: '2026-07-18T15:35:51.008049Z'
lastmod: '2026-07-18T16:38:07.418253Z'
draft: false
source: agnes_llm
status: published
language: id
description: Rectified Linear Unit adalah fungsi aktivasi yang mengeluarkan input
  secara langsung jika bernilai positif, dan nol jika tidak.
---
## Definition

ReLU banyak digunakan dalam jaringan saraf pembelajaran mendalam karena efisiensi komputasinya dan kemampuannya mengurangi masalah gradien yang menghilang (vanishing gradient). Secara matematis didefinisikan sebagai f(x) = max(0, x), fungsi ini introduc

### Summary

Rectified Linear Unit adalah fungsi aktivasi yang mengeluarkan input secara langsung jika bernilai positif, dan nol jika tidak.

## Key Concepts

- Non-linearitas
- Fungsi Aktivasi
- Gradien Menghilang (Vanishing Gradient)
- Linear Potong-Potong (Piecewise Linear)

## Use Cases

- Lapisan tersembunyi pada CNN
- Jaringan Feedforward Dalam
- Model Pengenalan Gambar

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (Fungsi aktivasi S)](/en/terms/sigmoid-fungsi-aktivasi-s/)
- [Tanh (Fungsi tangen hiperbolik)](/en/terms/tanh-fungsi-tangen-hiperbolik/)
- [Leaky ReLU (Variasi ReLU)](/en/terms/leaky-relu-variasi-relu/)
- [Jaringan Saraf (Neural Network)](/en/terms/jaringan-saraf-neural-network/)
