---
title: "Unità Ricorrente con Gate (GRU)"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
date: "2026-07-18T16:01:05.354938Z"
lastmod: "2026-07-18T17:15:08.628441Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Un tipo di architettura di rete neurale ricorrente che utilizza meccanismi di gate per controllare il flusso di informazioni, fungendo da alternativa semplificata all'LSTM."
---
## Definition

Un'Unità Ricorrente con Gate (GRU) è una cella specializzata di rete neurale ricorrente (RNN) progettata per catturare dipendenze a lungo termine nei dati sequenziali. Semplifica l'architettura della Memoria a Breve e Lungo Termine (LSTM) riducendo il numero di parametri e la complessità computazionale, mantenendo comunque un'elevata capacità di modellazione delle sequenze. Utilizza due gate principali: il gate di aggiornamento e il gate di reset.

### Summary

Un tipo di architettura di rete neurale ricorrente che utilizza meccanismi di gate per controllare il flusso di informazioni, fungendo da alternativa semplificata all'LSTM.

## Key Concepts

- Rete Neurale Ricorrente
- Gate di Aggiornamento
- Gate di Reset
- Modellazione di Sequenze

## Use Cases

- Elaborazione del linguaggio naturale
- Previsione di serie temporali
- Riconoscimento vocale

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

- [LSTM (Memoria a Breve e Lungo Termine)](/en/terms/lstm-memoria-a-breve-e-lungo-termine/)
- [RNN (Rete Neurale Ricorrente)](/en/terms/rnn-rete-neurale-ricorrente/)
- [Deep Learning (Apprendimento profondo)](/en/terms/deep-learning-apprendimento-profondo/)
- [Sequence-to-Sequence (Architettura per traduzione e generazione)](/en/terms/sequence-to-sequence-architettura-per-traduzione-e-generazione/)
