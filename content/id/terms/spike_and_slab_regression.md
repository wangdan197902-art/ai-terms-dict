---
title: "Regresi Spike-and-Slab"
term_id: "spike_and_slab_regression"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "bayesian", "regression"]
difficulty: 4
weight: 1
slug: "spike_and_slab_regression"
aliases:
  - /id/terms/spike_and_slab_regression/
date: "2026-07-18T16:09:47.379061Z"
lastmod: "2026-07-18T16:38:07.509990Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Sebuah metode seleksi variabel Bayesian yang menggunakan prior campuran untuk membedakan antara koefisien nol dan bukan nol."
---

## Definition

Regresi Spike-and-Slab adalah teknik statistik Bayesian yang digunakan untuk seleksi variabel dan pemodelan jarang (sparse modeling). Teknik ini menggunakan distribusi prior campuran yang terdiri dari dua komponen: 'spike' (biasanya berupa distribusi Dirac di nol atau distribusi normal dengan varians sangat kecil) untuk merepresentasikan koefisien yang nol, dan 'slab' (biasanya distribusi normal dengan varians lebih besar) untuk merepresentasikan koefisien yang tidak nol. Pendekatan ini memungkinkan model secara probabilistik menentukan apakah suatu prediktor harus disertakan dalam model atau tidak.

### Summary

Sebuah metode seleksi variabel Bayesian yang menggunakan prior campuran untuk membedakan antara koefisien nol dan bukan nol.

## Key Concepts

- Inferensi Bayesian
- Pemodelan jarang (Sparse modeling)
- Prior campuran
- Seleksi variabel

## Use Cases

- Analisis data genomik berdimensi tinggi
- Identifikasi faktor risiko keuangan
- Seleksi fitur dalam pemodelan prediktif

## Related Terms

- [Lasso (Regresi L1 untuk sparsity)](/en/terms/lasso-regresi-l1-untuk-sparsity/)
- [Ridge Regression (Regresi L2 untuk regularisasi)](/en/terms/ridge-regression-regresi-l2-untuk-regularisasi/)
- [Bayesian Linear Regression (Regresi Linear Bayesian)](/en/terms/bayesian-linear-regression-regresi-linear-bayesian/)
- [Sparsity (Sifat jarang/kekosongan parameter)](/en/terms/sparsity-sifat-jarang-kekosongan-parameter/)
