---
title: Skjult Lag
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
date: '2026-07-18T15:59:53.982821Z'
lastmod: '2026-07-18T17:15:09.295799Z'
draft: false
source: agnes_llm
status: published
language: da
description: Et mellemliggende lag i et neuralt netværk mellem input- og outputlagene,
  der behandler funktioner.
---
## Definition

Et skjult lag består af neuroner, der modtager input fra tidligere lag, anvender vægte og bias-værdier og sender transformeret data videre gennem en aktiveringsfunktion. Disse lag gør det muligt for neurale netværk at

### Summary

Et mellemliggende lag i et neuralt netværk mellem input- og outputlagene, der behandler funktioner.

## Key Concepts

- Neurale Netværk
- Funktionsekstraktion
- Aktiveringsfunktioner
- Dyb Læring

## Use Cases

- Systemer til billedgenkendelse
- Modeller til naturlig sprogbehandling
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

- [neuron (neuron)](/en/terms/neuron-neuron/)
- [backpropagation (bagudpropagering)](/en/terms/backpropagation-bagudpropagering/)
- [activation_function (aktiveringsfunktion)](/en/terms/activation_function-aktiveringsfunktion/)
- [deep_learning (dyb læring)](/en/terms/deep_learning-dyb-læring/)
