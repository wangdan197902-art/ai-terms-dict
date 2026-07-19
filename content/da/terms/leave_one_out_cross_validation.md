---
title: Leave-one-out krydsvalidering
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
date: '2026-07-18T16:04:42.129358Z'
lastmod: '2026-07-18T17:15:09.304790Z'
draft: false
source: agnes_llm
status: published
language: da
description: En streng resamplingsmetode, hvor modellen trænes på alle data bortset
  fra én prøve og testes på denne enkelt udeladte prøve, gentaget for hvert datapunkt.
---
## Definition

Leave-one-out krydsvalidering (LOOCV) er et specifikt tilfælde af k-fold krydsvalidering, hvor k svarer til antallet af prøver i datasættet. Det giver et næsten ubiasserede estimat af modellens ydeevne.

### Summary

En streng resamplingsmetode, hvor modellen trænes på alle data bortset fra én prøve og testes på denne enkelt udeladte prøve, gentaget for hvert datapunkt.

## Key Concepts

- Resamling
- Modelvurdering
- Bias-varians tradeoff
- Databehandlingsomkostninger

## Use Cases

- Vurdering af modeller på små medicinske datasæt
- Finjustering af hyperparametre, når data er knappe
- Rigorøs sammenligning af algoritmeydeevne

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

- [k-fold krydsvalidering (en metode til at evaluere modellens evne til at generalisere ved at opdele data i k undergrupper)](/en/terms/k-fold-krydsvalidering-en-metode-til-at-evaluere-modellens-evne-til-at-generalisere-ved-at-opdele-data-i-k-undergrupper/)
- [train_test_split (opdeling af data i trænings- og testmængder)](/en/terms/train_test_split-opdeling-af-data-i-trænings-og-testmængder/)
- [bootstrap (en stikprøveudtagelsesmetode med tilbageplacering)](/en/terms/bootstrap-en-stikprøveudtagelsesmetode-med-tilbageplacering/)
- [cross_validation_score (en score, der beregnes gennem krydsvalidering)](/en/terms/cross_validation_score-en-score-der-beregnes-gennem-krydsvalidering/)
