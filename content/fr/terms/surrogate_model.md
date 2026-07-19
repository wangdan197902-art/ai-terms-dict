---
title: Modèle substitut
term_id: surrogate_model
category: basic_concepts
subcategory: ''
tags:
- Optimization
- approximation
- ML Technique
difficulty: 3
weight: 1
slug: surrogate_model
date: '2026-07-18T11:40:12.277017Z'
lastmod: '2026-07-18T11:44:45.340251Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Un modèle mathématique simplifié utilisé pour approximer le comportement
  d'un modèle plus complexe, coûteux en calcul ou inaccessible (boîte noire).
---
## Definition

En apprentissage automatique et en optimisation, un modèle substitut sert de proxy pour une fonction cible difficile à évaluer directement. Il est entraîné sur des paires entrée-sortie issues du modèle original pour approximer sa sortie.

### Summary

Un modèle mathématique simplifié utilisé pour approximer le comportement d'un modèle plus complexe, coûteux en calcul ou inaccessible (boîte noire).

## Key Concepts

- Approximation de modèle
- Optimisation de boîte noire
- Efficacité computationnelle
- Modèle proxy

## Use Cases

- Optimisation des hyperparamètres
- Accélération des simulations de conception technique
- Analyse de sensibilité des systèmes complexes

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Optimisation bayésienne (méthode d'optimisation séquentielle)](/en/terms/optimisation-bayésienne-méthode-d-optimisation-séquentielle/)
- [Processus gaussien (modèle probabiliste utilisé comme substitut)](/en/terms/processus-gaussien-modèle-probabiliste-utilisé-comme-substitut/)
- [Fonction de boîte noire (fonction dont l'interne est inconnu)](/en/terms/fonction-de-boîte-noire-fonction-dont-l-interne-est-inconnu/)
- [Émulateur (modèle imitant le comportement d'un système)](/en/terms/émulateur-modèle-imitant-le-comportement-d-un-système/)
