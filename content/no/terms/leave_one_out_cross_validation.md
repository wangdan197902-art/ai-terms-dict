---
title: "Korsvalidering med utelatt én observasjon"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /no/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:02:37.288905Z"
lastmod: "2026-07-18T16:38:07.018632Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En grundig resamplingsmetode der modellen trenes på alle unntatt én prøve og testes på den enkelt utelatte prøven, gjentatt for hvert datapunkt."
---

## Definition

Korsvalidering med utelatt én observasjon (LOOCV) er et spesielt tilfelle av k-fold korsvalidering der k er lik antall prøver i datasettet. Det gir en nesten ubestridelig estimat av modellens ytelse ved å bruke hver enkelt observasjon som testsett nøyaktig én gang, mens resten brukes til trening. Dette gir en lav skjevhet i estimatet, men kan være beregningsmessig kostbart.

### Summary

En grundig resamplingsmetode der modellen trenes på alle unntatt én prøve og testes på den enkelt utelatte prøven, gjentatt for hvert datapunkt.

## Key Concepts

- Resamplingsmetoder
- Modellvurdering
- Skjevhet-varians-handelsavtale
- Beregningsekostnad

## Use Cases

- Vurdering av modeller på små medisinske datasett
- Finjustering av hyperparametre når data er knappe
- Rigorøs sammenligning av algoritmenes ytelse

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

- [k-fold cross-validation (k-fold korsvalidering)](/en/terms/k-fold-cross-validation-k-fold-korsvalidering/)
- [train_test_split (trening-test-delning)](/en/terms/train_test_split-trening-test-delning/)
- [bootstrap (bootstrap-metoden)](/en/terms/bootstrap-bootstrap-metoden/)
- [cross_validation_score (korsvalideringsscore)](/en/terms/cross_validation_score-korsvalideringsscore/)
