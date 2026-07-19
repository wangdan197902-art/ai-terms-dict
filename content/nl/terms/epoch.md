---
title: Epoch
term_id: epoch
category: training_techniques
subcategory: ''
tags:
- training
- Neural Networks
- basics
difficulty: 2
weight: 1
slug: epoch
date: '2026-07-18T15:54:18.101659Z'
lastmod: '2026-07-18T17:15:08.742521Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Één volledige doorloop van de trainingsdataset door het machine learning-algoritme
  tijdens het trainen van het model.
---
## Definition

In machine learning vertegenwoordigt een epoch een enkele iteratie over de gehele trainingsdataset. Tijdens elke epoch verwerkt het model alle trainingsvoorbeelden, update het zijn gewichten via backpropagatie en past het de hyperparameters aan om de prestaties te verbeteren.

### Summary

Één volledige doorloop van de trainingsdataset door het machine learning-algoritme tijdens het trainen van het model.

## Key Concepts

- Trainingsiteratie
- Backpropagatie
- Convergentie
- Hyperparameterafstelling

## Use Cases

- Configureren van neurale netwerktrainingslussen
- Monitoren van validatieverlies per cyclus
- Implementeren van vroege stopstrategieën

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

- [Batch Size (Baatgrootte)](/en/terms/batch-size-baatgrootte/)
- [Iteration (Iteratie)](/en/terms/iteration-iteratie/)
- [Learning Rate (Leersnelheid)](/en/terms/learning-rate-leersnelheid/)
- [Overfitting (Overfitting)](/en/terms/overfitting-overfitting/)
