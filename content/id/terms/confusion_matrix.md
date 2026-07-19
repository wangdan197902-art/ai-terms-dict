---
title: Matriks Kebingungan
term_id: confusion_matrix
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Classification
- metrics
difficulty: 2
weight: 1
slug: confusion_matrix
date: '2026-07-18T15:43:34.312203Z'
lastmod: '2026-07-18T16:38:07.439814Z'
draft: false
source: agnes_llm
status: published
language: id
description: Sebuah tabel yang digunakan untuk menggambarkan kinerja model klasifikasi
  pada seperangkat data uji.
---
## Definition

Matriks kebingungan adalah tata letak tabel spesifik yang memungkinkan visualisasi kinerja suatu algoritma, biasanya pembelajaran terawasi. Tabel ini menunjukkan jumlah true positive (positif benar), true negative (negatif benar), false positive (positif salah), dan false negative (negatif salah).

### Summary

Sebuah tabel yang digunakan untuk menggambarkan kinerja model klasifikasi pada seperangkat data uji.

## Key Concepts

- Positif Benar
- Negatif Salah
- Presisi
- Panggilan Kembali

## Use Cases

- Mengevaluasi klasifikator biner
- Menganalisis kinerja klasifikasi multi-kelas
- Men-debug bias model pada dataset yang tidak seimbang

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (presisi)](/en/terms/precision-presisi/)
- [recall (panggilan kembali)](/en/terms/recall-panggilan-kembali/)
- [F1 score (skor F1)](/en/terms/f1-score-skor-f1/)
- [ROC curve (kurva ROC)](/en/terms/roc-curve-kurva-roc/)
