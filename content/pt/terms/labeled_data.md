---
title: "Dados Rotulados"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /pt/terms/labeled_data/
date: "2026-07-18T15:07:34.362149Z"
lastmod: "2026-07-18T15:51:59.506271Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Dados nos quais o valor de saída ou alvo correto é fornecido junto com as características de entrada."
---

## Definition

Os dados rotulados consistem em amostras de entrada pareadas com seus rótulos de verdade fundamental correspondentes, servindo como base para o aprendizado de máquina supervisionado. Eles permitem que os algoritmos aprendam o mapeamento entre as entradas e as saídas desejadas.

### Summary

Dados nos quais o valor de saída ou alvo correto é fornecido junto com as características de entrada.

## Key Concepts

- Aprendizado Supervisionado
- Verdade Fundamental
- Anotação
- Variável Alvo

## Use Cases

- Treinamento de classificadores de imagem
- Construção de sistemas de reconhecimento de fala
- Modelagem preditiva em finanças

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (Dados Não Rotulados)](/en/terms/unlabeled_data-dados-não-rotulados/)
- [supervised_learning (Aprendizado Supervisionado)](/en/terms/supervised_learning-aprendizado-supervisionado/)
- [data_annotation (Anotação de Dados)](/en/terms/data_annotation-anotação-de-dados/)
- [training_set (Conjunto de Treinamento)](/en/terms/training_set-conjunto-de-treinamento/)
