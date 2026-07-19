---
title: Övervakad inlärning
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
date: '2026-07-18T15:40:47.756409Z'
lastmod: '2026-07-18T17:15:08.967584Z'
draft: false
source: agnes_llm
status: published
language: sv
description: En paradigm inom maskininlärning där en modell lär sig att mappa indata
  till utdata baserat på märkta träningsexempel.
---
## Definition

Inom övervakad inlärning tränas algoritmen på ett märkt dataset, vilket innebär att varje indataexempel är kopplat till rätt utdata. Målet är att modellen ska lära sig det underliggande sambandet mellan in- och utdata.

### Summary

En paradigm inom maskininlärning där en modell lär sig att mappa indata till utdata baserat på märkta träningsexempel.

## Key Concepts

- Märkt data
- In-data-ut-data-mappning
- Klassificering
- Regression

## Use Cases

- Detektering av skräppost i e-post
- Prisprognos för bostäder
- Bildigenkänning

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Oövervakad inlärning (Unsupervised Learning)](/en/terms/oövervakad-inlärning-unsupervised-learning/)
- [Träningsset (Training Set)](/en/terms/träningsset-training-set/)
- [Valideringsset (Validation Set)](/en/terms/valideringsset-validation-set/)
- [Modellnoggrannhet (Model Accuracy)](/en/terms/modellnoggrannhet-model-accuracy/)
