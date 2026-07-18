---
title: "Feature Hashing"
term_id: "feature_hashing"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "text-mining", "optimization"]
difficulty: 3
weight: 1
slug: "feature_hashing"
aliases:
  - /pt/terms/feature_hashing/
date: "2026-07-18T14:59:57.207467Z"
lastmod: "2026-07-18T15:51:59.490901Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Uma técnica que mapeia features esparsos de alta dimensão para um vetor de tamanho fixo usando uma função de hash."
---

## Definition

O feature hashing, também conhecido como truque de hash, permite que modelos de aprendizado de máquina lidem com espaços de features grandes e esparsos sem manter um mapeamento explícito entre features e índices. Ao aplicar uma função de hash, os dados são comprimidos eficientemente, economizando memória e permitindo o processamento em tempo real.

### Summary

Uma técnica que mapeia features esparsos de alta dimensão para um vetor de tamanho fixo usando uma função de hash.

## Key Concepts

- Função de Hash
- Vetores Esparsos
- Redução de Dimensionalidade
- Eficiência de Memória

## Use Cases

- Classificação de texto com grandes vocabulários
- Sistemas de recomendação com conjuntos massivos de itens
- Processamento de dados em streaming em tempo real

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-hot encoding (Codificação One-Hot)](/en/terms/one-hot-encoding-codificação-one-hot/)
- [Bag of Words (Bolsa de Palavras)](/en/terms/bag-of-words-bolsa-de-palavras/)
- [Dimensionality reduction (Redução de dimensionalidade)](/en/terms/dimensionality-reduction-redução-de-dimensionalidade/)
- [Sparse matrix (Matriz esparsa)](/en/terms/sparse-matrix-matriz-esparsa/)
