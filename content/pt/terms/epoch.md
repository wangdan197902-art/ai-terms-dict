---
title: "Época"
term_id: "epoch"
category: "training_techniques"
subcategory: ""
tags: ["training", "neural_networks", "basics"]
difficulty: 2
weight: 1
slug: "epoch"
aliases:
  - /pt/terms/epoch/
date: "2026-07-18T14:59:14.708787Z"
lastmod: "2026-07-18T15:51:59.489016Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Uma passagem completa do conjunto de dados de treinamento através do algoritmo de aprendizado de máquina durante o treinamento do modelo."
---

## Definition

No aprendizado de máquina, uma época representa uma única iteração sobre todo o conjunto de dados de treinamento. Durante cada época, o modelo processa todos os exemplos de treinamento, atualiza seus pesos por meio da retropropagação e

### Summary

Uma passagem completa do conjunto de dados de treinamento através do algoritmo de aprendizado de máquina durante o treinamento do modelo.

## Key Concepts

- Iteração de Treinamento
- Retropropagação
- Convergência
- Ajuste de Hiperparâmetros

## Use Cases

- Configuração de loops de treinamento de redes neurais
- Monitoramento da perda de validação por ciclo
- Implementação de estratégias de parada antecipada

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Batch Size (Tamanho do Lote)](/en/terms/batch-size-tamanho-do-lote/)
- [Iteration (Iteração)](/en/terms/iteration-iteração/)
- [Learning Rate (Taxa de Aprendizado)](/en/terms/learning-rate-taxa-de-aprendizado/)
- [Overfitting (Sobreajuste)](/en/terms/overfitting-sobreajuste/)
