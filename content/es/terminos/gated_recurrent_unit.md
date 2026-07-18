---
title: "Unidad Recurrente con Puertas"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
aliases:
  - /es/terms/gated_recurrent_unit/
date: "2026-07-18T10:50:13.497630Z"
lastmod: "2026-07-18T11:44:44.809727Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Un tipo de arquitectura de red neuronal recurrente que utiliza mecanismos de puertas para controlar el flujo de información, sirviendo como una alternativa simplificada a la LSTM."
---

## Definition

Una Unidad Recurrente con Puertas (GRU, por sus siglas en inglés) es una celda especializada de red neuronal recurrente diseñada para capturar dependencias a largo plazo en datos secuenciales. Simplifica la arquitectura de la Memoria a Corto Plazo Largo (LSTM) al combinar las puertas de olvido y entrada en una única puerta de actualización, lo que reduce la complejidad computacional manteniendo un rendimiento competitivo.

### Summary

Un tipo de arquitectura de red neuronal recurrente que utiliza mecanismos de puertas para controlar el flujo de información, sirviendo como una alternativa simplificada a la LSTM.

## Key Concepts

- Red Neuronal Recurrente
- Puerta de Actualización
- Puerta de Reinicio
- Modelado de Secuencias

## Use Cases

- Procesamiento del lenguaje natural
- Pronóstico de series temporales
- Reconocimiento de voz

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

- [LSTM (Memoria a Corto Plazo Largo)](/en/terms/lstm-memoria-a-corto-plazo-largo/)
- [RNN (Red Neuronal Recurrente)](/en/terms/rnn-red-neuronal-recurrente/)
- [Aprendizaje Profundo (Campo general)](/en/terms/aprendizaje-profundo-campo-general/)
- [Secuencia a Secuencia (Arquitectura de aplicación)](/en/terms/secuencia-a-secuencia-arquitectura-de-aplicación/)
