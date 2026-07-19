---
title: Pembelajaran Supervisi
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T15:36:17.841141Z'
lastmod: '2026-07-18T16:38:07.419942Z'
draft: false
source: agnes_llm
status: published
language: id
description: Paradigma pembelajaran mesin di mana model belajar memetakan input ke
  output berdasarkan contoh pelatihan yang berlabel.
---
## Definition

Dalam pembelajaran supervisi, algoritma dilatih pada dataset berlabel, artinya setiap contoh input dipasangkan dengan output yang benar. Tujuannya adalah agar model mempelajari hubungan mendasar antara input dan output.

### Summary

Paradigma pembelajaran mesin di mana model belajar memetakan input ke output berdasarkan contoh pelatihan yang berlabel.

## Key Concepts

- Data Berlabel
- Pemetaan Input-Output
- Klasifikasi
- Regresi

## Use Cases

- Deteksi email spam
- Prediksi harga rumah
- Pengenalan gambar

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (Pembelajaran Tanpa Pengawasan)](/en/terms/unsupervised-learning-pembelajaran-tanpa-pengawasan/)
- [Training Set (Himpunan Pelatihan)](/en/terms/training-set-himpunan-pelatihan/)
- [Validation Set (Himpunan Validasi)](/en/terms/validation-set-himpunan-validasi/)
- [Model Accuracy (Akurasi Model)](/en/terms/model-accuracy-akurasi-model/)
