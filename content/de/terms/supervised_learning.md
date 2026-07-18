---
title: "Überwachtes Lernen"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /de/terms/supervised_learning/
date: "2026-07-18T11:00:05.256712Z"
lastmod: "2026-07-18T11:44:44.900760Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Ein Paradigma des maschinellen Lernens, bei dem ein Modell anhand beschrifteter Trainingsbeispiele lernt, Eingaben Ausgaben zuzuordnen."
---

## Definition

Beim überwachten Lernen wird der Algorithmus mit einem beschrifteten Datensatz trainiert, was bedeutet, dass jedem Eingabebeispiel die korrekte Ausgabe zugeordnet ist. Das Ziel besteht darin, dass das Modell die zugrunde liegende Beziehung zwischen Eingabe und Ausgabe lernt.

### Summary

Ein Paradigma des maschinellen Lernens, bei dem ein Modell anhand beschrifteter Trainingsbeispiele lernt, Eingaben Ausgaben zuzuordnen.

## Key Concepts

- Beschriftete Daten
- Eingabe-Ausgabe-Zuordnung
- Klassifizierung
- Regression

## Use Cases

- Erkennung von Spam-E-Mails
- Vorhersage von Hauspreisen
- Bilderkennung

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (Unüberwachtes Lernen)](/en/terms/unsupervised-learning-unüberwachtes-lernen/)
- [Training Set (Trainingsdatensatz)](/en/terms/training-set-trainingsdatensatz/)
- [Validation Set (Validierungsdatensatz)](/en/terms/validation-set-validierungsdatensatz/)
- [Model Accuracy (Modellgenauigkeit)](/en/terms/model-accuracy-modellgenauigkeit/)
