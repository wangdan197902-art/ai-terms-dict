---
title: Fonction de prédicteur linéaire
term_id: linear_predictor_function
category: basic_concepts
subcategory: ''
tags:
- statistics
- Linear Models
- mathematics
difficulty: 2
weight: 1
slug: linear_predictor_function
date: '2026-07-18T11:25:56.352282Z'
lastmod: '2026-07-18T11:44:45.285004Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Une fonction mathématique qui calcule une combinaison linéaire de variables
  d'entrée pour prédire un résultat.
---
## Definition

Dans la modélisation statistique et l'apprentissage automatique, une fonction de prédicteur linéaire représente la somme pondérée des caractéristiques d'entrée (features) plus un terme de biais. Elle constitue le composant central des modèles linéaires généralisés (MLG).

### Summary

Une fonction mathématique qui calcule une combinaison linéaire de variables d'entrée pour prédire un résultat.

## Key Concepts

- Somme pondérée
- Terme de biais
- Modèles linéaires généralisés
- Coefficients de caractéristiques

## Use Cases

- Analyse de régression linéaire
- Classification par régression logistique
- Machines à vecteurs de support (contexte du noyau)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (coefficients de régression)](/en/terms/regression_coefficients-coefficients-de-régression/)
- [bias_intercept (terme d'interception/biais)](/en/terms/bias_intercept-terme-d-interception-biais/)
- [feature_engineering (ingénierie des caractéristiques)](/en/terms/feature_engineering-ingénierie-des-caractéristiques/)
- [generalized_linear_model (modèle linéaire généralisé)](/en/terms/generalized_linear_model-modèle-linéaire-généralisé/)
