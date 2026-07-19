---
title: Uczenie oparte na eksemplarzach
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
date: '2026-07-18T16:00:17.460378Z'
lastmod: '2026-07-18T17:15:08.886244Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Podejście leniwego uczenia, w którym predykcje są dokonywane poprzez
  porównywanie nowych danych wejściowych do przechowywanych eksemplarzy treningowych.
---
## Definition

Znane również jako uczenie oparte na pamięci, ta technika nie buduje uogólnionego modelu podczas treningu. Zamiast tego przechowuje cały zbiór danych treningowych. Gdy potrzebna jest predykcja, znajduje najbardziej s

### Summary

Podejście leniwego uczenia, w którym predykcje są dokonywane poprzez porównywanie nowych danych wejściowych do przechowywanych eksemplarzy treningowych.

## Key Concepts

- Leniwe uczenie
- Miara podobieństwa
- K-Nearest Neighbors (K-Najbliższych Sąsiadów)
- Opieranie na pamięci

## Use Cases

- Systemy rekomendacyjne
- Rozpoznawanie wzorców
- Małe do średnich zbiorów danych

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```

## Related Terms

- [KNN (Algorytm K-Najbliższych Sąsiadów)](/en/terms/knn-algorytm-k-najbliższych-sąsiadów/)
- [Similarity search (Wyszukiwanie podobieństw)](/en/terms/similarity-search-wyszukiwanie-podobieństw/)
- [Lazy learning (Leniwe uczenie)](/en/terms/lazy-learning-leniwe-uczenie/)
- [Kernel methods (Metody jądrowe)](/en/terms/kernel-methods-metody-jądrowe/)
