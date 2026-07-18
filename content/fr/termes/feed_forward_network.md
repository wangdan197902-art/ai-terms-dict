---
title: "Réseau à propagation avant"
term_id: "feed_forward_network"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "architecture", "fundamentals"]
difficulty: 2
weight: 1
slug: "feed_forward_network"
aliases:
  - /fr/terms/feed_forward_network/
date: "2026-07-18T11:17:05.500094Z"
lastmod: "2026-07-18T11:44:45.251256Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Une classe de réseau de neurones artificiels où les connexions entre les nœuds ne forment pas de cycles, propageant l'information dans une seule direction."
---

## Definition

Les réseaux à propagation avant (FFN), également connus sous le nom de perceptrons multicouches (MLP), traitent les données séquentiellement à travers des couches de neurones, de l'entrée vers la sortie, sans boucles de rétroaction. Chaque neurone reçoit des entrées pondérées, applique une fonction d'activation et transmet le résultat à la couche suivante.

### Summary

Une classe de réseau de neurones artificiels où les connexions entre les nœuds ne forment pas de cycles, propageant l'information dans une seule direction.

## Key Concepts

- Absence de cycles
- Couches (Entrée, Cachée, Sortie)
- Fonctions d'activation
- Sommes pondérées

## Use Cases

- Tâches de régression simples
- Problèmes de classification avec des données tabulaires
- Blocs de construction pour des architectures plus profondes

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

- [Multi-Layer Perceptron (Perceptron multicouche)](/en/terms/multi-layer-perceptron-perceptron-multicouche/)
- [Backpropagation (Rétropropagation)](/en/terms/backpropagation-rétropropagation/)
- [Activation Function (Fonction d'activation)](/en/terms/activation-function-fonction-d-activation/)
- [Neural Network (Réseau de neurones)](/en/terms/neural-network-réseau-de-neurones/)
