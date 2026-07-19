---
title: Codificación Posicional
term_id: positional_encoding
category: basic_concepts
subcategory: ''
tags:
- transformers
- NLP
- architecture
difficulty: 3
weight: 1
slug: positional_encoding
date: '2026-07-18T10:31:40.904861Z'
lastmod: '2026-07-18T11:44:44.765216Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una técnica que inyecta información sobre la posición relativa o absoluta
  de los tokens en una secuencia dentro de los modelos transformadores.
---
## Definition

Dado que los transformadores procesan todos los tokens en paralelo en lugar de secuencialmente como las RNN, carecen de conocimiento inherente sobre el orden de los tokens. La codificación posicional añade vectores específicos a las incrustaciones de entrada para preservar esta información de orden.

### Summary

Una técnica que inyecta información sobre la posición relativa o absoluta de los tokens en una secuencia dentro de los modelos transformadores.

## Key Concepts

- Orden de la Secuencia
- Autoatención
- Funciones Senoidales
- Incrustaciones de Tokens

## Use Cases

- Traducción Automática
- Resumen de Textos
- Modelado del Lenguaje

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Arquitectura Transformer (Arquitectura de red neuronal basada en atención)](/en/terms/arquitectura-transformer-arquitectura-de-red-neuronal-basada-en-atención/)
- [Incrustación (Representación vectorial de datos discretos)](/en/terms/incrustación-representación-vectorial-de-datos-discretos/)
- [Mecanismo de Atención (Proceso de ponderar la importancia de diferentes partes de la entrada)](/en/terms/mecanismo-de-atención-proceso-de-ponderar-la-importancia-de-diferentes-partes-de-la-entrada/)
- [RoPE (Codificación de posición rotatoria)](/en/terms/rope-codificación-de-posición-rotatoria/)
