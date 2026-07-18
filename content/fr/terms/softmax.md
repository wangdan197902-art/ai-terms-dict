---
title: "Softmax"
term_id: "softmax"
category: "basic_concepts"
subcategory: ""
tags: ["math", "neural-networks", "classification"]
difficulty: 2
weight: 1
slug: "softmax"
aliases:
  - /fr/terms/softmax/
date: "2026-07-18T11:01:39.206467Z"
lastmod: "2026-07-18T11:44:45.189036Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Une fonction mathématique qui convertit un vecteur de scores réels arbitraires en une distribution de probabilité."
---

## Definition

Le Softmax est largement utilisé dans la couche de sortie des réseaux de neurones pour les tâches de classification multi-classe. Il prend un vecteur de logis bruts et les normalise afin que chaque élément représente une probabilité.

### Summary

Une fonction mathématique qui convertit un vecteur de scores réels arbitraires en une distribution de probabilité.

## Key Concepts

- Distribution de probabilité
- Logis
- Normalisation
- Classification multi-classe

## Use Cases

- Couches de sortie de classification d'images
- Prédiction de tokens par les modèles de langage
- Catégorisation multi-étiquettes

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (fonction renvoyant l'indice de la valeur maximale)](/en/terms/argmax-fonction-renvoyant-l-indice-de-la-valeur-maximale/)
- [Perte d'entropie croisée (mesure de différence entre deux distributions de probabilité)](/en/terms/perte-d-entropie-croisée-mesure-de-différence-entre-deux-distributions-de-probabilité/)
- [Logis (scores non normalisés avant activation)](/en/terms/logis-scores-non-normalisés-avant-activation/)
- [Réseau de neurones (modèle informatique inspiré du cerveau)](/en/terms/réseau-de-neurones-modèle-informatique-inspiré-du-cerveau/)
