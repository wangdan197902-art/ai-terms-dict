---
title: "Uczenie nadzorowane"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /pl/terms/supervised_learning/
date: "2026-07-18T15:37:11.704019Z"
lastmod: "2026-07-18T17:15:08.837539Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Paradygmat uczenia maszynowego, w którym model uczy się mapować wejścia na wyjścia na podstawie oznaczonych przykładów treningowych."
---

## Definition

W uczeniu nadzorowanym algorytm jest trenowany na oznaczonym zbiorze danych, co oznacza, że każdy przykład wejściowy jest sparowany z poprawnym wyjściem. Celem jest nauczenie modelu podstawowej relacji między danymi wejściowymi a wyjściowymi.

### Summary

Paradygmat uczenia maszynowego, w którym model uczy się mapować wejścia na wyjścia na podstawie oznaczonych przykładów treningowych.

## Key Concepts

- Dane oznaczone
- Mapowanie wejście-wyjście
- Klasyfikacja
- Regresja

## Use Cases

- Wykrywanie spamu w e-mailach
- Prognozowanie cen nieruchomości
- Rozpoznawanie obrazów

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (uczenie nienadzorowane)](/en/terms/unsupervised-learning-uczenie-nienadzorowane/)
- [Training Set (zbiór treningowy)](/en/terms/training-set-zbiór-treningowy/)
- [Validation Set (zbiór walidacyjny)](/en/terms/validation-set-zbiór-walidacyjny/)
- [Model Accuracy (dokładność modelu)](/en/terms/model-accuracy-dokładność-modelu/)
