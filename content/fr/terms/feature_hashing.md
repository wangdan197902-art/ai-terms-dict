---
title: Hachage de fonctionnalités
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
date: '2026-07-18T11:17:05.500020Z'
lastmod: '2026-07-18T11:44:45.250622Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Une technique qui mape des fonctionnalités creuses de haute dimension
  vers un vecteur de taille fixe à l'aide d'une fonction de hachage.
---
## Definition

Le hachage de fonctionnalités, également connu sous le nom d'astuce de hachage (hashing trick), permet aux modèles d'apprentissage automatique de gérer de grands espaces de fonctionnalités creux sans maintenir de mappage explicite entre les fonctionnalités et leurs indices. En appliquant une fonction de hachage, on réduit la dimensionalité tout en préservant les relations statistiques, ce qui optimise l'utilisation de la mémoire.

### Summary

Une technique qui mape des fonctionnalités creuses de haute dimension vers un vecteur de taille fixe à l'aide d'une fonction de hachage.

## Key Concepts

- Fonction de hachage
- Vecteurs creux
- Réduction de dimensionalité
- Efficacité mémoire

## Use Cases

- Classification de texte avec de grands vocabulaires
- Systèmes de recommandation avec d'immenses ensembles d'articles
- Traitement de données en streaming en temps réel

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

- [One-hot encoding (Encodage en une seule valeur active)](/en/terms/one-hot-encoding-encodage-en-une-seule-valeur-active/)
- [Bag of Words (Sac de mots)](/en/terms/bag-of-words-sac-de-mots/)
- [Dimensionality reduction (Réduction de dimensionalité)](/en/terms/dimensionality-reduction-réduction-de-dimensionalité/)
- [Sparse matrix (Matrice creuse)](/en/terms/sparse-matrix-matrice-creuse/)
