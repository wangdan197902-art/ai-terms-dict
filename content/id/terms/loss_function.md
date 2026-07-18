---
title: "Fungsi Kerugian"
term_id: "loss_function"
category: "basic_concepts"
subcategory: ""
tags: ["training", "mathematics", "evaluation"]
difficulty: 3
weight: 1
slug: "loss_function"
aliases:
  - /id/terms/loss_function/
date: "2026-07-18T15:34:55.886084Z"
lastmod: "2026-07-18T16:38:07.415731Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Fungsi matematika yang mengukur perbedaan antara nilai prediksi dan nilai target aktual selama pelatihan."
---

## Definition

Dikenal juga sebagai fungsi biaya atau kesalahan, fungsi kerugian menyediakan nilai skalar yang menunjukkan seberapa baik kinerja model. Selama pelatihan, algoritma optimisasi menggunakan nilai ini untuk menghitung gradien dan memperbarui parameter model guna meminimalkan kesalahan prediksi.

### Summary

Fungsi matematika yang mengukur perbedaan antara nilai prediksi dan nilai target aktual selama pelatihan.

## Key Concepts

- Propagasi Balik
- Komputasi Gradien
- Optimisasi
- Metrik Kesalahan

## Use Cases

- Melatih model pembelajaran terawasi
- Mengevaluasi kinerja model
- Penyetelan hiperparameter

## Code Example

```python
import torch.nn as nn
criterion = nn.CrossEntropyLoss()
```

## Related Terms

- [backpropagation (propagasi balik)](/en/terms/backpropagation-propagasi-balik/)
- [gradient_descent (penurunan gradien)](/en/terms/gradient_descent-penurunan-gradien/)
- [cross_entropy (entropi silang)](/en/terms/cross_entropy-entropi-silang/)
- [mse (mean squared error / rata-rata kuadrat kesalahan)](/en/terms/mse-mean-squared-error-rata-rata-kuadrat-kesalahan/)
