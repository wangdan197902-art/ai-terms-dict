---
title: "Tingkat Pembelajaran"
term_id: "learning_rate"
category: "training_techniques"
subcategory: ""
tags: ["training", "optimization", "hyperparameters"]
difficulty: 3
weight: 1
slug: "learning_rate"
aliases:
  - /id/terms/learning_rate/
date: "2026-07-18T15:34:55.886062Z"
lastmod: "2026-07-18T16:38:07.415426Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Hiperparameter yang mengontrol ukuran langkah selama optimisasi model untuk meminimalkan fungsi kerugian."
---

## Definition

Tingkat pembelajaran menentukan seberapa besar bobot model diperbarui relatif terhadap gradien yang dihitung selama setiap iterasi pelatihan. Tingkat yang terlalu tinggi dapat menyebabkan model melewatasi optimum, sedangkan tingkat yang terlalu rendah dapat membuat pelatihan menjadi sangat lambat atau terjebak dalam minimum lokal.

### Summary

Hiperparameter yang mengontrol ukuran langkah selama optimisasi model untuk meminimalkan fungsi kerugian.

## Key Concepts

- Penurunan Gradien
- Penyetelan Hiperparameter
- Konvergensi
- Pengoptimal

## Use Cases

- Pelatihan jaringan saraf
- Optimisasi model pembelajaran mendalam
- Pembaruan kebijakan pembelajaran penguatan

## Code Example

```python
import torch.optim as optim
model = MyModel()
optimizer = optim.SGD(model.parameters(), lr=0.01)
```

## Related Terms

- [gradient_descent (penurunan gradien)](/en/terms/gradient_descent-penurunan-gradien/)
- [optimizer (pengoptimal)](/en/terms/optimizer-pengoptimal/)
- [hyperparameter (hiperparameter)](/en/terms/hyperparameter-hiperparameter/)
- [convergence (konvergensi)](/en/terms/convergence-konvergensi/)
