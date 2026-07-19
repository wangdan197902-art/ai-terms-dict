---
title: Křížová validace metodou "vynechání jednoho"
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
date: '2026-07-18T16:05:50.902178Z'
lastmod: '2026-07-18T17:15:09.147557Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Přísnná technika resamplingu, při které je model trénován na všech vzorcích
  kromě jednoho a testován na tomto jednom vyňatém vzorku; proces se opakuje pro každý
  datový bod.
---
## Definition

Křížová validace metodou "vynechání jednoho" (LOOCV) je specifickým případem k-fold křížové validace, kde k odpovídá počtu vzorků v sadě dat. Poskytuje téměř nezaujatý odhad výkonu modelu.

### Summary

Přísnná technika resamplingu, při které je model trénován na všech vzorcích kromě jednoho a testován na tomto jednom vyňatém vzorku; proces se opakuje pro každý datový bod.

## Key Concepts

- Resampling
- Hodnocení modelu
- Kompromis mezi zkreslením a rozptylem
- Výpočetní náročnost

## Use Cases

- Hodnocení modelů na malých lékařských datech
- Ladění hyperparametrů při nedostatku dat
- Přísnné srovnávání výkonu algoritmů

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

- [k-fold cross-validation (k-fold křížová validace)](/en/terms/k-fold-cross-validation-k-fold-křížová-validace/)
- [train_test_split (rozdělení na trénovací a testovací sadu)](/en/terms/train_test_split-rozdělení-na-trénovací-a-testovací-sadu/)
- [bootstrap (bootstrapování)](/en/terms/bootstrap-bootstrapování/)
- [cross_validation_score (skóre křížové validace)](/en/terms/cross_validation_score-skóre-křížové-validace/)
