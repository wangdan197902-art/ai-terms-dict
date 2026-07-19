---
title: Tanh
term_id: tanh
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- mathematics
difficulty: 2
weight: 1
slug: tanh
date: '2026-07-18T16:10:27.791361Z'
lastmod: '2026-07-18T16:38:07.512927Z'
draft: false
source: agnes_llm
status: published
language: id
description: Tanh, atau tangen hiperbolik, adalah fungsi aktivasi yang memetakan nilai
  input ke rentang antara -1 dan 1.
---
## Definition

Fungsi tangen hiperbolik (Tanh) adalah fungsi aktivasi non-linier yang umum digunakan dalam jaringan saraf. Fungsi ini menekan nilai input ke dalam interval (-1, 1), menyediakan output yang berpusat pada nol yang m

### Summary

Tanh, atau tangen hiperbolik, adalah fungsi aktivasi yang memetakan nilai input ke rentang antara -1 dan 1.

## Key Concepts

- Fungsi aktivasi
- Non-linearitas
- Output berpusat nol
- Backpropagation

## Use Cases

- Jaringan saraf rekuren
- Gerbang sel LSTM
- Lapisan tersembunyi dalam MLP

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (Sigmoid)](/en/terms/sigmoid-sigmoid/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (Jaringan Saraf)](/en/terms/neural_networks-jaringan-saraf/)
