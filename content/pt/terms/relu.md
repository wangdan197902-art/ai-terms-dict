---
title: ReLU
term_id: relu
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Activation Functions
- Deep Learning
difficulty: 3
weight: 1
slug: relu
date: '2026-07-18T14:45:42.847411Z'
lastmod: '2026-07-18T15:51:59.454104Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Unidade Linear Retificada é uma função de ativação que retorna a entrada
  diretamente se for positiva, caso contrário, retorna zero.
---
## Definition

A ReLU é amplamente utilizada em redes neurais de aprendizado profundo devido à sua eficiência computacional e capacidade de mitigar o problema do gradiente desaparecente. Definida matematicamente como f(x) = max(0, x), ela introduz não linearidade na rede, permitindo que o modelo aprenda padrões complexos.

### Summary

Unidade Linear Retificada é uma função de ativação que retorna a entrada diretamente se for positiva, caso contrário, retorna zero.

## Key Concepts

- Não-linearidade
- Função de Ativação
- Gradiente Desaparecente
- Linear por Partes

## Use Cases

- Camadas ocultas em Redes Neurais Convolucionais (CNNs)
- Redes Feedforward Profundas
- Modelos de Reconhecimento de Imagens

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (Função de ativação sigmoide)](/en/terms/sigmoid-função-de-ativação-sigmoide/)
- [Tanh (Função tangente hiperbólica)](/en/terms/tanh-função-tangente-hiperbólica/)
- [Leaky ReLU (Variante da ReLU que permite pequenos gradientes para valores negativos)](/en/terms/leaky-relu-variante-da-relu-que-permite-pequenos-gradientes-para-valores-negativos/)
- [Rede Neural (Modelo computacional inspirado no cérebro)](/en/terms/rede-neural-modelo-computacional-inspirado-no-cérebro/)
