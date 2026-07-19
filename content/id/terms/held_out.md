---
title: held-out (data yang disisihkan)
term_id: held_out
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Data Splitting
- validation
difficulty: 2
weight: 1
slug: held_out
date: '2026-07-18T15:31:45.413608Z'
lastmod: '2026-07-18T16:38:07.408114Z'
draft: false
source: agnes_llm
status: published
language: id
description: Sampel data yang dicadangkan dari himpunan pelatihan untuk mengevaluasi
  kinerja model dan mencegah overfitting selama pengembangan.
---
## Definition

Dataset 'held-out' terdiri dari contoh-contoh yang sengaja dikecualikan dari fase pelatihan model pembelajaran mesin. Subset ini digunakan untuk menilai seberapa baik model dapat digeneralisasi ke data yang belum pernah dilihat sebelumnya, memberikan estimasi kinerja yang tidak bias terhadap data baru.

### Summary

Sampel data yang dicadangkan dari himpunan pelatihan untuk mengevaluasi kinerja model dan mencegah overfitting selama pengembangan.

## Key Concepts

- Generalisasi
- Overfitting
- Himpunan validasi
- Evaluasi tidak bias

## Use Cases

- Menyetel hiperparameter
- Membandingkan berbagai arsitektur model
- Estimasi kinerja akhir sebelum produksi

## Related Terms

- [training_set (himpunan pelatihan)](/en/terms/training_set-himpunan-pelatihan/)
- [test_set (himpunan pengujian)](/en/terms/test_set-himpunan-pengujian/)
- [cross_validation (validasi silang)](/en/terms/cross_validation-validasi-silang/)
- [generalization (generalisasi)](/en/terms/generalization-generalisasi/)
