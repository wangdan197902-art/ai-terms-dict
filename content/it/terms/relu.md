---
title: ReLU
term_id: relu
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Activation Functions
- Deep Learning
difficulty: 3
weight: 1
slug: relu
date: '2026-07-18T15:37:31.194404Z'
lastmod: '2026-07-18T17:15:08.589343Z'
draft: false
source: agnes_llm
status: published
language: it
description: La funzione unitaria lineare rettificata (ReLU) è una funzione di attivazione
  che restituisce l'input direttamente se positivo, altrimenti zero.
---
## Definition

ReLU è ampiamente utilizzata nelle reti neurali profonde grazie alla sua efficienza computazionale e alla capacità di mitigare il problema del gradiente nullo. Matematicamente definita come f(x) = max(0, x), introduce non linearità nella rete permettendo l'apprendimento di pattern complessi.

### Summary

La funzione unitaria lineare rettificata (ReLU) è una funzione di attivazione che restituisce l'input direttamente se positivo, altrimenti zero.

## Key Concepts

- Non linearità
- Funzione di attivazione
- Gradiente nullo (Vanishing Gradient)
- Funzione lineare a tratti

## Use Cases

- Strati nascosti nelle CNN (Reti Neurali Convoluzionali)
- Reti feedforward profonde
- Modelli di riconoscimento di immagini

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (funzione di attivazione sigmoide)](/en/terms/sigmoid-funzione-di-attivazione-sigmoide/)
- [Tanh (funzione di attivazione tangente iperbolica)](/en/terms/tanh-funzione-di-attivazione-tangente-iperbolica/)
- [Leaky ReLU (variante della ReLU)](/en/terms/leaky-relu-variante-della-relu/)
- [Neural Network (Rete neurale)](/en/terms/neural-network-rete-neurale/)
