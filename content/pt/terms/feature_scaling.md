---
title: Escalonamento de Recursos
term_id: feature_scaling
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- statistics
- Optimization
difficulty: 2
weight: 1
slug: feature_scaling
date: '2026-07-18T15:00:10.842861Z'
lastmod: '2026-07-18T15:51:59.491111Z'
draft: false
source: agnes_llm
status: published
language: pt
description: O processo de normalização da faixa de variáveis independentes ou recursos
  dos dados para garantir uniformidade na magnitude.
---
## Definition

O escalonamento de recursos padroniza a faixa das variáveis de entrada para evitar que recursos com magnitudes maiores dominem o processo de aprendizado. Os métodos comuns incluem normalização (escalonamento min-max) e padronização (escalonamento z-score).

### Summary

O processo de normalização da faixa de variáveis independentes ou recursos dos dados para garantir uniformidade na magnitude.

## Key Concepts

- Normalização
- Padronização
- Descida do Gradiente
- Pré-processamento de Dados

## Use Cases

- Treinamento de redes neurais
- Agrupamento K-means
- Máquinas de Vetores de Suporte (SVM)

## Code Example

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
```

## Related Terms

- [Min-Max Scaling (Escala Min-Max)](/en/terms/min-max-scaling-escala-min-max/)
- [Z-score Normalization (Normalização Z-score)](/en/terms/z-score-normalization-normalização-z-score/)
- [Data preprocessing (Pré-processamento de dados)](/en/terms/data-preprocessing-pré-processamento-de-dados/)
- [Gradient Descent (Descida do gradiente)](/en/terms/gradient-descent-descida-do-gradiente/)
