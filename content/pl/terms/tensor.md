---
title: "Tenzor"
term_id: "tensor"
category: "basic_concepts"
subcategory: ""
tags: ["math", "data-structures", "pytorch"]
difficulty: 2
weight: 1
slug: "tensor"
aliases:
  - /pl/terms/tensor/
date: "2026-07-18T16:20:05.759149Z"
lastmod: "2026-07-18T17:15:08.923052Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Wielowymiarowa tablica, która stanowi podstawową strukturę danych dla frameworków uczenia głębokiego."
---

## Definition

W informatyce i uczeniu głębokim tenzor to obiekt matematyczny uogólniający skalary, wektory i macierze na wyższe wymiary. Charakteryzuje się jego rangą (liczbą wymiarów) oraz kształtem.

### Summary

Wielowymiarowa tablica, która stanowi podstawową strukturę danych dla frameworków uczenia głębokiego.

## Key Concepts

- Ranga
- Kształt
- Wymiarowość
- Broadcasting (Rozpraszanie)

## Use Cases

- Przetwarzanie obrazów (tenzory 4D)
- Przechowywanie wag sieci neuronowych
- Wejście danych partiami (batched data)

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix (Macierz)](/en/terms/matrix-macierz/)
- [Vector (Wektor)](/en/terms/vector-wektor/)
- [Deep Learning (Uczenie głębokie)](/en/terms/deep-learning-uczenie-głębokie/)
- [NumPy (Biblioteka NumPy)](/en/terms/numpy-biblioteka-numpy/)
