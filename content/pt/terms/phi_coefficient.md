---
title: "Coeficiente Phi"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /pt/terms/phi_coefficient/
date: "2026-07-18T15:16:33.387066Z"
lastmod: "2026-07-18T15:51:59.522499Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Uma medida estatística de associação entre duas variáveis binárias."
---

## Definition

O coeficiente Phi (φ) é uma medida de associação para duas variáveis binárias, servindo como o coeficiente de correlação de Pearson para variáveis dicotômicas. Varia de -1 a +1, onde 0 indica ausência de associação e os extremos indicam associação perfeita.

### Summary

Uma medida estatística de associação entre duas variáveis binárias.

## Key Concepts

- Variáveis binárias
- Correlação
- Tabela de contingência
- Força da associação

## Use Cases

- Avaliação do desempenho de classificadores binários além da precisão
- Análise de relacionamentos em dados de pesquisa com respostas sim/não
- Seleção de recursos em conjuntos de dados com entradas categóricas

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [Cramer's V](/en/terms/cramer-s-v/)
- [Pearson correlation](/en/terms/pearson-correlation/)
- [Confusion matrix](/en/terms/confusion-matrix/)
- [Mutual information](/en/terms/mutual-information/)
