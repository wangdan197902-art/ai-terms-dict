---
title: "Apprendimento Supervisionato"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /it/terms/supervised_learning/
date: "2026-07-18T15:40:54.938675Z"
lastmod: "2026-07-18T17:15:08.590579Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Un paradigma di apprendimento automatico in cui un modello impara a mappare gli input agli output basandosi su esempi di addestramento etichettati."
---

## Definition

Nell'apprendimento supervisionato, l'algoritmo viene addestrato su un dataset etichettato, il che significa che ogni esempio di input è associato all'output corretto. L'obiettivo è permettere al modello di apprendere la relazione sottostante.

### Summary

Un paradigma di apprendimento automatico in cui un modello impara a mappare gli input agli output basandosi su esempi di addestramento etichettati.

## Key Concepts

- Dati Etichettati
- Mappatura Input-Output
- Classificazione
- Regressione

## Use Cases

- Rilevamento di email spam
- Previsione dei prezzi delle case
- Riconoscimento di immagini

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (apprendimento non supervisionato)](/en/terms/unsupervised-learning-apprendimento-non-supervisionato/)
- [Training Set (insieme di addestramento)](/en/terms/training-set-insieme-di-addestramento/)
- [Validation Set (insieme di validazione)](/en/terms/validation-set-insieme-di-validazione/)
- [Model Accuracy (accuratezza del modello)](/en/terms/model-accuracy-accuratezza-del-modello/)
