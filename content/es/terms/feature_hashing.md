---
title: Hashing de características
term_id: feature_hashing
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- Text Mining
- Optimization
difficulty: 3
weight: 1
slug: feature_hashing
date: '2026-07-18T10:49:18.358246Z'
lastmod: '2026-07-18T11:44:44.805785Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una técnica que mapea características dispersas de alta dimensión a un
  vector de tamaño fijo utilizando una función hash.
---
## Definition

El hashing de características, también conocido como el truco del hashing, permite que los modelos de aprendizaje automático manejen espacios de características grandes y dispersos sin mantener un mapeo explícito entre las características y sus índices. Al aplicar

### Summary

Una técnica que mapea características dispersas de alta dimensión a un vector de tamaño fijo utilizando una función hash.

## Key Concepts

- Función hash
- Vectores dispersos
- Reducción de dimensionalidad
- Eficiencia de memoria

## Use Cases

- Clasificación de texto con vocabularios grandes
- Sistemas de recomendación con conjuntos de elementos enormes
- Procesamiento de datos en transmisión en tiempo real

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

- [One-hot encoding (Codificación uno entre varios)](/en/terms/one-hot-encoding-codificación-uno-entre-varios/)
- [Bag of Words (Bolsa de palabras)](/en/terms/bag-of-words-bolsa-de-palabras/)
- [Dimensionality reduction (Reducción de dimensionalidad)](/en/terms/dimensionality-reduction-reducción-de-dimensionalidad/)
- [Sparse matrix (Matriz dispersa)](/en/terms/sparse-matrix-matriz-dispersa/)
