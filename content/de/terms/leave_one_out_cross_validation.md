---
title: Leave-One-Out-Cross-Validation
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
date: '2026-07-18T11:21:34.994988Z'
lastmod: '2026-07-18T11:44:44.958183Z'
draft: false
source: agnes_llm
status: published
language: de
description: Eine strenge Resampling-Technik, bei der das Modell mit allen bis auf
  eine Stichprobe trainiert und mit dieser einzelnen zurückgehaltenen Stichprobe getestet
  wird, wobei dieser Vorgang für jeden Daten
---
## Definition

Die Leave-One-Out-Cross-Validation (LOOCV) ist ein spezieller Fall der k-Fold-Cross-Validation, bei dem k gleich der Anzahl der Stichproben im Datensatz ist. Sie liefert eine nahezu unverzerrte Schätzung der Modellleistung, indem...

### Summary

Eine strenge Resampling-Technik, bei der das Modell mit allen bis auf eine Stichprobe trainiert und mit dieser einzelnen zurückgehaltenen Stichprobe getestet wird, wobei dieser Vorgang für jeden Datenpunkt wiederholt wird.

## Key Concepts

- Resampling
- Modellbewertung
- Bias-Varianz-Kompromiss
- Berechnungskosten

## Use Cases

- Bewertung von Modellen auf kleinen medizinischen Datensätzen
- Hyperparameter-Tuning bei knappen Daten
- Strenge Vergleich der Algorithmenleistung

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

- [k-fold cross-validation (k-Fold-Cross-Validation)](/en/terms/k-fold-cross-validation-k-fold-cross-validation/)
- [train_test_split (Train-Test-Aufteilung)](/en/terms/train_test_split-train-test-aufteilung/)
- [bootstrap (Bootstrapping)](/en/terms/bootstrap-bootstrapping/)
- [cross_validation_score (Cross-Validation-Score)](/en/terms/cross_validation_score-cross-validation-score/)
