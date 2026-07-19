---
title: Κρυφή Στήλη
term_id: hidden_layer
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- Deep Learning
difficulty: 3
weight: 1
slug: hidden_layer
date: '2026-07-18T16:11:51.103949Z'
lastmod: '2026-07-18T17:15:09.916439Z'
draft: false
source: agnes_llm
status: published
language: el
description: Μια ενδιάμεση στήλη σε ένα νευρωνικό δίκτυο μεταξύ των στρωμάτων εισόδου
  και εξόδου που επεξεργάζεται χαρακτηριστικά.
---
## Definition

Μια κρυφή στήλη αποτελείται από νευρώνες που λαμβάνουν εισόδους από προηγούμενες στήλες, εφαρμόζουν βάρη και αποκλίσεις, και περνούν μετασχηματισμένα δεδομένα προς τα εμπρός μέσω μιας συνάρτησης ενεργοποίησης. Αυτές οι στήλες επιτρέπουν στα νευρωνικά δίκτυα.

### Summary

Μια ενδιάμεση στήλη σε ένα νευρωνικό δίκτυο μεταξύ των στρωμάτων εισόδου και εξόδου που επεξεργάζεται χαρακτηριστικά.

## Key Concepts

- Νευρωνικά Δίκτυα
- Εξαγωγή Χαρακτηριστικών
- Συναρτήσεις Ενεργοποίησης
- Βαθιά Μάθηση

## Use Cases

- Συστήματα αναγνώρισης εικόνας
- Μοντέλα φυσικής γλώσσας
- Προβλεπτική ανάλυση

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron (νευρώνας)](/en/terms/neuron-νευρώνας/)
- [backpropagation (οπισθοδιάδοση)](/en/terms/backpropagation-οπισθοδιάδοση/)
- [activation_function (συνάρτηση ενεργοποίησης)](/en/terms/activation_function-συνάρτηση-ενεργοποίησης/)
- [deep_learning (βαθιά μάθηση)](/en/terms/deep_learning-βαθιά-μάθηση/)
