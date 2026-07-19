---
title: Validasi silang leave-one-out
term_id: leave_one_out_cross_validation
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- evaluation
- statistics
difficulty: 3
weight: 1
slug: leave_one_out_cross_validation
date: '2026-07-18T15:57:56.933506Z'
lastmod: '2026-07-18T16:38:07.476872Z'
draft: false
source: agnes_llm
status: published
language: id
description: Teknik resampling yang ketat di mana model dilatih pada semua sampel
  kecuali satu dan diuji pada satu sampel yang disimpan tersebut, diulang untuk setiap
  titik data.
---
## Definition

Validasi silang leave-one-out (LOOCV) adalah kasus khusus dari validasi silang k-fold di mana k sama dengan jumlah sampel dalam dataset. Metode ini memberikan estimasi kinerja model yang hampir tidak bias.

### Summary

Teknik resampling yang ketat di mana model dilatih pada semua sampel kecuali satu dan diuji pada satu sampel yang disimpan tersebut, diulang untuk setiap titik data.

## Key Concepts

- Resampling
- Evaluasi Model
- Tradeoff Bias-Variansi
- Biaya Komputasi

## Use Cases

- Mengevaluasi model pada dataset medis kecil
- Penyetelan hiperparameter ketika data terbatas
- Membandingkan kinerja algoritma secara ketat

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (validasi silang k-fold)](/en/terms/k-fold-cross-validation-validasi-silang-k-fold/)
- [train_test_split (pemisahan data latih dan uji)](/en/terms/train_test_split-pemisahan-data-latih-dan-uji/)
- [bootstrap (teknik sampling ulang)](/en/terms/bootstrap-teknik-sampling-ulang/)
- [cross_validation_score (skor validasi silang)](/en/terms/cross_validation_score-skor-validasi-silang/)
