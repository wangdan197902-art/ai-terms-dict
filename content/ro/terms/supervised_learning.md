---
title: Învățare supravegheată
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
date: '2026-07-18T15:38:35.785312Z'
lastmod: '2026-07-18T17:15:09.619479Z'
draft: false
source: agnes_llm
status: published
language: ro
description: Un paradigmă de învățare automată în care un model învață să mapeze intrările
  la ieșiri pe baza exemplelor de antrenament etichetate.
---
## Definition

În învățarea supravegheată, algoritmul este antrenat pe un set de date etichetat, ceea ce înseamnă că fiecare exemplu de intrare este asociat cu ieșirea corectă. Scopul este ca modelul să învețe relația subiacentă dintre intrări și ieșiri.

### Summary

Un paradigmă de învățare automată în care un model învață să mapeze intrările la ieșiri pe baza exemplelor de antrenament etichetate.

## Key Concepts

- Date etichetate
- Mapare intrare-ieșire
- Clasificare
- Regresie

## Use Cases

- Detectarea spam-ului în e-mailuri
- Predicția prețurilor imobilelor
- Recunoașterea imaginilor

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Învățare nesupravegheată](/en/terms/învățare-nesupravegheată/)
- [Set de antrenament](/en/terms/set-de-antrenament/)
- [Set de validare](/en/terms/set-de-validare/)
- [Precizia modelului](/en/terms/precizia-modelului/)
