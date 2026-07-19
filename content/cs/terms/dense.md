---
title: Hustá vrstva
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:53:20.475266Z'
lastmod: '2026-07-18T17:15:09.121666Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Vrstva nebo tenzor, kde je každý prvek propojen s každým prvkem předchozí
  vrstvy nebo dimenze.
---
## Definition

V neuronových sítích označuje 'hustá' plně propojené vrstvy, kde každý neuron přijímá vstupy ze všech neuronů v předchozí vrstvě. To se kontrastuje s řídkými spoji nalezenými v konvolučních nebo jiných typech vrstev.

### Summary

Vrstva nebo tenzor, kde je každý prvek propojen s každým prvkem předchozí vrstvy nebo dimenze.

## Key Concepts

- Plně propojená
- Váhová matice
- Aktivační funkce
- Integrace funkcí

## Use Cases

- Klasifikační vrstvy v MLP
- Fúze funkcí v hybridních modelech
- Jednoduché regresní úlohy

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Neuronová síť s přímou vazbou)](/en/terms/feedforward-neural-network-neuronová-síť-s-přímou-vazbou/)
- [Backpropagation (Zpětná propagace chyby)](/en/terms/backpropagation-zpětná-propagace-chyby/)
- [ReLU (Aktivační funkce ReLU)](/en/terms/relu-aktivační-funkce-relu/)
- [Bias Term (Posunový člen)](/en/terms/bias-term-posunový-člen/)
