---
title: Validazione incrociata leave-one-out
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
date: '2026-07-18T16:08:01.928377Z'
lastmod: '2026-07-18T17:15:08.643023Z'
draft: false
source: agnes_llm
status: published
language: it
description: Una tecnica rigorosa di ricampionamento in cui il modello viene addestrato
  su tutti i dati tranne uno e testato su quell'unico campione escluso, ripetuto per
  ogni punto dati.
---
## Definition

La validazione incrociata leave-one-out (LOOCV) è un caso specifico della validazione incrociata k-fold in cui k è uguale al numero di campioni nel dataset. Fornisce una stima quasi non distorta delle prestazioni del modello.

### Summary

Una tecnica rigorosa di ricampionamento in cui il modello viene addestrato su tutti i dati tranne uno e testato su quell'unico campione escluso, ripetuto per ogni punto dati.

## Key Concepts

- Ricampionamento
- Valutazione del modello
- Trade-off bias-varianza
- Costo computazionale

## Use Cases

- Valutazione di modelli su piccoli dataset medici
- Ottimizzazione degli iperparametri quando i dati sono scarsi
- Confronto rigoroso delle prestazioni degli algoritmi

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

- [k-fold cross-validation (validazione incrociata k-fold)](/en/terms/k-fold-cross-validation-validazione-incrociata-k-fold/)
- [train_test_split (divisione train/test)](/en/terms/train_test_split-divisione-train-test/)
- [bootstrap (bootstrap)](/en/terms/bootstrap-bootstrap/)
- [cross_validation_score (punteggio validazione incrociata)](/en/terms/cross_validation_score-punteggio-validazione-incrociata/)
