---
title: Učení se supervizí
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
date: '2026-07-18T15:38:50.937277Z'
lastmod: '2026-07-18T17:15:09.094297Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Paradigma strojového učení, kde se model učí mapovat vstupy na výstupy
  na základě trénovacích příkladů s označením.
---
## Definition

Při učení se supervizí je algoritmus trénován na sadě dat s označením, což znamená, že každý vstupní příklad je spárován se správným výstupem. Cílem je, aby model naučil vztah mezi vstupy a výstupy.

### Summary

Paradigma strojového učení, kde se model učí mapovat vstupy na výstupy na základě trénovacích příkladů s označením.

## Key Concepts

- Data s označením
- Mapování vstup-výstup
- Klasifikace
- Regrese

## Use Cases

- Detekce spamu v e-mailech
- Predikce cen nemovitostí
- Rozpoznávání obrázků

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (učení bez supervize)](/en/terms/unsupervised-learning-učení-bez-supervize/)
- [Training Set (trénovací sada)](/en/terms/training-set-trénovací-sada/)
- [Validation Set (validační sada)](/en/terms/validation-set-validační-sada/)
- [Model Accuracy (přesnost modelu)](/en/terms/model-accuracy-přesnost-modelu/)
