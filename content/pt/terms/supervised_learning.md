---
title: Aprendizado Supervisionado
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T14:47:01.752738Z'
lastmod: '2026-07-18T15:51:59.455600Z'
draft: false
source: agnes_llm
status: published
language: pt
description: Um paradigma de aprendizado de máquina no qual um modelo aprende a mapear
  entradas para saídas com base em exemplos de treinamento rotulados.
---
## Definition

No aprendizado supervisionado, o algoritmo é treinado em um conjunto de dados rotulado, o que significa que cada exemplo de entrada é pareado com a saída correta. O objetivo é que o modelo aprenda a relação subjacente entre as variáveis de entrada e as saídas desejadas.

### Summary

Um paradigma de aprendizado de máquina no qual um modelo aprende a mapear entradas para saídas com base em exemplos de treinamento rotulados.

## Key Concepts

- Dados Rotulados
- Mapeamento Entrada-Saída
- Classificação
- Regressão

## Use Cases

- Detecção de spam em e-mails
- Previsão de preços de imóveis
- Reconhecimento de imagens

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Aprendizado Não Supervisionado](/en/terms/aprendizado-não-supervisionado/)
- [Conjunto de Treinamento](/en/terms/conjunto-de-treinamento/)
- [Conjunto de Validação](/en/terms/conjunto-de-validação/)
- [Precisão do Modelo](/en/terms/precisão-do-modelo/)
