---
title: Hipotesis Tiket Lotere
term_id: lottery_ticket_hypothesis
category: basic_concepts
subcategory: ''
tags:
- Optimization
- pruning
- theory
difficulty: 4
weight: 1
slug: lottery_ticket_hypothesis
date: '2026-07-18T15:58:53.437603Z'
lastmod: '2026-07-18T16:38:07.479475Z'
draft: false
source: agnes_llm
status: published
language: id
description: Teori bahwa jaringan saraf padat mengandung sub-jaringan lebih kecil
  yang, ketika dilatih secara terisolasi dari inisialisasinya, dapat mencapai akurasi
  yang setara dengan jaringan asli.
---
## Definition

Hipotesis Tiket Lotere menyatakan bahwa dalam jaringan saraf besar yang diinisialisasi secara acak, terdapat sub-jaringan jarang (atau 'tiket pemenang') yang sudah memiliki inisialisasi yang baik untuk pelatihan. Dengan memangkas bobot yang tidak penting dan melatih sub-jaringan ini secara terisolasi, performa yang setara dengan jaringan penuh dapat dicapai.

### Summary

Teori bahwa jaringan saraf padat mengandung sub-jaringan lebih kecil yang, ketika dilatih secara terisolasi dari inisialisasinya, dapat mencapai akurasi yang setara dengan jaringan asli.

## Key Concepts

- Pemangkasan bobot
- Jaringan jarang
- Kompresi model
- Sensitivitas inisialisasi

## Use Cases

- Menyebarkan model ringan pada perangkat tepi
- Mengurangi biaya komputasi selama pelatihan
- Mempercepat kecepatan inferensi

## Related Terms

- [Network Pruning (Pemangkasan Jaringan)](/en/terms/network-pruning-pemangkasan-jaringan/)
- [Model Distillation (Distilasi Model)](/en/terms/model-distillation-distilasi-model/)
- [Sparse Training (Pelatihan Jarang)](/en/terms/sparse-training-pelatihan-jarang/)
- [Efficient AI (AI Efisien)](/en/terms/efficient-ai-ai-efisien/)
