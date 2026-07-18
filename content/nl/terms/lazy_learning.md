---
title: "Lazy learning"
term_id: "lazy_learning"
category: "training_techniques"
subcategory: ""
tags: ["algorithms", "training_methods", "machine_learning"]
difficulty: 2
weight: 1
slug: "lazy_learning"
aliases:
  - /nl/terms/lazy_learning/
date: "2026-07-18T16:02:56.116387Z"
lastmod: "2026-07-18T17:15:08.760834Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een leeraanpak die generalisatie uitstelt tot het moment van classificatie, waarbij trainingsinstanties worden opgeslagen in plaats van een expliciet model te bouwen."
---

## Definition

Lazy learners, zoals k-Nearest Neighbors (k-NN), onthouden de volledige trainingsdataset en voeren berekeningen alleen uit wanneer voorspellingen worden gedaan. Dit contrasteert met eager learning, dat een algemeen model bouwt voordat de training plaatsvindt.

### Summary

Een leeraanpak die generalisatie uitstelt tot het moment van classificatie, waarbij trainingsinstanties worden opgeslagen in plaats van een expliciet model te bouwen.

## Key Concepts

- Instance-Based Learning
- k-Nearest Neighbors
- Inferentiekosten
- Generalization

## Use Cases

- Aanbevelingssystemen
- Patroonherkenning in kleine datasets
- Prototyping van predictieve modellen

## Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)
```

## Related Terms

- [instance_based_learning (instance-based learning)](/en/terms/instance_based_learning-instance-based-learning/)
- [knn (k-naburige methode)](/en/terms/knn-k-naburige-methode/)
- [eager_learning (eager learning)](/en/terms/eager_learning-eager-learning/)
- [generalization (generalisatie)](/en/terms/generalization-generalisatie/)
