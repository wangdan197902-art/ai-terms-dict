---
title: Valvottu oppiminen
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T15:38:32.320024Z'
lastmod: '2026-07-18T17:15:09.375583Z'
draft: false
source: agnes_llm
status: published
language: fi
description: Konduktiivisen oppimisen paradigma, jossa malli oppii kuvaamaan syötteitä
  tuloksiksi merkittyjen koulutusaineistojen avulla.
---
## Definition

Valvotussa oppimisessa algoritmi koulutetaan merkityllä aineistolla, mikä tarkoittaa, että jokainen syöte-esimerkki on paritettu oikean tuloksen kanssa. Tavoitteena on, että malli oppii piilevän suhteen syötteen ja tuloksen välillä.

### Summary

Konduktiivisen oppimisen paradigma, jossa malli oppii kuvaamaan syötteitä tuloksiksi merkittyjen koulutusaineistojen avulla.

## Key Concepts

- Merkitty data
- Syöte-tulos-kuvaukset
- Luokittelu
- Regressio

## Use Cases

- Roskapostin tunnistus
- Asuntojen hintojen ennustaminen
- Kuvantunnistus

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Valvomaton oppiminen](/en/terms/valvomaton-oppiminen/)
- [Koulutusjoukko](/en/terms/koulutusjoukko/)
- [Validointijoukko](/en/terms/validointijoukko/)
- [Mallin tarkkuus](/en/terms/mallin-tarkkuus/)
