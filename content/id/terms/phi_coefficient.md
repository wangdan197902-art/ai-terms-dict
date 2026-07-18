---
title: "Koefisien Phi"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /id/terms/phi_coefficient/
date: "2026-07-18T16:04:14.079832Z"
lastmod: "2026-07-18T16:38:07.494110Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Ukuran statistik untuk mengukur asosiasi antara dua variabel biner."
---

## Definition

Koefisien Phi (φ) adalah ukuran asosiasi untuk dua variabel biner, yang berfungsi sebagai koefisien korelasi Pearson untuk variabel dikotomi. Nilainya berkisar dari -1 hingga +1, di mana 0 menunjukkan tidak ada asosiasi.

### Summary

Ukuran statistik untuk mengukur asosiasi antara dua variabel biner.

## Key Concepts

- Variabel Biner
- Korelasi
- Tabel Kontingensi
- Kekuatan Asosiasi

## Use Cases

- Mengevaluasi kinerja klasifikator biner di luar akurasi
- Menganalisis hubungan dalam data survei dengan respons ya/tidak
- Seleksi fitur dalam dataset dengan input kategorikal

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [Cramer's V (V Cramer)](/en/terms/cramer-s-v-v-cramer/)
- [Pearson correlation (Korelasi Pearson)](/en/terms/pearson-correlation-korelasi-pearson/)
- [Confusion matrix (Matriks Kekeliruan)](/en/terms/confusion-matrix-matriks-kekeliruan/)
- [Mutual information (Informasi Bersama)](/en/terms/mutual-information-informasi-bersama/)
