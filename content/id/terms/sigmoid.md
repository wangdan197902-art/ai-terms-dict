---
title: "Sigmoid"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:08:37.677453Z"
lastmod: "2026-07-18T16:38:07.506491Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Fungsi matematika yang memetakan bilangan bernilai riil apa pun ke nilai antara nol dan satu, membentuk kurva berbentuk S."
---
## Definition

Fungsi sigmoid, yang didefinisikan sebagai σ(z) = 1 / (1 + e^-z), banyak digunakan dalam pembelajaran mesin untuk memodelkan probabilitas. Fungsi ini menekan nilai input ke dalam rentang (0, 1), sehingga cocok untuk klasifikasi biner, meskipun sering menghadapi masalah gradien yang hilang pada jaringan yang dalam.

### Summary

Fungsi matematika yang memetakan bilangan bernilai riil apa pun ke nilai antara nol dan satu, membentuk kurva berbentuk S.

## Key Concepts

- Fungsi Logistik
- Pemetaan Probabilitas
- Gradien Hilang
- Non-linearitas

## Use Cases

- Output klasifikasi biner
- Regresi Logistik
- Aktivasi pada jaringan saraf dangkal

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Logistic Regression (Regresi Logistik)](/en/terms/logistic-regression-regresi-logistik/)
- [Activation Function (Fungsi Aktivasi)](/en/terms/activation-function-fungsi-aktivasi/)
