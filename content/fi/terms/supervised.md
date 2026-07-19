---
title: "Valvottu"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
date: "2026-07-18T15:31:25.815279Z"
lastmod: "2026-07-18T17:15:09.360394Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Oppimismuoto, jossa malleja koulutetaan merkittyjen syöte-lähtö-parien avulla."
---
## Definition

Valvottu oppiminen sisältää algoritmin syöttämisen datalla, joka sisältää sekä syötteet että oikeat vastaukset (merkinnät). Malli oppii kuvaamaan syötteet lähdöiksi minimoimalla ennustusvirheet. Tämä tekn...

### Summary

Oppimismuoto, jossa malleja koulutetaan merkittyjen syöte-lähtö-parien avulla.

## Key Concepts

- Merkitty data
- Kuvaus
- Häviön minimointi

## Use Cases

- Kuvien luokittelu
- Roskapostin tunnistus
- Hintojen ennustaminen

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (Valvomaton)](/en/terms/unsupervised-valvomaton/)
- [Label (Merkintä)](/en/terms/label-merkintä/)
- [Regression (Regressio)](/en/terms/regression-regressio/)
