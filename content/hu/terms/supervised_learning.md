---
title: "Felügyelt tanulás"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /hu/terms/supervised_learning/
date: "2026-07-18T15:39:55.777452Z"
lastmod: "2026-07-18T17:15:09.745804Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy gépi tanulási paradigmában a modell a címkézett példák alapján tanulja meg a bemenetek és kimenetek közötti leképezést."
---

## Definition

A felügyelt tanulásban az algoritmust egy címkézett adathalmon tanítják, ami azt jelenti, hogy minden bemeneti példa párosul a helyes kimenettel. A cél, hogy a modell megtanulja a mögöttes kapcsolatot.

### Summary

Egy gépi tanulási paradigmában a modell a címkézett példák alapján tanulja meg a bemenetek és kimenetek közötti leképezést.

## Key Concepts

- Címkézett adat
- Bemenet-kimenet leképezés
- Besorolás (Classification)
- Regresszió

## Use Cases

- Spam e-mailek észlelése
- Ingatlanárak előrejelzése
- Képfelismerés

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Felügyelet nélküli tanulás](/en/terms/felügyelet-nélküli-tanulás/)
- [Tanítóhalmaz](/en/terms/tanítóhalmaz/)
- [Validációs halmaz](/en/terms/validációs-halmaz/)
- [Modell pontosság](/en/terms/modell-pontosság/)
