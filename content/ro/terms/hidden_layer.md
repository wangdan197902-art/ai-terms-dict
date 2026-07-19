---
title: Strat Ascuns
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
date: '2026-07-18T16:02:17.351536Z'
lastmod: '2026-07-18T17:15:09.664291Z'
draft: false
source: agnes_llm
status: published
language: ro
description: Un strat intermediar într-o rețea neuronală, situat între straturile
  de intrare și ieșire, care procesează caracteristici.
---
## Definition

Un strat ascuns constă din neuroni care primesc intrări de la straturile anterioare, aplică ponderi și bias-uri, și transmit datele transformate mai departe printr-o funcție de activare. Aceste straturi permit rețelelor neuronale să învețe reprezentări complexe.

### Summary

Un strat intermediar într-o rețea neuronală, situat între straturile de intrare și ieșire, care procesează caracteristici.

## Key Concepts

- Rețele Neurale
- Extragerea Caracteristicilor
- Funcții de Activare
- Învățare Profundă

## Use Cases

- Sisteme de recunoaștere a imaginilor
- Modele de procesare a limbajului natural
- Analitică predictivă

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

- [neuron (neurón)](/en/terms/neuron-neurón/)
- [backpropagation (propagare inversă)](/en/terms/backpropagation-propagare-inversă/)
- [activation_function (funcție de activare)](/en/terms/activation_function-funcție-de-activare/)
- [deep_learning (învățare profundă)](/en/terms/deep_learning-învățare-profundă/)
