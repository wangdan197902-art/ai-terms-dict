---
title: "Nadzorowany"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
aliases:
  - /pl/terms/supervised/
date: "2026-07-18T15:29:55.028181Z"
lastmod: "2026-07-18T17:15:08.821919Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Paradygmat uczenia maszynowego, w którym modele są trenowane na parach wejście-wyjście z etykietami."
---

## Definition

Uczenie nadzorowane polega na podaniu algorytmowi danych, które zawierają zarówno wejścia, jak i poprawne odpowiedzi (etykiety). Model uczy się mapować wejścia na wyjścia poprzez minimalizację błędów predykcji. Ta technika...

### Summary

Paradygmat uczenia maszynowego, w którym modele są trenowane na parach wejście-wyjście z etykietami.

## Key Concepts

- Dane z etykietami
- Mapowanie
- Minimalizacja strat

## Use Cases

- Klasyfikacja obrazów
- Wykrywanie spamu
- Prognozowanie cen

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (Beznadzorowany)](/en/terms/unsupervised-beznadzorowany/)
- [Label (Etykieta)](/en/terms/label-etykieta/)
- [Regression (Regresja)](/en/terms/regression-regresja/)
