---
title: "Gated Recurrent Unit"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
date: "2026-07-18T11:15:36.270955Z"
lastmod: "2026-07-18T11:44:44.943072Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine Art rekurrentes neuronales Netzwerk (RNN), das Gating-Mechanismen verwendet, um den Informationsfluss zu steuern, und als vereinfachte Alternative zu LSTM dient."
---
## Definition

Eine Gated Recurrent Unit (GRU) ist eine spezialisierte Zelle eines rekurrenten neuronalen Netzwerks (RNN), die entwickelt wurde, um langfristige Abhängigkeiten in sequenziellen Daten zu erfassen. Sie vereinfacht die Architektur der Long Short-Term Memory (LSTM)-Netze, indem sie zwei Gates (Update- und Reset-Gate) verwendet, um den Informationsfluss zu regulieren.

### Summary

Eine Art rekurrentes neuronales Netzwerk (RNN), das Gating-Mechanismen verwendet, um den Informationsfluss zu steuern, und als vereinfachte Alternative zu LSTM dient.

## Key Concepts

- Recurrent Neural Network
- Update Gate
- Reset Gate
- Sequence Modeling

## Use Cases

- Natürliche Sprachverarbeitung
- Zeitreihenvorhersage
- Spracherkennung

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

- [LSTM (Long Short-Term Memory)](/en/terms/lstm-long-short-term-memory/)
- [RNN (Recurrent Neural Network)](/en/terms/rnn-recurrent-neural-network/)
- [Deep Learning (Tiefes Lernen)](/en/terms/deep-learning-tiefes-lernen/)
- [Sequence-to-Sequence (Sequenz-zu-Sequenz)](/en/terms/sequence-to-sequence-sequenz-zu-sequenz/)
