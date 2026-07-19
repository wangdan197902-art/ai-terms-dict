---
title: Rețea cu propagare înainte
term_id: feed_forward_network
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- fundamentals
difficulty: 2
weight: 1
slug: feed_forward_network
date: '2026-07-18T15:58:24.013451Z'
lastmod: '2026-07-18T17:15:09.656356Z'
draft: false
source: agnes_llm
status: published
language: ro
description: O clasă de rețele neuronale artificiale în care conexiunile dintre noduri
  nu formează cicluri, propagând informația într-o singură direcție.
---
## Definition

Rețelele cu Propagare Înainte (FFN), cunoscute și sub numele de Perceptroni Multistrat (MLP), procesează datele secvențial prin straturi de neuroni, de la intrare la ieșire, fără bucle de feedback. Fiecare neuron primește intrări, le ponderază, aplică o funcție de activare și transmite rezultatul stratului următor.

### Summary

O clasă de rețele neuronale artificiale în care conexiunile dintre noduri nu formează cicluri, propagând informația într-o singură direcție.

## Key Concepts

- Fără cicluri
- Straturi (Intrare, Ascuns, Ieșire)
- Funcții de activare
- Sume ponderate

## Use Cases

- Sarcini simple de regresie
- Probleme de clasificare cu date tabulare
- Blocuri de construcție pentru arhitecturi mai profunde

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Perceptron Multistrat (Multi-Layer Perceptron)](/en/terms/perceptron-multistrat-multi-layer-perceptron/)
- [Propagarea înapoi (Backpropagation)](/en/terms/propagarea-înapoi-backpropagation/)
- [Funcție de activare (Activation Function)](/en/terms/funcție-de-activare-activation-function/)
- [Rețea neuronală (Neural Network)](/en/terms/rețea-neuronală-neural-network/)
