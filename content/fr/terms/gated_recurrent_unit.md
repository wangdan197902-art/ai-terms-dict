---
title: "Unité Récurrente à Portes (GRU)"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
aliases:
  - /fr/terms/gated_recurrent_unit/
date: "2026-07-18T11:18:03.076339Z"
lastmod: "2026-07-18T11:44:45.256052Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Un type d'architecture de réseau neuronal récurrent qui utilise des mécanismes de porte pour contrôler le flux d'informations, servant d'alternative simplifiée au LSTM."
---

## Definition

Une Unité Récurrente à Portes (GRU) est une cellule spécialisée de réseau neuronal récurrent (RNN) conçue pour capturer les dépendances à long terme dans les données séquentielles. Elle simplifie l'architecture du Long Short-Term Memory (LSTM) en combinant les portes de forget et d'entrée en une seule porte de mise à jour, tout en conservant une capacité efficace à gérer les séquences longues.

### Summary

Un type d'architecture de réseau neuronal récurrent qui utilise des mécanismes de porte pour contrôler le flux d'informations, servant d'alternative simplifiée au LSTM.

## Key Concepts

- Réseau Neuronal Récurrent
- Porte de Mise à Jour
- Porte de Réinitialisation
- Modélisation de Séquences

## Use Cases

- Traitement du langage naturel
- Prévision de séries chronologiques
- Reconnaissance vocale

## Code Example

```python
import torch.nn as nn

# Define a simple GRU layer
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=1)

# Example input: (seq_len, batch, input_size)
input_data = torch.randn(5, 3, 10)
hidden_state = None

output, hidden = gru(input_data, hidden_state)
```

## Related Terms

- [LSTM (Architecture similaire mais plus complexe)](/en/terms/lstm-architecture-similaire-mais-plus-complexe/)
- [RNN (Catégorie générale de réseau)](/en/terms/rnn-catégorie-générale-de-réseau/)
- [Deep Learning (Champ d'application)](/en/terms/deep-learning-champ-d-application/)
- [Sequence-to-Sequence (Architecture d'utilisation courante)](/en/terms/sequence-to-sequence-architecture-d-utilisation-courante/)
