---
title: Superviseret læring
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
date: '2026-07-18T15:37:59.426736Z'
lastmod: '2026-07-18T17:15:09.250604Z'
draft: false
source: agnes_llm
status: published
language: da
description: Et maskinlæringsparadigme, hvor en model lærer at kortlægge input til
  outputs baseret på mærkede træningseksempler.
---
## Definition

I superviseret læring trænes algoritmen på et mærket datasæt, hvilket betyder, at hvert inputeksempel er parret med det korrekte output. Målet er, at modellen skal lære den underliggende sammenhæng mellem input og output.

### Summary

Et maskinlæringsparadigme, hvor en model lærer at kortlægge input til outputs baseret på mærkede træningseksempler.

## Key Concepts

- Mærkede data
- Input-output-kortlægning
- Klassificering
- Regression

## Use Cases

- Detektion af spam-e-mails
- Prisprognose for boliger
- Billedgenkendelse

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (ultra superviseret læring)](/en/terms/unsupervised-learning-ultra-superviseret-læring/)
- [Training Set (træningsdatasæt)](/en/terms/training-set-træningsdatasæt/)
- [Validation Set (valideringssæt)](/en/terms/validation-set-valideringssæt/)
- [Model Accuracy (modellens nøjagtighed)](/en/terms/model-accuracy-modellens-nøjagtighed/)
