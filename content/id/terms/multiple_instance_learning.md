---
title: Pembelajaran Multiple Instance
term_id: multiple_instance_learning
category: training_techniques
subcategory: ''
tags:
- Supervised Learning
- Weak Labeling
- ML Paradigm
difficulty: 4
weight: 1
slug: multiple_instance_learning
date: '2026-07-18T15:35:24.562427Z'
lastmod: '2026-07-18T16:38:07.416601Z'
draft: false
source: agnes_llm
status: published
language: id
description: Paradigma pembelajaran semi-pengawasan di mana label diberikan kepada
  kumpulan (bag) instance, bukan pada instance individu.
---
## Definition

Pembelajaran Multiple Instance (MIL) menangani skenario di mana data dikelompokkan menjadi 'kumpulan' dengan satu label, sementara instance individu di dalam kumpulan tersebut tetap tidak berlabel. Sebuah kumpulan biasanya bersifat positif jika setidaknya satu instance di dalamnya memiliki properti yang relevan, meskipun instance lainnya mungkin negatif.

### Summary

Paradigma pembelajaran semi-pengawasan di mana label diberikan kepada kumpulan (bag) instance, bukan pada instance individu.

## Key Concepts

- Penandaan tingkat kumpulan
- Ketidakpastian tingkat instance
- Semi-pengawasan
- Logika positif/negatif kumpulan

## Use Cases

- Prediksi aktivitas obat
- Klasifikasi gambar dengan kotak pembatas (bounding boxes)
- Pencarian gambar berbasis konten

## Related Terms

- [weak_supervision (semi-pengawasan)](/en/terms/weak_supervision-semi-pengawasan/)
- [bagging (teknik ensemble)](/en/terms/bagging-teknik-ensemble/)
- [instance_classification (klasifikasi instance)](/en/terms/instance_classification-klasifikasi-instance/)
- [label_noise (kebisingan label)](/en/terms/label_noise-kebisingan-label/)
