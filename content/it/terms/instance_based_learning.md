---
title: Apprendimento basato su istanze
term_id: instance_based_learning
category: training_techniques
subcategory: ''
tags:
- algorithm
- Lazy Learning
- Classification
difficulty: 2
weight: 1
slug: instance_based_learning
date: '2026-07-18T16:04:55.190534Z'
lastmod: '2026-07-18T17:15:08.637845Z'
draft: false
source: agnes_llm
status: published
language: it
description: Un approccio di apprendimento pigro in cui le previsioni vengono effettuate
  confrontando nuovi input con le istanze di addestramento memorizzate.
---
## Definition

Conosciuto anche come apprendimento basato sulla memoria, questa tecnica non costruisce un modello generalizzato durante l'addestramento. Memorizza invece l'intero dataset di addestramento. Quando è necessaria una previsione, trova le istanze più simili all'input.

### Summary

Un approccio di apprendimento pigro in cui le previsioni vengono effettuate confrontando nuovi input con le istanze di addestramento memorizzate.

## Key Concepts

- Apprendimento pigro
- Metrica di similarità
- K-Nearest Neighbors (K-NN)
- Basato sulla memoria

## Use Cases

- Sistemi di raccomandazione
- Riconoscimento di pattern
- Dataset di piccole e medie dimensioni

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```

## Related Terms

- [KNN (K-Nearest Neighbors / K-Vicini Più Prossimi)](/en/terms/knn-k-nearest-neighbors-k-vicini-più-prossimi/)
- [Similarity search (Ricerca per similarità)](/en/terms/similarity-search-ricerca-per-similarità/)
- [Lazy learning (Apprendimento pigro)](/en/terms/lazy-learning-apprendimento-pigro/)
- [Kernel methods (Metodi kernel)](/en/terms/kernel-methods-metodi-kernel/)
