---
title: "Tek Çıkararak Çapraz Doğrulama"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /tr/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:00:49.800268Z"
lastmod: "2026-07-18T16:38:07.327277Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Modelin tüm örneklerden biri hariç eğitildiği ve bu tek tutulan örnekte test edildiği, her veri noktası için tekrarlanan titiz bir yeniden örnekleme tekniğidir."
---

## Definition

Tek çıkararak çapraz doğrulama (LOOCV), k'nın veri setindeki örnek sayısına eşit olduğu k-katlı çapraz doğrulamanın özel bir durumudur. Model performansının neredeyse yanlısız bir tahminini sağlar.

### Summary

Modelin tüm örneklerden biri hariç eğitildiği ve bu tek tutulan örnekte test edildiği, her veri noktası için tekrarlanan titiz bir yeniden örnekleme tekniğidir.

## Key Concepts

- Yeniden Örnekleme
- Model Değerlendirme
- Yanlılık-Varyans Dengesi
- Hesaplama Maliyeti

## Use Cases

- Küçük tıbbi veri setlerinde modelleri değerlendirme
- Verinin kısıtlı olduğu durumlarda hiperparametre ayarlama
- Algoritma performansını titizlikle karşılaştırma

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

- [k-fold cross-validation (k-katlı çapraz doğrulama)](/en/terms/k-fold-cross-validation-k-katlı-çapraz-doğrulama/)
- [train_test_split (eğitim-test bölme)](/en/terms/train_test_split-eğitim-test-bölme/)
- [bootstrap (bootstrap yöntemi)](/en/terms/bootstrap-bootstrap-yöntemi/)
- [cross_validation_score (çapraz doğrulama skoru)](/en/terms/cross_validation_score-çapraz-doğrulama-skoru/)
