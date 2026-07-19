---
title: "Felügyelt"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
date: "2026-07-18T15:31:33.974555Z"
lastmod: "2026-07-18T17:15:09.731090Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy gépi tanulási paradigm, ahol a modelleket címkézett bemenet-kimenet párokkal tanítják."
---
## Definition

A felügyelt tanulás során az algoritmust olyan adatokkal etetik, amelyek tartalmazzák a bemeneteket és a helyes válaszokat (címkéket). A modell a predikciós hibák minimalizálásával tanulja meg leképezni a bemeneteket a kimenetekre.

### Summary

Egy gépi tanulási paradigm, ahol a modelleket címkézett bemenet-kimenet párokkal tanítják.

## Key Concepts

- Címkézett adat
- Leképezés
- Veszteségminimalizálás

## Use Cases

- Képosztályozás
- Spam-szűrés
- Árelőrejelzés

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (felügyelet nélküli)](/en/terms/unsupervised-felügyelet-nélküli/)
- [Label (címke)](/en/terms/label-címke/)
- [Regression (regresszió)](/en/terms/regression-regresszió/)
