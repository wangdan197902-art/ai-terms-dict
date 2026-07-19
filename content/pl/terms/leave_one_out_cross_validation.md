---
title: Walidacja krzyżowa typu leave-one-out
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
date: '2026-07-18T16:03:57.818447Z'
lastmod: '2026-07-18T17:15:08.891544Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Rygorystyczna technika próbkowania ponownego, w której model jest trenowany
  na wszystkich próbach z wyjątkiem jednej i testowany na tej pojedynczej, pominiętej
  próbce, co powtarzane jest dla każdego p
---
## Definition

Walidacja krzyżowa typu leave-one-out (LOOCV) jest szczególnym przypadkiem walidacji krzyżowej k-fold, gdzie k jest równe liczbie próbek w zbiorze danych. Zapewnia ona niemal nieobciążoną estymację wydajności modelu, ponieważ każda próbka jest używana dokładnie raz jako zbiór testowy.

### Summary

Rygorystyczna technika próbkowania ponownego, w której model jest trenowany na wszystkich próbach z wyjątkiem jednej i testowany na tej pojedynczej, pominiętej próbce, co powtarzane jest dla każdego punktu danych.

## Key Concepts

- Próbkowanie ponowne
- Ocena modelu
- Kompromis między biasem a wariancją
- Koszt obliczeniowy

## Use Cases

- Ewaluacja modeli na małych zestawach danych medycznych
- Dopasowywanie hiperparametrów przy ograniczonej ilości danych
- Rygorystyczne porównanie wydajności algorytmów

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

- [k-fold cross-validation (walidacja krzyżowa k-fold)](/en/terms/k-fold-cross-validation-walidacja-krzyżowa-k-fold/)
- [train_test_split (podział na zbiór treningowy i testowy)](/en/terms/train_test_split-podział-na-zbiór-treningowy-i-testowy/)
- [bootstrap (metoda bootstrap)](/en/terms/bootstrap-metoda-bootstrap/)
- [cross_validation_score (wynik walidacji krzyżowej)](/en/terms/cross_validation_score-wynik-walidacji-krzyżowej/)
