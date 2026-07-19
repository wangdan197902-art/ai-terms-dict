---
title: Codificação Posicional
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
date: '2026-07-18T14:45:14.667430Z'
lastmod: '2026-07-18T15:51:59.453166Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Uma técnica que injeta informações sobre a posição relativa ou absoluta
  dos tokens em uma sequência em modelos Transformer.
---
## Definition

Como os Transformers processam todos os tokens em paralelo, em vez de sequencialmente como as RNNs, eles não possuem conhecimento inerente da ordem dos tokens. A codificação posicional adiciona vetores específicos às embeddings de entrada para pres

### Summary

Uma técnica que injeta informações sobre a posição relativa ou absoluta dos tokens em uma sequência em modelos Transformer.

## Key Concepts

- Ordem da Sequência
- Autoatenção
- Funções Senoidais
- Embeddings de Tokens

## Use Cases

- Tradução Automática
- Resumo de Texto
- Modelagem de Linguagem

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

- [Transformer Architecture (Arquitetura Transformer)](/en/terms/transformer-architecture-arquitetura-transformer/)
- [Embedding (Embedding)](/en/terms/embedding-embedding/)
- [Attention Mechanism (Mecanismo de Atenção)](/en/terms/attention-mechanism-mecanismo-de-atenção/)
- [RoPE (Posição Relativa de Posições Rotacionadas)](/en/terms/rope-posição-relativa-de-posições-rotacionadas/)
