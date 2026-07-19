---
title: Volledig verbonden
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:51:03.977199Z'
lastmod: '2026-07-18T17:15:08.736944Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Een laag of tensor waarbij elk element verbonden is met elk element van
  de vorige laag of dimensie.
---
## Definition

In neurale netwerken verwijst 'volledig verbonden' naar lagen waarin elke neuron input ontvangt van alle neuronen in de voorgaande laag. Dit staat in contrast met de spaarzame verbindingen die voorkomen in convolutie- of

### Summary

Een laag of tensor waarbij elk element verbonden is met elk element van de vorige laag of dimensie.

## Key Concepts

- Volledig verbonden
- Gewichtsmatrix
- Activatiefunctie
- Functie-integratie

## Use Cases

- Classificatielagen in MLP's
- Fusie van kenmerken in hybride modellen
- Eenvoudige regressietaken

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neurale Netwerk (Neuraal netwerk zonder terugkoppeling)](/en/terms/feedforward-neurale-netwerk-neuraal-netwerk-zonder-terugkoppeling/)
- [Backpropagatie (Terugpropageren van fouten)](/en/terms/backpropagatie-terugpropageren-van-fouten/)
- [ReLU (Rectified Linear Unit)](/en/terms/relu-rectified-linear-unit/)
- [Bias-term (Verschuivingsparameter)](/en/terms/bias-term-verschuivingsparameter/)
