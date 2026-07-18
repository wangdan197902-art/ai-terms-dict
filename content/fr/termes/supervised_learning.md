---
title: "Apprentissage supervisé"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /fr/terms/supervised_learning/
date: "2026-07-18T11:01:39.206540Z"
lastmod: "2026-07-18T11:44:45.189528Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Un paradigme d'apprentissage automatique où un modèle apprend à mapper des entrées vers des sorties basé sur des exemples d'entraînement étiquetés."
---

## Definition

En apprentissage supervisé, l'algorithme est entraîné sur un jeu de données étiqueté, ce qui signifie que chaque exemple d'entrée est associé à la sortie correcte. L'objectif est que le modèle apprenne la relation sous-jacente entre les entrées et les sorties.

### Summary

Un paradigme d'apprentissage automatique où un modèle apprend à mapper des entrées vers des sorties basé sur des exemples d'entraînement étiquetés.

## Key Concepts

- Données étiquetées
- Mappage entrée-sortie
- Classification
- Régression

## Use Cases

- Détection de courriels indésirables
- Prédiction des prix immobiliers
- Reconnaissance d'images

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Apprentissage non supervisé (apprentissage sans étiquettes)](/en/terms/apprentissage-non-supervisé-apprentissage-sans-étiquettes/)
- [Jeu d'entraînement (données utilisées pour apprendre le modèle)](/en/terms/jeu-d-entraînement-données-utilisées-pour-apprendre-le-modèle/)
- [Jeu de validation (données utilisées pour ajuster les hyperparamètres)](/en/terms/jeu-de-validation-données-utilisées-pour-ajuster-les-hyperparamètres/)
- [Précision du modèle (mesure de performance)](/en/terms/précision-du-modèle-mesure-de-performance/)
