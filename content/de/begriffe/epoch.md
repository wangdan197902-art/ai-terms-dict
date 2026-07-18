---
title: "Epoch"
term_id: "epoch"
category: "training_techniques"
subcategory: ""
tags: ["training", "neural_networks", "basics"]
difficulty: 2
weight: 1
slug: "epoch"
aliases:
  - /de/terms/epoch/
date: "2026-07-18T11:13:31.420946Z"
lastmod: "2026-07-18T11:44:44.937624Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Ein vollständiger Durchlauf des Trainingsdatensatzes durch den maschinellen Lernalgorithmus während des Modelltrainings."
---

## Definition

Im maschinellen Lernen repräsentiert eine Epoch eine einzelne Iteration über den gesamten Trainingsdatensatz. Während jeder Epoch verarbeitet das Modell alle Trainingsbeispiele, aktualisiert seine Gewichte mittels Backpropagation und passt die Parameter an, um die Vorhersagegenauigkeit zu verbessern.

### Summary

Ein vollständiger Durchlauf des Trainingsdatensatzes durch den maschinellen Lernalgorithmus während des Modelltrainings.

## Key Concepts

- Trainingsiteration
- Backpropagation
- Konvergenz
- Hyperparameter-Tuning

## Use Cases

- Konfiguration von Trainings-Schleifen neuronaler Netze
- Überwachung des Validierungsfehlers pro Zyklus
- Implementierung von Early-Stopping-Strategien

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Batch-Größe](/en/terms/batch-größe/)
- [Iteration](/en/terms/iteration/)
- [Lernrate](/en/terms/lernrate/)
- [Overfitting](/en/terms/overfitting/)
