---
title: Koneksi Residual
term_id: residual_connection
category: basic_concepts
subcategory: ''
tags:
- architecture
- Optimization
- Deep Learning
difficulty: 3
weight: 1
slug: residual_connection
date: '2026-07-18T15:36:05.535153Z'
lastmod: '2026-07-18T16:38:07.418729Z'
draft: false
source: agnes_llm
status: published
language: id
description: Mekanisme yang menambahkan input secara langsung ke output lapisan untuk
  memfasilitasi aliran gradien dalam jaringan yang dalam.
---
## Definition

Koneksi residual, juga dikenal sebagai koneksi skip, memungkinkan gradien mengalir melalui jaringan dengan menambahkan input secara langsung ke output lapisan berikutnya. Arsitektur ini menyelesaikan masalah gradien menghilang (vanishing gradient) pada jaringan yang sangat dalam.

### Summary

Mekanisme yang menambahkan input secara langsung ke output lapisan untuk memfasilitasi aliran gradien dalam jaringan yang dalam.

## Key Concepts

- Koneksi Skip
- Masalah Gradien Menghilang
- Pembelajaran Residual Dalam
- Aliran Gradien

## Use Cases

- Melatih jaringan saraf konvolusional yang dalam
- Arsitektur Transformer
- Model klasifikasi gambar

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (koneksi skip)](/en/terms/skip_connection-koneksi-skip/)
- [vanishing_gradient (gradien menghilang)](/en/terms/vanishing_gradient-gradien-menghilang/)
- [deep_learning (pembelajaran mendalam)](/en/terms/deep_learning-pembelajaran-mendalam/)
- [resnet (jaringan residual)](/en/terms/resnet-jaringan-residual/)
