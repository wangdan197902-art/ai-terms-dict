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
date: '2026-07-18T15:55:19.995013Z'
lastmod: '2026-07-18T17:15:08.744943Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Een klasse van kunstmatige neurale netwerken waarbij verbindingen tussen
  knooppunten geen cycli vormen en informatie in één richting wordt voortgeplant.
---
## Definition

Feed-Forward Networks (FFN's), ook wel Multi-Layer Perceptrons (MLP's) genoemd, verwerken data sequentieel door lagen van neuronen van invoer naar uitvoer zonder feedbacklussen. Elke neuron ontvangt invoeren, past een gewogen som toe en passeert deze door een activatiefunctie naar de volgende laag.

### Summary

Een klasse van kunstmatige neurale netwerken waarbij verbindingen tussen knooppunten geen cycli vormen en informatie in één richting wordt voortgeplant.

## Key Concepts

- Geen cycli
- Lagen (Invoer, Verborgen, Uitvoer)
- Activatiefuncties
- Gewogen sommen

## Use Cases

- Eenvoudige regressietaken
- Classificatieproblemen met tabeldata
- Bouwstenen voor diepere architecturen

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

- [Multi-Layer Perceptron (Meerlagige perceptron)](/en/terms/multi-layer-perceptron-meerlagige-perceptron/)
- [Backpropagation (Terugpropageren)](/en/terms/backpropagation-terugpropageren/)
- [Activation Function (Activatiefunctie)](/en/terms/activation-function-activatiefunctie/)
- [Neural Network (Neuraal netwerk)](/en/terms/neural-network-neuraal-netwerk/)
