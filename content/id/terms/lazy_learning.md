---
title: "Pembelajaran malas"
term_id: "lazy_learning"
category: "training_techniques"
subcategory: ""
tags: ["algorithms", "training_methods", "machine_learning"]
difficulty: 2
weight: 1
slug: "lazy_learning"
aliases:
  - /id/terms/lazy_learning/
date: "2026-07-18T15:57:27.375192Z"
lastmod: "2026-07-18T16:38:07.476106Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Pendekatan pembelajaran yang menunda generalisasi hingga waktu klasifikasi, dengan menyimpan instance pelatihan daripada membangun model eksplisit."
---

## Definition

Pembelajar malas, seperti k-Nearest Neighbors (k-NN), menghafal seluruh dataset pelatihan dan melakukan komputasi hanya saat membuat prediksi. Hal ini kontras dengan pembelajaran aktif (eager learning), yang membangun model umum sebelum melihat data uji.

### Summary

Pendekatan pembelajaran yang menunda generalisasi hingga waktu klasifikasi, dengan menyimpan instance pelatihan daripada membangun model eksplisit.

## Key Concepts

- Pembelajaran Berbasis Instance
- k-Nearest Neighbors
- Biaya Inferensi
- Generalisasi

## Use Cases

- Sistem rekomendasi
- Pengenalan pola dalam dataset kecil
- Prototipe model prediktif

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)
```

## Related Terms

- [instance_based_learning (pembelajaran berbasis instance)](/en/terms/instance_based_learning-pembelajaran-berbasis-instance/)
- [knn (k-NN)](/en/terms/knn-k-nn/)
- [eager_learning (pembelajaran aktif)](/en/terms/eager_learning-pembelajaran-aktif/)
- [generalization (generalisasi)](/en/terms/generalization-generalisasi/)
