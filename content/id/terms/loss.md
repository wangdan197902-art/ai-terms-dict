---
title: "Loss"
term_id: "loss"
category: "training_techniques"
subcategory: ""
tags: ["training", "optimization"]
difficulty: 3
weight: 1
slug: "loss"
aliases:
  - /id/terms/loss/
date: "2026-07-18T15:27:07.159837Z"
lastmod: "2026-07-18T16:38:07.396848Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Nilai numerik yang mengukur kesalahan antara prediksi model dan nilai target sebenarnya."
---

## Definition

Fungsi loss, juga dikenal sebagai fungsi biaya, mengukur seberapa baik prediksi model pembelajaran mesin sesuai dengan kebenaran dasar selama pelatihan. Tujuan dari algoritma optimasi adalah meminimalkan nilai

### Summary

Nilai numerik yang mengukur kesalahan antara prediksi model dan nilai target sebenarnya.

## Key Concepts

- Fungsi Biaya
- Optimasi
- Penurunan Gradien
- Metrik Kesalahan

## Use Cases

- Melatih pengklasifikasi gambar
- Mengoptimalkan model regresi
- Mengevaluasi konvergensi model

## Code Example

```python
import torch.nn as nn
criterion = nn.CrossEntropyLoss()
loss = criterion(outputs, targets)
```

## Related Terms

- [Accuracy (Akurasi)](/en/terms/accuracy-akurasi/)
- [Gradient Descent (Penurunan gradien)](/en/terms/gradient-descent-penurunan-gradien/)
- [Cross-Entropy (Entropi silang)](/en/terms/cross-entropy-entropi-silang/)
- [Overfitting (Kelebihan pasokan/overfitting)](/en/terms/overfitting-kelebihan-pasokan-overfitting/)
