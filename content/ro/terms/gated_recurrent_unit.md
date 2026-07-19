---
title: "Unitate Recurentă cu Porți (GRU)"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
date: "2026-07-18T15:59:28.000301Z"
lastmod: "2026-07-18T17:15:09.658860Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Un tip de arhitectură de rețea neuronală recurentă care utilizează mecanisme de porți pentru a controla fluxul de informații, servind ca o alternativă simplificată la LSTM."
---
## Definition

O Unitate Recurentă cu Porți (GRU) este o celulă specializată de rețea neuronală recurentă (RNN), concepută pentru a captura dependențe pe termen lung în datele secvențiale. Simplifică arhitectura Memoriei Pe Termen Lung (LSTM)

### Summary

Un tip de arhitectură de rețea neuronală recurentă care utilizează mecanisme de porți pentru a controla fluxul de informații, servind ca o alternativă simplificată la LSTM.

## Key Concepts

- Rețea Neuronală Recurentă
- Poarta de Actualizare
- Poarta de Resetare
- Modelarea Secvențială

## Use Cases

- Procesarea limbajului natural
- Prognozarea seriilor temporale
- Recunoașterea vorbirii

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

- [LSTM (Memorie Pe Termen Lung)](/en/terms/lstm-memorie-pe-termen-lung/)
- [RNN (Rețea Neuronală Recurentă)](/en/terms/rnn-rețea-neuronală-recurentă/)
- [Deep Learning (Învățare Profundă)](/en/terms/deep-learning-învățare-profundă/)
- [Secvență-la-Secvență](/en/terms/secvență-la-secvență/)
