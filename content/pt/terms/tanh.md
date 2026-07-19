---
title: Tanh
term_id: tanh
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- mathematics
difficulty: 2
weight: 1
slug: tanh
date: '2026-07-18T15:24:14.267999Z'
lastmod: '2026-07-18T15:51:59.537346Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Tanh, ou tangente hiperbólica, é uma função de ativação que mapeia valores
  de entrada para um intervalo entre -1 e 1.
---
## Definition

A função tangente hiperbólica (Tanh) é uma função de ativação não linear comumente usada em redes neurais. Ela comprime os valores de entrada no intervalo (-1, 1), fornecendo saídas centradas em zero, o que...

### Summary

Tanh, ou tangente hiperbólica, é uma função de ativação que mapeia valores de entrada para um intervalo entre -1 e 1.

## Key Concepts

- Função de ativação
- Não linearidade
- Saída centrada em zero
- Backpropagation (retropropagação)

## Use Cases

- Redes neurais recorrentes
- Portas de células LSTM
- Camadas ocultas em MLPs

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (sigmoide)](/en/terms/sigmoid-sigmoide/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (redes neurais)](/en/terms/neural_networks-redes-neurais/)
