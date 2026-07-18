---
title: "Évaluation des classificateurs binaires"
term_id: "evaluation_of_binary_classifiers"
category: "basic_concepts"
subcategory: ""
tags: ["metrics", "classification", "evaluation"]
difficulty: 2
weight: 1
slug: "evaluation_of_binary_classifiers"
aliases:
  - /fr/terms/evaluation_of_binary_classifiers/
date: "2026-07-18T11:16:12.645186Z"
lastmod: "2026-07-18T11:44:45.247687Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Le processus d'évaluation des performances des modèles d'apprentissage automatique qui prédisent l'une des deux issues possibles."
---

## Definition

Ce domaine implique l'analyse de métriques telles que la précision globale (accuracy), la précision (precision), le rappel (recall), le score F1 et l'Aire sous la courbe ROC (AUC-ROC). Cela permet de déterminer dans quelle mesure un modèle fonctionne bien pour distinguer les deux classes.

### Summary

Le processus d'évaluation des performances des modèles d'apprentissage automatique qui prédisent l'une des deux issues possibles.

## Key Concepts

- Matrice de confusion
- Compromis Précision-Rappel
- Courbe ROC
- Score F1

## Use Cases

- Dépistage médical des maladies
- Filtrage des courriels indésirables (spam)
- Évaluation du risque de crédit

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (matrice de confusion)](/en/terms/confusion_matrix-matrice-de-confusion/)
- [roc_auc (aire sous la courbe ROC)](/en/terms/roc_auc-aire-sous-la-courbe-roc/)
- [precision_recall (précision et rappel)](/en/terms/precision_recall-précision-et-rappel/)
- [cross_validation (validation croisée)](/en/terms/cross_validation-validation-croisée/)
