---
title: "Unidade Recorrente com Portas (GRU)"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
aliases:
  - /pt/terms/gated_recurrent_unit/
date: "2026-07-18T15:01:22.127480Z"
lastmod: "2026-07-18T15:51:59.493456Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Um tipo de arquitetura de rede neural recorrente que usa mecanismos de portas para controlar o fluxo de informações, servindo como uma alternativa simplificada ao LSTM."
---

## Definition

Uma Unidade Recorrente com Portas (GRU) é uma célula especializada de rede neural recorrente (RNN) projetada para capturar dependências de longo prazo em dados sequenciais. Ela simplifica a arquitetura da Memória de Curto e Longo Prazo (LSTM) ao combinar os gates de esquecimento e entrada em um único gate de atualização, reduzindo a complexidade computacional enquanto mantém a eficácia.

### Summary

Um tipo de arquitetura de rede neural recorrente que usa mecanismos de portas para controlar o fluxo de informações, servindo como uma alternativa simplificada ao LSTM.

## Key Concepts

- Rede Neural Recorrente
- Gate de Atualização
- Gate de Reset
- Modelagem de Sequências

## Use Cases

- Processamento de Linguagem Natural (PLN)
- Previsão de séries temporais
- Reconhecimento de fala

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

- [LSTM (Memória de Curto e Longo Prazo)](/en/terms/lstm-memória-de-curto-e-longo-prazo/)
- [RNN (Rede Neural Recorrente)](/en/terms/rnn-rede-neural-recorrente/)
- [Deep Learning (Aprendizado Profundo)](/en/terms/deep-learning-aprendizado-profundo/)
- [Sequência para Sequência (Sequence-to-Sequence)](/en/terms/sequência-para-sequência-sequence-to-sequence/)
