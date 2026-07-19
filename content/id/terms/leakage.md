---
title: Kebocoran Data
term_id: leakage
category: basic_concepts
subcategory: ''
tags:
- Data Integrity
- evaluation
- Best Practices
difficulty: 3
weight: 1
slug: leakage
date: '2026-07-18T15:57:39.683548Z'
lastmod: '2026-07-18T16:38:07.476231Z'
draft: false
source: agnes_llm
status: published
language: id
description: Kebocoran data terjadi ketika informasi dari luar dataset pelatihan secara
  tidak sengaja memengaruhi model, yang mengakibatkan estimasi kinerja yang terlalu
  optimis.
---
## Definition

Kebocoran data adalah kesalahan kritis dalam pembelajaran mesin di mana model memperoleh akses ke informasi selama pelatihan yang tidak akan tersedia pada saat prediksi. Hal ini sering terjadi melalui pemisahan data yang tidak tepat atau fitur yang mengandung informasi masa depan.

### Summary

Kebocoran data terjadi ketika informasi dari luar dataset pelatihan secara tidak sengaja memengaruhi model, yang mengakibatkan estimasi kinerja yang terlalu optimis.

## Key Concepts

- Kebocoran target
- Kontaminasi data pelatihan-uji
- Pemisahan data yang tepat

## Use Cases

- Mendeteksi penyebab overfitting model
- Memvalidasi alur rekayasa fitur
- Memastikan evaluasi model yang robust

## Related Terms

- [Overfitting (Kelebihan pencocokan)](/en/terms/overfitting-kelebihan-pencocokan/)
- [Validasi silang](/en/terms/validasi-silang/)
- [Rekayasa fitur](/en/terms/rekayasa-fitur/)
