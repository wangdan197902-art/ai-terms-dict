---
title: "Jaringan Umpan Maju"
term_id: "feed_forward_network"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "architecture", "fundamentals"]
difficulty: 2
weight: 1
slug: "feed_forward_network"
aliases:
  - /id/terms/feed_forward_network/
date: "2026-07-18T15:50:36.790464Z"
lastmod: "2026-07-18T16:38:07.458337Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Kelas jaringan saraf tiruan di mana koneksi antar node tidak membentuk siklus, menyebarkan informasi dalam satu arah."
---

## Definition

Jaringan Umpan Maju (FFN), yang juga dikenal sebagai Multi-Layer Perceptrons (MLP), memproses data secara berurutan melalui lapisan neuron dari masukan ke keluaran tanpa loop umpan balik. Setiap neuron menerima masukan, melakukan penjumlahan tertimbang, dan menerapkannya pada fungsi aktivasi sebelum meneruskan sinyal ke lapisan berikutnya.

### Summary

Kelas jaringan saraf tiruan di mana koneksi antar node tidak membentuk siklus, menyebarkan informasi dalam satu arah.

## Key Concepts

- Tanpa Siklus
- Lapisan (Masukan, Tersembunyi, Keluaran)
- Fungsi Aktivasi
- Penjumlahan Tertimbang

## Use Cases

- Tugas regresi sederhana
- Masalah klasifikasi dengan data tabel
- Blok bangunan untuk arsitektur yang lebih dalam

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron (Perseptron Multi-Lapis)](/en/terms/multi-layer-perceptron-perseptron-multi-lapis/)
- [Backpropagation (Propagasi Balik)](/en/terms/backpropagation-propagasi-balik/)
- [Activation Function (Fungsi Aktivasi)](/en/terms/activation-function-fungsi-aktivasi/)
- [Neural Network (Jaringan Saraf)](/en/terms/neural-network-jaringan-saraf/)
