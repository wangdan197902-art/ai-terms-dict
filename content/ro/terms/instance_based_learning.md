---
title: "Învățarea bazată pe instanțe"
term_id: "instance_based_learning"
category: "training_techniques"
subcategory: ""
tags: ["algorithm", "lazy_learning", "classification"]
difficulty: 2
weight: 1
slug: "instance_based_learning"
aliases:
  - /ro/terms/instance_based_learning/
date: "2026-07-18T16:05:00.205028Z"
lastmod: "2026-07-18T17:15:09.669297Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "O abordare de învățare leneșă în care predicțiile sunt făcute comparând noile intrări cu instanțele de antrenament stocate."
---

## Definition

Cunoscută și sub numele de învățare bazată pe memorie, această tehnică nu construiește un model generalizat în timpul antrenamentului. În schimb, stochează întregul set de date de antrenament. Când este necesară o predicție, algoritmul găsește cele mai similare...

### Summary

O abordare de învățare leneșă în care predicțiile sunt făcute comparând noile intrări cu instanțele de antrenament stocate.

## Key Concepts

- Învățare leneșă
- Metrică de similaritate
- K-Cel Mai Apropiat Vecin (KNN)
- Bazat pe memorie

## Use Cases

- Sisteme de recomandare
- Recunoașterea tiparelor
- Seturi de date mici până la medii

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```

## Related Terms

- [KNN (K-Nearest Neighbors)](/en/terms/knn-k-nearest-neighbors/)
- [Căutare de similaritate](/en/terms/căutare-de-similaritate/)
- [Învățare leneșă](/en/terms/învățare-leneșă/)
- [Metode kernel](/en/terms/metode-kernel/)
