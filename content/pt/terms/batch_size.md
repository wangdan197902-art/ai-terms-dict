---
title: Tamanho do Lote
term_id: batch_size
category: training_techniques
subcategory: ''
tags:
- hyperparameters
- Optimization
- memory
difficulty: 2
weight: 1
slug: batch_size
date: '2026-07-18T14:51:20.538279Z'
lastmod: '2026-07-18T15:51:59.467494Z'
draft: false
source: agnes_llm
status: published
language: pt
description: O número de exemplos de treinamento utilizados em uma única iteração
  do algoritmo de descida do gradiente estocástico.
---
## Definition

O tamanho do lote é um hiperparâmetro crítico que determina quantas amostras são processadas antes que os parâmetros internos do modelo sejam atualizados. Um tamanho de lote maior fornece uma estimativa mais precisa do gradiente global, mas consome mais memória; já um tamanho menor introduz mais ruído, o que pode ajudar na generalização.

### Summary

O número de exemplos de treinamento utilizados em uma única iteração do algoritmo de descida do gradiente estocástico.

## Key Concepts

- Estimativa de gradiente
- Restrições de memória
- Estabilidade da convergência
- Ajuste de hiperparâmetros

## Use Cases

- Ajuste da velocidade de convergência do modelo
- Gerenciamento dos limites de memória da GPU durante o treinamento
- Melhoria da generalização através de gradientes ruidosos

## Related Terms

- [learning_rate (taxa de aprendizado)](/en/terms/learning_rate-taxa-de-aprendizado/)
- [stochastic_gradient_descent (descida do gradiente estocástica)](/en/terms/stochastic_gradient_descent-descida-do-gradiente-estocástica/)
- [mini_batch (mini-lote)](/en/terms/mini_batch-mini-lote/)
- [memory_usage (uso de memória)](/en/terms/memory_usage-uso-de-memória/)
