---
title: Fitur Acak
term_id: random_feature
category: basic_concepts
subcategory: ''
tags:
- Kernel Methods
- Feature Engineering
- Optimization
difficulty: 3
weight: 1
slug: random_feature
date: '2026-07-18T16:06:48.591936Z'
lastmod: '2026-07-18T16:38:07.499727Z'
draft: false
source: agnes_llm
status: published
language: id
description: Sebuah teknik yang memetakan data input ke ruang berdimensi lebih tinggi
  menggunakan proyeksi acak untuk mengaproksimasi metode kernel secara efisien.
---
## Definition

Pemetaan fitur acak mengubah input ke ruang baru di mana model linier dapat mengaproksimasi fungsi kernel non-linier. Pendekatan ini, yang sering dikaitkan dengan metode Nystrom atau fitur Fourier, memungkinkan komputasi yang lebih cepat dan skalabel.

### Summary

Sebuah teknik yang memetakan data input ke ruang berdimensi lebih tinggi menggunakan proyeksi acak untuk mengaproksimasi metode kernel secara efisien.

## Key Concepts

- Aproksimasi kernel
- Pemetaan fitur
- Efisiensi komputasi
- Linierisasi

## Use Cases

- Regresi kernel skala besar
- Aproksimasi Neural Tangent Kernel
- Proses Gaussian yang skalabel

## Code Example

```python
import numpy as np
from sklearn.kernel_approximation import RBFSampler
X = np.random.rand(100, 5)
transformer = RBFSampler(gamma=1, n_components=50, random_state=42)
X_transformed = transformer.fit_transform(X)
```

## Related Terms

- [Trik kernel](/en/terms/trik-kernel/)
- [Fitur Fourier](/en/terms/fitur-fourier/)
- [Metode Nystrom](/en/terms/metode-nystrom/)
- [Reduksi dimensi](/en/terms/reduksi-dimensi/)
