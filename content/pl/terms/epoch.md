---
title: Epoka
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
date: '2026-07-18T15:53:42.345012Z'
lastmod: '2026-07-18T17:15:08.871088Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Jedno pełne przejście zbioru danych treningowych przez algorytm uczenia
  maszynowego podczas trenowania modelu.
---
## Definition

W uczeniu maszynowym epoka reprezentuje jedną pełną iterację po całym zbiorze danych treningowych. Podczas każdej epoki model przetwarza wszystkie przykłady treningowe, aktualizuje swoje wagi poprzez propagację wsteczną i dostosowuje parametry.

### Summary

Jedno pełne przejście zbioru danych treningowych przez algorytm uczenia maszynowego podczas trenowania modelu.

## Key Concepts

- Iteracja treningowa
- Propagacja wsteczna
- Konwergencja
- Dopasowanie hiperparametrów

## Use Cases

- Konfigurowanie pętli treningowych sieci neuronowych
- Monitorowanie strat walidacyjnych w każdym cyklu
- Wdrażanie strategii wcześniejszego zatrzymania (early stopping)

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

- [Rozmiar partii (Batch Size)](/en/terms/rozmiar-partii-batch-size/)
- [Iteracja](/en/terms/iteracja/)
- [Współczynnik uczenia (Learning Rate)](/en/terms/współczynnik-uczenia-learning-rate/)
- [Przetrenowanie (Overfitting)](/en/terms/przetrenowanie-overfitting/)
