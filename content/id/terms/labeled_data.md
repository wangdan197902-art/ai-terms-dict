---
title: Data berlabel
term_id: labeled_data
category: basic_concepts
subcategory: ''
tags:
- data
- Supervised Learning
- fundamentals
difficulty: 1
weight: 1
slug: labeled_data
date: '2026-07-18T15:57:27.375099Z'
lastmod: '2026-07-18T16:38:07.475533Z'
draft: false
source: agnes_llm
status: published
language: id
description: Data di mana nilai keluaran atau target yang benar disediakan bersama
  dengan fitur masukan.
---
## Definition

Data berlabel terdiri dari sampel masukan yang dipasangkan dengan label kebenaran dasar (ground truth) yang sesuai, yang menjadi fondasi untuk pembelajaran mesin terawasi (supervised machine learning). Hal ini memungkinkan algoritma mempelajari pemetaan antara masukan dan keluaran.

### Summary

Data di mana nilai keluaran atau target yang benar disediakan bersama dengan fitur masukan.

## Key Concepts

- Pembelajaran Terawasi
- Kebenaran Dasar
- Anotasi
- Variabel Target

## Use Cases

- Melatih pengklasifikasi gambar
- Membangun sistem pengenalan suara
- Pemodelan prediktif dalam keuangan

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (data tanpa label)](/en/terms/unlabeled_data-data-tanpa-label/)
- [supervised_learning (pembelajaran terawasi)](/en/terms/supervised_learning-pembelajaran-terawasi/)
- [data_annotation (anotasi data)](/en/terms/data_annotation-anotasi-data/)
- [training_set (himpunan pelatihan)](/en/terms/training_set-himpunan-pelatihan/)
