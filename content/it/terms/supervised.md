---
title: "Supervisionato"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
aliases:
  - /it/terms/supervised/
date: "2026-07-18T15:29:39.936073Z"
lastmod: "2026-07-18T17:15:08.575429Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Un paradigma di apprendimento automatico in cui i modelli vengono addestrati su coppie di input-output etichettate."
---

## Definition

L'apprendimento supervisionato implica l'alimentazione di un algoritmo con dati che includono sia input che risposte corrette (etichette). Il modello impara a mappare gli input agli output minimizzando gli errori di previsione. Questa tecnica è ampiamente utilizzata per compiti di classificazione e regressione.

### Summary

Un paradigma di apprendimento automatico in cui i modelli vengono addestrati su coppie di input-output etichettate.

## Key Concepts

- Dati etichettati
- Mappatura
- Minimizzazione della perdita

## Use Cases

- Classificazione di immagini
- Rilevamento dello spam
- Previsione dei prezzi

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Non supervisionato (apprendimento senza etichette)](/en/terms/non-supervisionato-apprendimento-senza-etichette/)
- [Etichetta (il valore target corretto)](/en/terms/etichetta-il-valore-target-corretto/)
- [Regressione (previsione di valori continui)](/en/terms/regressione-previsione-di-valori-continui/)
