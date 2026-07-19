---
title: "Terawasi"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
date: "2026-07-18T15:29:49.319385Z"
lastmod: "2026-07-18T16:38:07.403670Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Paradigma pembelajaran mesin di mana model dilatih pada pasangan input-output yang berlabel."
---
## Definition

Pembelajaran terawasi melibatkan pemberian data kepada algoritma yang mencakup baik input maupun jawaban yang benar (label). Model belajar memetakan input ke output dengan meminimalkan kesalahan prediksi.

### Summary

Paradigma pembelajaran mesin di mana model dilatih pada pasangan input-output yang berlabel.

## Key Concepts

- Data Berlabel
- Pemetaan
- Minimisasi Kerugian

## Use Cases

- Klasifikasi gambar
- Deteksi spam
- Prediksi harga

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (Pembelajaran dari data tanpa label, mencari pola tersembunyi)](/en/terms/unsupervised-pembelajaran-dari-data-tanpa-label-mencari-pola-tersembunyi/)
- [Label (Tanda atau anotasi yang menunjukkan kelas atau nilai target untuk sebuah contoh data)](/en/terms/label-tanda-atau-anotasi-yang-menunjukkan-kelas-atau-nilai-target-untuk-sebuah-contoh-data/)
- [Regression (Jenis tugas pembelajaran terawasi yang bertujuan memprediksi nilai kontinu)](/en/terms/regression-jenis-tugas-pembelajaran-terawasi-yang-bertujuan-memprediksi-nilai-kontinu/)
