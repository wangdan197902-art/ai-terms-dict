---
title: Truque de Reparametrização
term_id: reparameterization_trick
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- Probabilistic Models
- Optimization
difficulty: 4
weight: 1
slug: reparameterization_trick
date: '2026-07-18T15:19:39.994223Z'
lastmod: '2026-07-18T15:51:59.528836Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Uma técnica que separa variáveis estocásticas de parâmetros aprendíveis
  para permitir a otimização baseada em gradientes na inferência variacional.
---
## Definition

O truque de reparametrização é um método fundamental utilizado em autoencoders variacionais e outros modelos probabilísticos. Ele permite que os gradientes fluam através de nós estocásticos expressando uma variável aleatória como uma função determinística de seus parâmetros e de uma variável de ruído independente, facilitando assim o cálculo do gradiente via retropropagação.

### Summary

Uma técnica que separa variáveis estocásticas de parâmetros aprendíveis para permitir a otimização baseada em gradientes na inferência variacional.

## Key Concepts

- Inferência Variacional
- Estimativa de Gradiente
- Nós Estocásticos
- Simulação Diferenciável

## Use Cases

- Treinamento de Autoencoders Variacionais (VAEs)
- Redes Neurais Bayesianas
- Modelos Gráficos Probabilísticos

## Code Example

```python
import torch
epsilon = torch.randn(100, 10)
mu = torch.zeros(100, 10)
sigma = torch.ones(100, 10)
z = mu + sigma * epsilon  # Reparameterized sampling
```

## Related Terms

- [ELBO](/en/terms/elbo/)
- [Variáveis Latentes](/en/terms/variáveis-latentes/)
- [Retropropagação](/en/terms/retropropagação/)
- [Estimativa de Monte Carlo](/en/terms/estimativa-de-monte-carlo/)
