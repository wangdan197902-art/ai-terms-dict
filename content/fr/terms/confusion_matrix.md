---
title: "Matrice de confusion"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /fr/terms/confusion_matrix/
date: "2026-07-18T11:10:13.419117Z"
lastmod: "2026-07-18T11:44:45.210666Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Un tableau utilisé pour décrire les performances d'un modèle de classification sur un ensemble de données de test."
---

## Definition

Une matrice de confusion est une disposition tabulaire spécifique qui permet de visualiser les performances d'un algorithme, généralement supervisé. Elle affiche les effectifs des vrais positifs, des vrais négatifs, des faux positifs et des faux négatifs.

### Summary

Un tableau utilisé pour décrire les performances d'un modèle de classification sur un ensemble de données de test.

## Key Concepts

- Vrais positifs
- Faux négatifs
- Précision
- Rappel

## Use Cases

- Évaluation des classificateurs binaires
- Analyse des performances de classification multi-classe
- Débogage du biais du modèle sur des jeux de données déséquilibrés

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (précision)](/en/terms/precision-précision/)
- [recall (rappel)](/en/terms/recall-rappel/)
- [F1 score (score F1)](/en/terms/f1-score-score-f1/)
- [ROC curve (courbe ROC)](/en/terms/roc-curve-courbe-roc/)
