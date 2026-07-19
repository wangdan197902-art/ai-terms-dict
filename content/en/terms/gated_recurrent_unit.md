---
title: "Gated Recurrent Unit"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
date: "2026-07-18T09:59:06.865477Z"
lastmod: "2026-07-18T11:44:44.675568Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A type of recurrent neural network architecture that uses gating mechanisms to control the flow of information, serving as a simplified alternative to LSTM."
---
## Definition

A Gated Recurrent Unit (GRU) is a specialized recurrent neural network (RNN) cell designed to capture long-term dependencies in sequential data. It simplifies the Long Short-Term Memory (LSTM) architecture by combining the forget and input gates into a single update gate and merging the cell state and hidden state. This results in fewer parameters and faster training while maintaining competitive performance in tasks like language modeling and time-series prediction.

### Summary

A type of recurrent neural network architecture that uses gating mechanisms to control the flow of information, serving as a simplified alternative to LSTM.

## Key Concepts

- Recurrent Neural Network
- Update Gate
- Reset Gate
- Sequence Modeling

## Use Cases

- Natural language processing
- Time-series forecasting
- Speech recognition

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

- [LSTM](/en/terms/lstm/)
- [RNN](/en/terms/rnn/)
- [Deep Learning](/en/terms/deep-learning/)
- [Sequence-to-Sequence](/en/terms/sequence-to-sequence/)
