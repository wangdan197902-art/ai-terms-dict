---
title: Pengacakan Fitur
term_id: feature_hashing
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- Text Mining
- Optimization
difficulty: 3
weight: 1
slug: feature_hashing
date: '2026-07-18T15:50:36.790420Z'
lastmod: '2026-07-18T16:38:07.457831Z'
draft: false
source: agnes_llm
status: published
language: id
description: Sebuah teknik yang memetakan fitur jarang (sparse) berdimensi tinggi
  ke dalam vektor berukuran tetap menggunakan fungsi hash.
---
## Definition

Pengacakan fitur, yang juga dikenal sebagai trik pengacakan (hashing trick), memungkinkan model pembelajaran mesin menangani ruang fitur yang besar dan jarang tanpa perlu mempertahankan pemetaan eksplisit antara fitur dan indeks. Dengan menerapkan fungsi hash, teknik ini mengubah fitur menjadi indeks vektor yang tetap, sehingga menghemat memori dan komputasi.

### Summary

Sebuah teknik yang memetakan fitur jarang (sparse) berdimensi tinggi ke dalam vektor berukuran tetap menggunakan fungsi hash.

## Key Concepts

- Fungsi Hash
- Vektor Jarang
- Reduksi Dimensi
- Efisiensi Memori

## Use Cases

- Klasifikasi teks dengan kosakata besar
- Sistem rekomendasi dengan set item yang sangat besar
- Pemrosesan data aliran waktu nyata (real-time streaming)

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-hot encoding (Enkoding satu-hot)](/en/terms/one-hot-encoding-enkoding-satu-hot/)
- [Bag of Words (Tas Kata)](/en/terms/bag-of-words-tas-kata/)
- [Dimensionality reduction (Reduksi dimensi)](/en/terms/dimensionality-reduction-reduksi-dimensi/)
- [Sparse matrix (Matriks jarang)](/en/terms/sparse-matrix-matriks-jarang/)
