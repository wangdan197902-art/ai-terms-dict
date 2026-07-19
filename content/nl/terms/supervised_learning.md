---
title: Bewaakt Leren
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T15:39:02.758017Z'
lastmod: '2026-07-18T17:15:08.709490Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Een machine learning-paradigma waarbij een model leert om invoer naar
  uitvoer te mappen op basis van gelabelde trainingsvoorbeelden.
---
## Definition

Bij bewaakt leren wordt het algoritme getraind op een gelabelde dataset, wat betekent dat elk invoervoorbeeld gepaard gaat met de juiste uitvoer. Het doel is dat het model de onderliggende relatie leert tussen invoer en uitvoer.

### Summary

Een machine learning-paradigma waarbij een model leert om invoer naar uitvoer te mappen op basis van gelabelde trainingsvoorbeelden.

## Key Concepts

- Gelabelde Gegevens
- Invoer-Uitvoer Mapping
- Classificatie
- Regressie

## Use Cases

- Detectie van spam-e-mails
- Voorspelling van huizenprijzen
- Beeldherkenning

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (onbewaakt leren)](/en/terms/unsupervised-learning-onbewaakt-leren/)
- [Training Set (trainingsset)](/en/terms/training-set-trainingsset/)
- [Validation Set (validatieset)](/en/terms/validation-set-validatieset/)
- [Model Accuracy (modelnauwkeurigheid)](/en/terms/model-accuracy-modelnauwkeurigheid/)
