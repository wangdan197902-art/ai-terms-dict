---
title: "Données étiquetées"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /fr/terms/labeled_data/
date: "2026-07-18T11:25:14.947305Z"
lastmod: "2026-07-18T11:44:45.282791Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Données pour lesquelles la sortie correcte ou la valeur cible est fournie avec les caractéristiques d'entrée."
---

## Definition

Les données étiquetées consistent en des échantillons d'entrée associés à des étiquettes de vérité terrain correspondantes, servant de fondement à l'apprentissage supervisé. Elles permettent aux algorithmes d'apprendre la mappage entre l'entrée et la sortie.

### Summary

Données pour lesquelles la sortie correcte ou la valeur cible est fournie avec les caractéristiques d'entrée.

## Key Concepts

- Apprentissage supervisé
- Vérité terrain
- Annotation
- Variable cible

## Use Cases

- Entraînement de classificateurs d'images
- Construction de systèmes de reconnaissance vocale
- Modélisation prédictive en finance

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (données non étiquetées)](/en/terms/unlabeled_data-données-non-étiquetées/)
- [supervised_learning (apprentissage supervisé)](/en/terms/supervised_learning-apprentissage-supervisé/)
- [data_annotation (annotation de données)](/en/terms/data_annotation-annotation-de-données/)
- [training_set (ensemble d'entraînement)](/en/terms/training_set-ensemble-d-entraînement/)
