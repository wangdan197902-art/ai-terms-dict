---
title: "Merkitty data"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /fi/terms/labeled_data/
date: "2026-07-18T16:06:12.544202Z"
lastmod: "2026-07-18T17:15:09.426831Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Dataa, jossa oikea lähtöarvo tai kohdearvo on annettu syötteiden ominaisuuksien lisäksi."
---

## Definition

Merkitty data koostuu syötenäytteistä, joihin on liitetty vastaavat totuudenmukaiset tunnisteet, ja se muodostaa valvottua koneoppimisen perustan. Se mahdollistaa algoritmien oppia kuvaajan syötteen ja tuloksen välillä.

### Summary

Dataa, jossa oikea lähtöarvo tai kohdearvo on annettu syötteiden ominaisuuksien lisäksi.

## Key Concepts

- Valvottu oppiminen
- Totuusarvo
- Annotointi
- Kohdemuuttuja

## Use Cases

- Kuvien luokittelijoiden koulutus
- Puheentunnistusjärjestelmien rakentaminen
- Ennakoiva mallinnus rahoituksessa

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (merkitsemätön data)](/en/terms/unlabeled_data-merkitsemätön-data/)
- [supervised_learning (valvottu oppiminen)](/en/terms/supervised_learning-valvottu-oppiminen/)
- [data_annotation (datan annotointi)](/en/terms/data_annotation-datan-annotointi/)
- [training_set (harjoitusjoukko)](/en/terms/training_set-harjoitusjoukko/)
