---
title: Skjult lag
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
date: '2026-07-18T15:58:40.705496Z'
lastmod: '2026-07-18T16:38:07.008586Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: Et mellomliggende lag i et nevralt nettverk mellom inndata- og utdatalaget
  som prosesserer funksjoner.
---
## Definition

Et skjult lag består av nerver som mottar inndata fra tidligere lag, anvender vekter og bias, og sender transformert data videre gjennom en aktiveringsfunksjon. Disse lagene gjør det mulig for nevronale nettverk

### Summary

Et mellomliggende lag i et nevralt nettverk mellom inndata- og utdatalaget som prosesserer funksjoner.

## Key Concepts

- Nevrale nettverk
- Funksjonsekstraksjon
- Aktiveringsfunksjoner
- Dyp læring

## Use Cases

- Systemer for gjenkjenning av bilder
- Modeller for naturlig språkbehandling
- Prediktiv analyse

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

- [neuron (nevron)](/en/terms/neuron-nevron/)
- [backpropagation (bakoverpropagering)](/en/terms/backpropagation-bakoverpropagering/)
- [activation_function (aktiveringsfunksjon)](/en/terms/activation_function-aktiveringsfunksjon/)
- [deep_learning (dyp læring)](/en/terms/deep_learning-dyp-læring/)
