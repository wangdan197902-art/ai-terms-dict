---
title: "Pembelajaran berbasis instans"
term_id: "instance_based_learning"
category: "training_techniques"
subcategory: ""
tags: ["algorithm", "lazy_learning", "classification"]
difficulty: 2
weight: 1
slug: "instance_based_learning"
aliases:
  - /id/terms/instance_based_learning/
date: "2026-07-18T15:55:53.651894Z"
lastmod: "2026-07-18T16:38:07.471110Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Pendekatan pembelajaran malas di mana prediksi dibuat dengan membandingkan input baru dengan instans pelatihan yang disimpan."
---

## Definition

Juga dikenal sebagai pembelajaran berbasis memori, teknik ini tidak membangun model umum selama pelatihan. Sebaliknya, teknik ini menyimpan seluruh dataset pelatihan. Ketika prediksi diperlukan, teknik ini menemukan yang paling s

### Summary

Pendekatan pembelajaran malas di mana prediksi dibuat dengan membandingkan input baru dengan instans pelatihan yang disimpan.

## Key Concepts

- Pembelajaran malas
- Metrik kesamaan
- K-Nearest Neighbors (K-Tetangga Terdekat)
- Berbasis memori

## Use Cases

- Sistem rekomendasi
- Pengenalan pola
- Dataset kecil hingga menengah

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```

## Related Terms

- [KNN (K-Nearest Neighbors)](/en/terms/knn-k-nearest-neighbors/)
- [Similarity search (Pencarian kesamaan)](/en/terms/similarity-search-pencarian-kesamaan/)
- [Lazy learning (Pembelajaran malas)](/en/terms/lazy-learning-pembelajaran-malas/)
- [Kernel methods (Metode kernel)](/en/terms/kernel-methods-metode-kernel/)
