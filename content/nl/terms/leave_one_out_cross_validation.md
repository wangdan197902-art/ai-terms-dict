---
title: "Cross-validatie met één uitgesloten steekproef"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /nl/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:04:29.089140Z"
lastmod: "2026-07-18T17:15:08.761594Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een rigoureuze resampling-techniek waarbij het model wordt getraind op alle steekproeven behalve één, en getest op die ene achtergehouden steekproef, herhaald voor elk datapunt."
---

## Definition

Cross-validatie met één uitgesloten steekproef (LOOCV) is een specifiek geval van k-voudige cross-validatie waarbij k gelijk is aan het aantal steekproeven in de dataset. Het biedt een bijna onbevooroordeeld schatting van de modelprestaties door elke steekproef één keer als testset te gebruiken terwijl de rest als trainingsset dient.

### Summary

Een rigoureuze resampling-techniek waarbij het model wordt getraind op alle steekproeven behalve één, en getest op die ene achtergehouden steekproef, herhaald voor elk datapunt.

## Key Concepts

- Resampling
- Modelbeoordeling
- Bias-varianceafweging
- Rekenkosten

## Use Cases

- Beoordelen van modellen op kleine medische datasets
- Afstemmen van hyperparameters wanneer gegevens schaars zijn
- Strikt vergelijken van algoritme-prestaties

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

- [k-fold cross-validation (k-voudige cross-validatie)](/en/terms/k-fold-cross-validation-k-voudige-cross-validatie/)
- [train_test_split (verdeling in train- en testset)](/en/terms/train_test_split-verdeling-in-train-en-testset/)
- [bootstrap (bootstrap-resampling)](/en/terms/bootstrap-bootstrap-resampling/)
- [cross_validation_score (cross-validatiescore)](/en/terms/cross_validation_score-cross-validatiescore/)
