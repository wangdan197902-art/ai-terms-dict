---
title: "Sigmoïde"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
aliases:
  - /fr/terms/sigmoid/
date: "2026-07-18T11:37:32.319204Z"
lastmod: "2026-07-18T11:44:45.327207Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Une fonction mathématique qui mappe n'importe quel nombre réel dans une valeur comprise entre zéro et un, formant une courbe en forme de S."
---

## Definition

La fonction sigmoïde, définie par σ(z) = 1 / (1 + e^-z), est largement utilisée en apprentissage automatique pour modéliser des probabilités. Elle comprime les valeurs d'entrée dans l'intervalle (0, 1), ce qui la rend adaptée à la classification binaire.

### Summary

Une fonction mathématique qui mappe n'importe quel nombre réel dans une valeur comprise entre zéro et un, formant une courbe en forme de S.

## Key Concepts

- Fonction logistique
- Mappage de probabilité
- Disparition du gradient
- Non-linéarité

## Use Cases

- Sortie de classification binaire
- Régression logistique
- Activation dans les réseaux de neurones peu profonds

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU (Fonction d'activation linéaire rectifiée)](/en/terms/relu-fonction-d-activation-linéaire-rectifiée/)
- [Softmax (Fonction de normalisation exponentielle)](/en/terms/softmax-fonction-de-normalisation-exponentielle/)
- [Logistic Regression (Régression logistique)](/en/terms/logistic-regression-régression-logistique/)
- [Activation Function (Fonction d'activation)](/en/terms/activation-function-fonction-d-activation/)
