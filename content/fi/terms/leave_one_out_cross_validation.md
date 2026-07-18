---
title: "Yhden poissulkemisen ristiinvalidointi"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /fi/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:06:48.050000Z"
lastmod: "2026-07-18T17:15:09.428133Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Tiukka otantatekniikka, jossa malli opetetaan kaikilla muuttujilla paitsi yhdellä näytteellä ja testataan tällä yksittäisellä pidetyllä näytteellä, toistaen tämän jokaiselle datapisteele."
---

## Definition

Yhden poissulkemisen ristiinvalidointi (LOOCV) on k-otoksen ristiinvalidoinnin erikoistapaus, jossa k on yhtä suuri kuin otosjoukon näytteiden lukumäärä. Se tarjoaa lähes harjattoman arvion mallin suorituskyvystä.

### Summary

Tiukka otantatekniikka, jossa malli opetetaan kaikilla muuttujilla paitsi yhdellä näytteellä ja testataan tällä yksittäisellä pidetyllä näytteellä, toistaen tämän jokaiselle datapisteele.

## Key Concepts

- Otantatekniikka
- Mallin arviointi
- Harha-hajontavaihtoehto
- Laskennallinen kustannus

## Use Cases

- Mallien arviointi pienillä lääketieteellisillä datajoukoilla
- Hiperparametrien säätö, kun dataa on niukasti
- Algoritmien suorituskyvyn tiukka vertailu

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

- [k-otoksen ristiinvalidointi (yleinen menetelmä, jossa data jaetaan k:een osaan)](/en/terms/k-otoksen-ristiinvalidointi-yleinen-menetelmä-jossa-data-jaetaan-k-een-osaan/)
- [train_test_split (datan jakaminen harjoitus- ja testausjoukoksi)](/en/terms/train_test_split-datan-jakaminen-harjoitus-ja-testausjoukoksi/)
- [bootstrap (otanta menetelmä, jossa otoksia otetaan palauttaen)](/en/terms/bootstrap-otanta-menetelmä-jossa-otoksia-otetaan-palauttaen/)
- [cross_validation_score (ristiinvalidoinnilla laskettu arvosana)](/en/terms/cross_validation_score-ristiinvalidoinnilla-laskettu-arvosana/)
