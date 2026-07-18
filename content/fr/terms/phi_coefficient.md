---
title: "Coefficient Phi"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /fr/terms/phi_coefficient/
date: "2026-07-18T11:33:47.558581Z"
lastmod: "2026-07-18T11:44:45.311976Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Une mesure statistique de l'association entre deux variables binaires."
---

## Definition

Le coefficient Phi (φ) est une mesure d'association pour deux variables binaires, servant de coefficient de corrélation de Pearson pour les variables dichotomiques. Il varie de -1 à +1, où 0 indique aucune association.

### Summary

Une mesure statistique de l'association entre deux variables binaires.

## Key Concepts

- Variables binaires
- Corrélation
- Table de contingence
- Force de l'association

## Use Cases

- Évaluation des performances des classifieurs binaires au-delà de la précision
- Analyse des relations dans les données de sondage avec des réponses oui/non
- Sélection de fonctionnalités dans les ensembles de données avec des entrées catégorielles

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [V de Cramér (Mesure d'association pour les variables catégorielles)](/en/terms/v-de-cramér-mesure-d-association-pour-les-variables-catégorielles/)
- [Corrélation de Pearson (Mesure de linéarité entre variables continues)](/en/terms/corrélation-de-pearson-mesure-de-linéarité-entre-variables-continues/)
- [Matrice de confusion (Table résumant les performances d'un classifieur)](/en/terms/matrice-de-confusion-table-résumant-les-performances-d-un-classifieur/)
- [Information mutuelle (Mesure de dépendance statistique entre variables)](/en/terms/information-mutuelle-mesure-de-dépendance-statistique-entre-variables/)
