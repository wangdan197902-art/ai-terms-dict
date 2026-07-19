---
title: Tät
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:53:37.376405Z'
lastmod: '2026-07-18T17:15:08.995090Z'
draft: false
source: agnes_llm
status: published
language: sv
description: Ett lager eller en tensor där varje element är anslutet till varje element
  i det föregående lagret eller dimensionen.
---
## Definition

Inom neurala nätverk syftar 'tät' på fullt anslutna lager där varje neuron tar emot input från alla neuroner i det föregående lagret. Detta står i kontrast till de glesare anslutningar som finns i konvolutionära eller

### Summary

Ett lager eller en tensor där varje element är anslutet till varje element i det föregående lagret eller dimensionen.

## Key Concepts

- Fullt ansluten
- Viktmatris
- Aktiveringsfunktion
- Funktionintegration

## Use Cases

- Slutklassificeringslager i MLP:er
- Fusionslager för funktioner i hybrida modeller
- Enkla regressionsuppgifter

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Framåtriktat neuralt nätverk)](/en/terms/feedforward-neural-network-framåtriktat-neuralt-nätverk/)
- [Backpropagation (Bakåtpropagering)](/en/terms/backpropagation-bakåtpropagering/)
- [ReLU (Rectified Linear Unit)](/en/terms/relu-rectified-linear-unit/)
- [Bias Term (Biasterm)](/en/terms/bias-term-biasterm/)
