---
title: "Leave-one-out-crossvalidering"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /sv/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:06:48.737918Z"
lastmod: "2026-07-18T17:15:09.020562Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "En rigorös resampling-teknik där modellen tränas på alla utom ett prov och testas på det enskilda borttagna provet, upprepat för varje datapunkt."
---

## Definition

Leave-one-out-crossvalidering (LOOCV) är ett specifikt fall av k-faldig crossvalidering där k är lika med antalet prover i datamängden. Den ger en nästan opartisk uppskattning av modellens prestanda genom att iterativt använda varje enskild observation som valideringsset medan de återstående används för träning.

### Summary

En rigorös resampling-teknik där modellen tränas på alla utom ett prov och testas på det enskilda borttagna provet, upprepat för varje datapunkt.

## Key Concepts

- Resampling
- Modellutvärdering
- Bias-varians-tradeoff
- Beräkningskostnad

## Use Cases

- Utvärdering av modeller på små medicinska datamängder
- Hyperparameteroptimering när data är bristfällig
- Rigorös jämförelse av algoritmers prestanda

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

- [k-fold cross-validation (k-faldig crossvalidering)](/en/terms/k-fold-cross-validation-k-faldig-crossvalidering/)
- [train_test_split (uppdelning i tränings- och testdata)](/en/terms/train_test_split-uppdelning-i-tränings-och-testdata/)
- [bootstrap (bootstrapmetoden)](/en/terms/bootstrap-bootstrapmetoden/)
- [cross_validation_score (crossvalideringspoäng)](/en/terms/cross_validation_score-crossvalideringspoäng/)
