---
title: Avaliação de classificadores binários
term_id: evaluation_of_binary_classifiers
category: basic_concepts
subcategory: ''
tags:
- metrics
- Classification
- evaluation
difficulty: 2
weight: 1
slug: evaluation_of_binary_classifiers
date: '2026-07-18T14:59:14.708809Z'
lastmod: '2026-07-18T15:51:59.489240Z'
draft: false
source: agnes_llm
status: published
language: pt
description: O processo de avaliar o desempenho de modelos de aprendizado de máquina
  que preveem um de dois resultados possíveis.
---
## Definition

Esta área envolve a análise de métricas como precisão, exatidão, revocação, pontuação F1 e a Área Sob a Curva ROC (AUC-ROC). Ajuda a determinar quão bem um modelo distingue

### Summary

O processo de avaliar o desempenho de modelos de aprendizado de máquina que preveem um de dois resultados possíveis.

## Key Concepts

- Matriz de Confusão
- Compromisso Precisão-Revocação
- Curva ROC
- Pontuação F1

## Use Cases

- Rastreamento de doenças médicas
- Filtragem de spam por e-mail
- Avaliação de risco de crédito

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (matriz_de_confusão)](/en/terms/confusion_matrix-matriz_de_confusão/)
- [roc_auc (roc_auc)](/en/terms/roc_auc-roc_auc/)
- [precision_recall (precisao_revocacao)](/en/terms/precision_recall-precisao_revocacao/)
- [cross_validation (validacao_cruzada)](/en/terms/cross_validation-validacao_cruzada/)
