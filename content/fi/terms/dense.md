---
title: Tiheä kerros
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:54:06.289523Z'
lastmod: '2026-07-18T17:15:09.403314Z'
draft: false
source: agnes_llm
status: published
language: fi
description: Kerros tai tensori, jossa jokainen elementti on yhdistetty jokaiseen
  edellisen kerroksen tai ulottuvuuden elementtiin.
---
## Definition

Neuroverkoissa 'tiheä' viittaa täysin yhteenliitettyihin kerroksiin, joissa kukin neuroni saa syötteen kaikilta edellisen kerroksen neuroneilta. Tämä eroaa harvinaisista yhteyksistä, joita esiintyy esimerkiksi konvoluutio- tai...

### Summary

Kerros tai tensori, jossa jokainen elementti on yhdistetty jokaiseen edellisen kerroksen tai ulottuvuuden elementtiin.

## Key Concepts

- Täysin yhteenliitetty
- Painomatriisi
- Aktivaatiofunktio
- Ominaisuuksien integrointi

## Use Cases

- Lopulliset luokittelukerrokset monikerroksisissa perceptroneissa (MLP)
- Ominaisuuksien fuusio hybridimalleissa
- Yksinkertaiset regressiotehtävät

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Eteenpäin suuntautunut neuroverkko)](/en/terms/feedforward-neural-network-eteenpäin-suuntautunut-neuroverkko/)
- [Backpropagation (Takasulkulaskenta)](/en/terms/backpropagation-takasulkulaskenta/)
- [ReLU (Rectified Linear Unit - aktivaatiofunktio)](/en/terms/relu-rectified-linear-unit-aktivaatiofunktio/)
- [Bias Term (Vakiotermi)](/en/terms/bias-term-vakiotermi/)
