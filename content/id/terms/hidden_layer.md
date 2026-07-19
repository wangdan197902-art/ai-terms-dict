---
title: Lapisan Tersembunyi
term_id: hidden_layer
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- Deep Learning
difficulty: 3
weight: 1
slug: hidden_layer
date: '2026-07-18T15:54:25.332379Z'
lastmod: '2026-07-18T16:38:07.466442Z'
draft: false
source: agnes_llm
status: published
language: id
description: Lapisan perantara dalam jaringan saraf antara lapisan masukan dan keluaran
  yang memproses fitur.
---
## Definition

Lapisan tersembunyi terdiri dari neuron yang menerima masukan dari lapisan sebelumnya, menerapkan bobot dan bias, serta meneruskan data yang telah ditransformasikan ke depan melalui fungsi aktivasi. Lapisan-lapisan ini memungkinkan jaringan saraf untuk mempelajari representasi data yang kompleks dan abstrak.

### Summary

Lapisan perantara dalam jaringan saraf antara lapisan masukan dan keluaran yang memproses fitur.

## Key Concepts

- Jaringan Saraf
- Ekstraksi Fitur
- Fungsi Aktivasi
- Pembelajaran Mendalam

## Use Cases

- Sistem pengenalan gambar
- Model pemrosesan bahasa alami
- Analitik prediktif

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron (neuron)](/en/terms/neuron-neuron/)
- [backpropagation (propagasi mundur)](/en/terms/backpropagation-propagasi-mundur/)
- [activation_function (fungsi aktivasi)](/en/terms/activation_function-fungsi-aktivasi/)
- [deep_learning (pembelajaran mendalam)](/en/terms/deep_learning-pembelajaran-mendalam/)
