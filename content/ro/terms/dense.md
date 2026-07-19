---
title: Dens
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:54:13.484560Z'
lastmod: '2026-07-18T17:15:09.647315Z'
draft: false
source: agnes_llm
status: published
language: ro
description: Un strat sau un tensor în care fiecare element este conectat la fiecare
  element al stratului sau dimensiunii anterioare.
---
## Definition

În rețelele neuronale, termenul 'dens' se referă la straturile complet conectate, în care fiecare neuron primește intrări de la toți neuronii din stratul precedent. Acest lucru contrastează cu conexiunile rare întâlnite în rețelele convoluționale sau...

### Summary

Un strat sau un tensor în care fiecare element este conectat la fiecare element al stratului sau dimensiunii anterioare.

## Key Concepts

- Complet Conectat
- Matrice de Greutăți
- Funcție de Activare
- Integrarea Caracteristicilor

## Use Cases

- Straturi finale de clasificare în MLP-uri
- Fuziunea caracteristicilor în modele hibride
- Sarcini simple de regresie

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Rețea Neurală Feedforward (Rețea neuronală cu propagare înainte)](/en/terms/rețea-neurală-feedforward-rețea-neuronală-cu-propagare-înainte/)
- [Backpropagation (Propagarea înapoi a erorii)](/en/terms/backpropagation-propagarea-înapoi-a-erorii/)
- [ReLU (Funcția de activare lineară parțială)](/en/terms/relu-funcția-de-activare-lineară-parțială/)
- [Bias Term (Termen de bias/pivot)](/en/terms/bias-term-termen-de-bias-pivot/)
