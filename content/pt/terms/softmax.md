---
title: Softmax
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T14:45:55.098347Z'
lastmod: '2026-07-18T15:51:59.455211Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Uma função matemática que converte um vetor de pontuações reais arbitrárias
  em uma distribuição de probabilidade.
---
## Definition

O Softmax é amplamente utilizado na camada de saída de redes neurais para tarefas de classificação multiclasse. Ele recebe um vetor de logins brutos e os normaliza para que cada elemento represente uma probabilidade de

### Summary

Uma função matemática que converte um vetor de pontuações reais arbitrárias em uma distribuição de probabilidade.

## Key Concepts

- Distribuição de Probabilidade
- Logits
- Normalização
- Classificação Multiclasse

## Use Cases

- Camadas de saída de classificação de imagens
- Predição de tokens em modelos de linguagem
- Categorização multirótulo

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (Argmax)](/en/terms/argmax-argmax/)
- [Cross-Entropy Loss (Perda de Entropia Cruzada)](/en/terms/cross-entropy-loss-perda-de-entropia-cruzada/)
- [Logits (Logits)](/en/terms/logits-logits/)
- [Neural Network (Rede Neural)](/en/terms/neural-network-rede-neural/)
