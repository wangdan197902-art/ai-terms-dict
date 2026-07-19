---
title: Validation croisée leave-one-out
term_id: leave_one_out_cross_validation
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- evaluation
- statistics
difficulty: 3
weight: 1
slug: leave_one_out_cross_validation
date: '2026-07-18T11:25:42.850205Z'
lastmod: '2026-07-18T11:44:45.284214Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Une technique rigoureuse de rééchantillonnage où le modèle est entraîné
  sur tous les échantillons sauf un et testé sur cet unique échantillon conservé,
  répété pour chaque point de données.
---
## Definition

La validation croisée leave-one-out (LOOCV) est un cas particulier de la validation croisée k-fold où k est égal au nombre d'échantillons dans l'ensemble de données. Elle fournit une estimation quasi non biaisée de la performance du modèle en utilisant chaque point de données comme ensemble de test à tour de rôle.

### Summary

Une technique rigoureuse de rééchantillonnage où le modèle est entraîné sur tous les échantillons sauf un et testé sur cet unique échantillon conservé, répété pour chaque point de données.

## Key Concepts

- Rééchantillonnage
- Évaluation de modèle
- Compromis biais-variance
- Coût computationnel

## Use Cases

- Évaluation de modèles sur de petits ensembles de données médicales
- Réglage des hyperparamètres lorsque les données sont rares
- Comparaison rigoureuse des performances des algorithmes

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

- [k-fold cross-validation (validation croisée k-fold)](/en/terms/k-fold-cross-validation-validation-croisée-k-fold/)
- [train_test_split (séparation entraînement/test)](/en/terms/train_test_split-séparation-entraînement-test/)
- [bootstrap (méthode bootstrap)](/en/terms/bootstrap-méthode-bootstrap/)
- [cross_validation_score (score de validation croisée)](/en/terms/cross_validation_score-score-de-validation-croisée/)
