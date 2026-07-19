---
title: Validare încrucișată „leave-one-out”
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
date: '2026-07-18T16:08:34.181706Z'
lastmod: '2026-07-18T17:15:09.674650Z'
draft: false
source: agnes_llm
status: published
language: ro
description: O tehnică riguroasă de reeșantionare în care modelul este antrenat pe
  toate eșantioanele cu excepția unuia, fiind testat pe acel singur eșantion exclus,
  proces repetat pentru fiecare punct de date.
---
## Definition

Validarea încrucișată „leave-one-out” (LOOCV) este un caz specific al validării încrucișate k-fold, unde k este egal cu numărul de eșantioane din setul de date. Aceasta oferă o estimare aproape neîmproprietată a performanței modelului, deoarece fiecare observație este folosită o dată ca și set de testare.

### Summary

O tehnică riguroasă de reeșantionare în care modelul este antrenat pe toate eșantioanele cu excepția unuia, fiind testat pe acel singur eșantion exclus, proces repetat pentru fiecare punct de date.

## Key Concepts

- Reeșantionare
- Evaluarea modelului
- Compromis bias-varianță
- Cost computațional

## Use Cases

- Evaluarea modelelor pe seturi de date medicale mici
- Reglarea hiperparametrilor când datele sunt limitate
- Compararea riguroasă a performanței algoritmilor

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

- [validare încrucișată k-fold](/en/terms/validare-încrucișată-k-fold/)
- [train_test_split (împărțirea datelor în antrenament și test)](/en/terms/train_test_split-împărțirea-datelor-în-antrenament-și-test/)
- [bootstrap (metodă de reeșantionare cu revenire)](/en/terms/bootstrap-metodă-de-reeșantionare-cu-revenire/)
- [cross_validation_score (scorul de validare încrucișată)](/en/terms/cross_validation_score-scorul-de-validare-încrucișată/)
