---
title: "Adam"
term_id: "adam"
category: "basic_concepts"
subcategory: ""
tags: ["Optimization", "Deep Learning", "Algorithms"]
difficulty: 3
weight: 1
slug: "adam"
date: "2026-07-18T14:33:04.326095Z"
lastmod: "2026-07-18T15:51:59.424674Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Um algoritmo de otimização que calcula taxas de aprendizado adaptativas para cada parâmetro."
---
## Definition

Adam (Adaptive Moment Estimation) é um algoritmo de otimização baseado em gradiente de primeira ordem popular, usado no treinamento de redes neurais profundas. Ele combina as vantagens de duas outras extensões do gradiente estocástico.

### Summary

Um algoritmo de otimização que calcula taxas de aprendizado adaptativas para cada parâmetro.

## Key Concepts

- Descida de Gradiente
- Taxa de Aprendizado
- Momento
- Estimativa de Variância

## Use Cases

- Treinamento de Deep Learning
- Modelos de Visão Computacional
- Processamento de Linguagem Natural

## Code Example

```python
import torch.optim as optim
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

## Related Terms

- [SGD (Stochastic Gradient Descent)](/en/terms/sgd-stochastic-gradient-descent/)
- [RMSProp](/en/terms/rmsprop/)
- [Otimizador (Optimizer)](/en/terms/otimizador-optimizer/)
- [Backpropagation (Retropropagação)](/en/terms/backpropagation-retropropagação/)
