---
title: Lazy learning (passiv læring)
term_id: lazy_learning
category: training_techniques
subcategory: ''
tags:
- algorithms
- Training Methods
- Machine Learning
difficulty: 2
weight: 1
slug: lazy_learning
date: '2026-07-18T16:04:07.970239Z'
lastmod: '2026-07-18T17:15:09.304102Z'
draft: false
source: agnes_llm
status: published
language: da
description: En læringstilgang, der udskyder generalisering til klassificeringstidspunktet
  ved at gemme træningsinstanser frem for at bygge en eksplicit model.
---
## Definition

Lazy learners, såsom k-Nearest Neighbors (k-NN), husker hele træningsdatasættet og udfører beregninger først, når de laver forudsigelser. Dette står i kontrast til eager learning (aktiv læring), der bygger en generaliseret model under træningsfasen.

### Summary

En læringstilgang, der udskyder generalisering til klassificeringstidspunktet ved at gemme træningsinstanser frem for at bygge en eksplicit model.

## Key Concepts

- Instansbaseret læring
- k-Nearest Neighbors (k-NN)
- Inferensomkostning
- Generalisering

## Use Cases

- Anbefalingssystemer
- Mønstergenkendelse i små datasæt
- Prototyping af prediktive modeller

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)
```

## Related Terms

- [instance_based_learning (instansbaseret læring)](/en/terms/instance_based_learning-instansbaseret-læring/)
- [knn (k-NN)](/en/terms/knn-k-nn/)
- [eager_learning (aktiv læring)](/en/terms/eager_learning-aktiv-læring/)
- [generalization (generalisering)](/en/terms/generalization-generalisering/)
