---
title: "Fungsi Aktivasi"
term_id: "activation_function"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "mathematics", "deep_learning", "basics"]
difficulty: 3
weight: 1
slug: "activation_function"
aliases:
  - /id/terms/activation_function/
date: "2026-07-18T15:33:35.113509Z"
lastmod: "2026-07-18T16:38:07.411208Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Persamaan matematika yang menentukan output dari sebuah node jaringan saraf berdasarkan sinyal inputnya."
---

## Definition

Fungsi aktivasi memperkenalkan non-linearitas ke dalam jaringan saraf, memungkinkan jaringan tersebut mempelajari pola dan hubungan kompleks dalam data. Tanpa fungsi ini, jaringan berlapis akan berperilaku...

### Summary

Persamaan matematika yang menentukan output dari sebuah node jaringan saraf berdasarkan sinyal inputnya.

## Key Concepts

- Non-linearitas
- Penurunan Gradien
- Aktivasi Neuron
- Backpropagation (Propagasi Balik)

## Use Cases

- Memungkinkan jaringan saraf dalam mengklasifikasikan gambar
- Memfasilitasi tugas pemrosesan bahasa alami
- Meningkatkan kecepatan konvergensi saat melatih model generatif

## Code Example

```python
import torch.nn as nn
relu = nn.ReLU()
output = relu(input_tensor)
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Sigmoid](/en/terms/sigmoid/)
- [Tanh](/en/terms/tanh/)
- [Softmax](/en/terms/softmax/)
