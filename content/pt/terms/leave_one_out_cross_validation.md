---
title: "Validação Cruzada de Deixar Um Fora"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /pt/terms/leave_one_out_cross_validation/
date: "2026-07-18T15:08:07.232645Z"
lastmod: "2026-07-18T15:51:59.507282Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Uma técnica rigorosa de remostragem onde o modelo é treinado em todos, exceto uma amostra, e testado nessa única amostra retida, repetido para cada ponto de dados."
---

## Definition

A validação cruzada de deixar um fora (LOOCV) é um caso específico de validação cruzada k-fold onde k é igual ao número de amostras no conjunto de dados. Ela fornece uma estimativa quase não enviesada do desempenho do modelo.

### Summary

Uma técnica rigorosa de remostragem onde o modelo é treinado em todos, exceto uma amostra, e testado nessa única amostra retida, repetido para cada ponto de dados.

## Key Concepts

- Remostragem
- Avaliação de Modelo
- Compromisso Viés-Variância
- Custo Computacional

## Use Cases

- Avaliação de modelos em conjuntos de dados médicos pequenos
- Ajuste de hiperparâmetros quando os dados são escassos
- Comparação rigorosa do desempenho de algoritmos

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (Validação Cruzada k-Fold)](/en/terms/k-fold-cross-validation-validação-cruzada-k-fold/)
- [train_test_split (Divisão Treino/Teste)](/en/terms/train_test_split-divisão-treino-teste/)
- [bootstrap (Bootstrap)](/en/terms/bootstrap-bootstrap/)
- [cross_validation_score (Pontuação de Validação Cruzada)](/en/terms/cross_validation_score-pontuação-de-validação-cruzada/)
