---
title: Matriz de Confusão
term_id: confusion_matrix
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Classification
- metrics
difficulty: 2
weight: 1
slug: confusion_matrix
date: '2026-07-18T14:54:05.533321Z'
lastmod: '2026-07-18T15:51:59.473778Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Uma tabela usada para descrever o desempenho de um modelo de classificação
  em um conjunto de dados de teste.
---
## Definition

Uma matriz de confusão é um layout de tabela específico que permite visualizar o desempenho de um algoritmo, tipicamente de aprendizado supervisionado. Ela mostra as contagens de verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos, fornecendo uma visão detalhada dos erros cometidos pelo modelo em cada classe.

### Summary

Uma tabela usada para descrever o desempenho de um modelo de classificação em um conjunto de dados de teste.

## Key Concepts

- Verdadeiros Positivos
- Falsos Negativos
- Precisão
- Revocação (Recall)

## Use Cases

- Avaliação de classificadores binários
- Análise do desempenho de classificação multiclasse
- Depuração de viés do modelo em conjuntos de dados desbalanceados

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (precisão)](/en/terms/precision-precisão/)
- [recall (revocação/recall)](/en/terms/recall-revocação-recall/)
- [F1 score (escore F1)](/en/terms/f1-score-escore-f1/)
- [ROC curve (curva ROC)](/en/terms/roc-curve-curva-roc/)
