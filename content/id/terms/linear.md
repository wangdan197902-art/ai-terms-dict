---
title: "Linear"
term_id: "linear"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Foundations"]
difficulty: 2
weight: 1
slug: "linear"
aliases:
  - /id/terms/linear/
date: "2026-07-18T15:26:54.087902Z"
lastmod: "2026-07-18T16:38:07.396295Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Menggambarkan operasi atau hubungan di mana output berbanding lurus secara langsung dengan input, membentuk dasar transformasi afin dalam lapisan saraf."
---

## Definition

Operasi linear melibatkan perkalian dan penjumlahan tanpa aktivasi non-linear. Dalam jaringan saraf, lapisan linear (atau lapisan padat) menerapkan transformasi matriks bobot ke vektor input. Meskipun l

### Summary

Menggambarkan operasi atau hubungan di mana output berbanding lurus secara langsung dengan input, membentuk dasar transformasi afin dalam lapisan saraf.

## Key Concepts

- Matriks Bobot
- Transformasi Afine
- Produk Titik
- Superposisi

## Use Cases

- Proyeksi Fitur
- Regresi Logistik
- Mekanisme Perhatian

## Code Example

```python
import torch.nn as nn
layer = nn.Linear(10, 5)
output = layer(input_tensor)
```

## Related Terms

- [Fungsi Aktivasi](/en/terms/fungsi-aktivasi/)
- [Lapisan Padat](/en/terms/lapisan-padat/)
- [Perkalian Matriks](/en/terms/perkalian-matriks/)
