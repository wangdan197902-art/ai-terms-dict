---
title: Feed-Forward Network
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
date: '2026-07-18T15:59:38.684337Z'
lastmod: '2026-07-18T17:15:08.626039Z'
draft: false
source: agnes_llm
status: published
language: it
description: Una classe di rete neurale artificiale in cui le connessioni tra i nodi
  non formano cicli, propagando le informazioni in una sola direzione.
---
## Definition

Le Feed-Forward Networks (FFN), note anche come Multi-Layer Perceptrons (MLP), elaborano i dati sequenzialmente attraverso strati di neuroni dall'input all'output senza loop di feedback. Ogni neurone riceve input, li combina tramite somme pesate e applica una funzione di attivazione non lineare prima di passare il risultato allo strato successivo, permettendo l'apprendimento di funzioni complesse.

### Summary

Una classe di rete neurale artificiale in cui le connessioni tra i nodi non formano cicli, propagando le informazioni in una sola direzione.

## Key Concepts

- Assenza di cicli
- Strati (Input, Nascosti, Output)
- Funzioni di attivazione
- Somme pesate

## Use Cases

- Compiti semplici di regressione
- Problemi di classificazione con dati tabellari
- Blocchi costitutivi per architetture più profonde

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

- [Multi-Layer Perceptron (Perceptron Multistrato)](/en/terms/multi-layer-perceptron-perceptron-multistrato/)
- [Backpropagation (Retropropagazione)](/en/terms/backpropagation-retropropagazione/)
- [Activation Function (Funzione di attivazione)](/en/terms/activation-function-funzione-di-attivazione/)
- [Neural Network (Rete neurale)](/en/terms/neural-network-rete-neurale/)
