---
title: "Dense"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /id/terms/dense/
date: "2026-07-18T15:47:44.305297Z"
lastmod: "2026-07-18T16:38:07.449733Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Lapisan atau tensor di mana setiap elemen terhubung ke setiap elemen dari lapisan atau dimensi sebelumnya."
---

## Definition

Dalam jaringan saraf, 'dense' mengacu pada lapisan yang sepenuhnya terhubung di mana setiap neuron menerima masukan dari semua neuron di lapisan sebelumnya. Ini berbeda dengan koneksi jarang yang ditemukan dalam konvolusi atau...

### Summary

Lapisan atau tensor di mana setiap elemen terhubung ke setiap elemen dari lapisan atau dimensi sebelumnya.

## Key Concepts

- Terhubung Penuh
- Matriks Bobot
- Fungsi Aktivasi
- Integrasi Fitur

## Use Cases

- Lapisan klasifikasi akhir dalam MLP
- Fusi fitur dalam model hibrida
- Tugas regresi sederhana

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Jaringan Saraf Umpan Maju)](/en/terms/feedforward-neural-network-jaringan-saraf-umpan-maju/)
- [Backpropagation (Propagasi Balik)](/en/terms/backpropagation-propagasi-balik/)
- [ReLU (Fungsi Aktivasi Linear Terpotong)](/en/terms/relu-fungsi-aktivasi-linear-terpotong/)
- [Bias Term (Istilah Bias)](/en/terms/bias-term-istilah-bias/)
