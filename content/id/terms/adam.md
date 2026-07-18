---
title: "Adam"
term_id: "adam"
category: "basic_concepts"
subcategory: ""
tags: ["Optimization", "Deep Learning", "Algorithms"]
difficulty: 3
weight: 1
slug: "adam"
aliases:
  - /id/terms/adam/
date: "2026-07-18T15:23:13.605932Z"
lastmod: "2026-07-18T16:38:07.388218Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Algoritma optimisasi yang menghitung tingkat pembelajaran adaptif untuk setiap parameter."
---

## Definition

Adam (Adaptive Moment Estimation) adalah algoritma optimisasi berbasis gradien orde pertama yang populer digunakan dalam pelatihan jaringan saraf tiruan mendalam. Algoritma ini menggabungkan keunggulan dari dua ekstensi lain dari stokastik

### Summary

Algoritma optimisasi yang menghitung tingkat pembelajaran adaptif untuk setiap parameter.

## Key Concepts

- Penurunan Gradien
- Tingkat Pembelajaran
- Momentum
- Estimasi Varians

## Use Cases

- Pelatihan Deep Learning
- Model Computer Vision
- Pemrosesan Bahasa Alamiah

## Code Example

```python
import torch.optim as optim
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

## Related Terms

- [SGD (Stochastic Gradient Descent)](/en/terms/sgd-stochastic-gradient-descent/)
- [RMSProp](/en/terms/rmsprop/)
- [Optimizer (Pengoptimal)](/en/terms/optimizer-pengoptimal/)
- [Backpropagation (Propagasi Balik)](/en/terms/backpropagation-propagasi-balik/)
