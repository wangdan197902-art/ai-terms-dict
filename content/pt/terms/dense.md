---
title: "Dense"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /pt/terms/dense/
date: "2026-07-18T14:57:03.718528Z"
lastmod: "2026-07-18T15:51:59.482864Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Uma camada ou tensor onde cada elemento está conectado a todos os elementos da camada ou dimensão anterior."
---

## Definition

Em redes neurais, 'dense' refere-se a camadas totalmente conectadas, onde cada neurônio recebe entrada de todos os neurônios da camada precedente. Isso contrasta com as conexões esparsas encontradas em convolucionais ou...

### Summary

Uma camada ou tensor onde cada elemento está conectado a todos os elementos da camada ou dimensão anterior.

## Key Concepts

- Fully Connected
- Matriz de Pesos
- Função de Ativação
- Integração de Recursos

## Use Cases

- Camadas finais de classificação em MLPs
- Fusão de recursos em modelos híbridos
- Tarefas simples de regressão

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Rede Neural Feedforward)](/en/terms/feedforward-neural-network-rede-neural-feedforward/)
- [Backpropagation (Propagação Reversa)](/en/terms/backpropagation-propagação-reversa/)
- [ReLU (Função de Ativação Retificada Linear)](/en/terms/relu-função-de-ativação-retificada-linear/)
- [Bias Term (Termo de Viés)](/en/terms/bias-term-termo-de-viés/)
