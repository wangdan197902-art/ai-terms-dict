---
title: "Overvåket læring"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /no/terms/supervised_learning/
date: "2026-07-18T15:38:52.976140Z"
lastmod: "2026-07-18T16:38:06.963296Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Et maskinlæringsparadigme der en modell lærer å kartlegge inndata til utdata basert på merkte trenings eksempler."
---

## Definition

I overvåket læring trenes algoritmen på et merkt datasett, noe som betyr at hvert inndataeksempel er parret med riktig utdata. Målet er at modellen skal lære det underliggende forholdet mellom inndata og utdata.

### Summary

Et maskinlæringsparadigme der en modell lærer å kartlegge inndata til utdata basert på merkte trenings eksempler.

## Key Concepts

- Merkte data
- Inndata-utdata-kartlegging
- Klassifisering
- Regresjon

## Use Cases

- Oppdagelse av spam-e-post
- Prediksjon av huspriser
- Bilderekognisjon

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Uovervåket læring (læring uten merkte data)](/en/terms/uovervåket-læring-læring-uten-merkte-data/)
- [Treningssett (delen av dataen brukt til å trene modellen)](/en/terms/treningssett-delen-av-dataen-brukt-til-å-trene-modellen/)
- [Valideringssett (delen av dataen brukt til å justere hyperparametre)](/en/terms/valideringssett-delen-av-dataen-brukt-til-å-justere-hyperparametre/)
- [Modellnøyaktighet (mål på hvor godt modellen predikerer)](/en/terms/modellnøyaktighet-mål-på-hvor-godt-modellen-predikerer/)
