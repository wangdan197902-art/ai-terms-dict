---
title: Evaluasi klasifier biner
term_id: evaluation_of_binary_classifiers
category: basic_concepts
subcategory: ''
tags:
- metrics
- Classification
- evaluation
difficulty: 2
weight: 1
slug: evaluation_of_binary_classifiers
date: '2026-07-18T15:49:47.840428Z'
lastmod: '2026-07-18T16:38:07.455802Z'
draft: false
source: agnes_llm
status: published
language: id
description: Proses menilai kinerja model pembelajaran mesin yang memprediksi salah
  satu dari dua kemungkinan hasil.
---
## Definition

Bidang ini melibatkan analisis metrik seperti akurasi, presisi, recall, skor F1, dan Area Under the Receiver Operating Characteristic Curve (AUC-ROC). Hal ini membantu menentukan seberapa baik model dapat membedakan antara kelas positif dan negatif.

### Summary

Proses menilai kinerja model pembelajaran mesin yang memprediksi salah satu dari dua kemungkinan hasil.

## Key Concepts

- Matriks Kekacauan (Confusion Matrix)
- Pertukaran Presisi-Recall
- Kurva ROC
- Skor F1

## Use Cases

- Skrining penyakit medis
- Penyaringan email spam
- Penilaian risiko kredit

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (matriks kesalahan)](/en/terms/confusion_matrix-matriks-kesalahan/)
- [roc_auc (luas di bawah kurva ROC)](/en/terms/roc_auc-luas-di-bawah-kurva-roc/)
- [precision_recall (presisi dan recall)](/en/terms/precision_recall-presisi-dan-recall/)
- [cross_validation (validasi silang)](/en/terms/cross_validation-validasi-silang/)
