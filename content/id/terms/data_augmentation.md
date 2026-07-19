---
title: Augmentasi Data
term_id: data_augmentation
category: training_techniques
subcategory: ''
tags:
- Machine Learning
- preprocessing
- cv
difficulty: 2
weight: 1
slug: data_augmentation
date: '2026-07-18T15:44:45.409478Z'
lastmod: '2026-07-18T16:38:07.442392Z'
draft: false
source: agnes_llm
status: published
language: id
description: Augmentasi data adalah teknik yang digunakan untuk meningkatkan keragaman
  dan ukuran dataset pelatihan dengan menerapkan transformasi pada titik data yang
  ada.
---
## Definition

Metode ini memperluas dataset pelatihan secara artifisial dengan membuat versi modifikasi dari sampel yang ada, seperti memutar gambar, menambahkan noise pada audio, atau penggantian sinonim dalam teks. Hal ini membantu mencegah

### Summary

Augmentasi data adalah teknik yang digunakan untuk meningkatkan keragaman dan ukuran dataset pelatihan dengan menerapkan transformasi pada titik data yang ada.

## Key Concepts

- Pencegahan Overfitting
- Ekspansi Dataset
- Generalisasi
- Transformasi

## Use Cases

- Meningkatkan ketahanan model computer vision
- Meningkatkan kinerja model NLP dengan teks terbatas
- Menyeimbangkan dataset yang tidak seimbang

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularization (Regularisasi)](/en/terms/regularization-regularisasi/)
- [Synthetic Data (Data Sintetis)](/en/terms/synthetic-data-data-sintetis/)
- [Transfer Learning (Pembelajaran Transfer)](/en/terms/transfer-learning-pembelajaran-transfer/)
- [Overfitting (Overfitting)](/en/terms/overfitting-overfitting/)
