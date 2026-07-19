---
title: Modelo substituto
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T15:24:00.003250Z'
lastmod: '2026-07-18T15:51:59.536688Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Um modelo matemático simplificado usado para aproximar o comportamento
  de um modelo mais complexo, computacionalmente caro ou inacessível (black-box).
---
## Definition

No aprendizado de máquina e na otimização, um modelo substituto atua como um proxy para uma função alvo que é difícil de avaliar diretamente. Ele é treinado em pares de entrada-saída do modelo original para aproximar sua saída com menor custo computacional.

### Summary

Um modelo matemático simplificado usado para aproximar o comportamento de um modelo mais complexo, computacionalmente caro ou inacessível (black-box).

## Key Concepts

- Aproximação de Modelo
- Otimização de Caixa-Preta
- Eficiência Computacional
- Modelo Proxy

## Use Cases

- Otimização de hiperparâmetros
- Aceleração de simulações de projeto de engenharia
- Análise de sensibilidade de sistemas complexos

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Bayesian Optimization (Otimização Bayesiana)](/en/terms/bayesian-optimization-otimização-bayesiana/)
- [Gaussian Process (Processo Gaussiano)](/en/terms/gaussian-process-processo-gaussiano/)
- [Black-Box Function (Função de Caixa-Preta)](/en/terms/black-box-function-função-de-caixa-preta/)
- [Emulator (Emulador)](/en/terms/emulator-emulador/)
