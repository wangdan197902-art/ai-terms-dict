---
title: Piilotettu kerros
term_id: hidden_layer
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- Deep Learning
difficulty: 3
weight: 1
slug: hidden_layer
date: '2026-07-18T16:01:09.936874Z'
lastmod: '2026-07-18T17:15:09.418785Z'
draft: false
source: agnes_llm
status: published
language: fi
description: Syväoppimismallissa syöte- ja tulokerrosten välinen välillinen kerros,
  joka prosessoi ominaisuuksia.
---
## Definition

Piilotettu kerros koostuu neuroneista, jotka vastaanottavat syötteitä edellisistä kerroksista, soveltavat painoja ja vakiolukuja sekä välittävät muunnetun datan eteenpäin aktivointifunktion kautta. Nämä kerrokset mahdollistavat neuroverkkojen monimutkaisten kuvioiden oppimisen.

### Summary

Syväoppimismallissa syöte- ja tulokerrosten välinen välillinen kerros, joka prosessoi ominaisuuksia.

## Key Concepts

- Neuroverkot
- Ominaisuuksien erottelu
- Aktivointifunktiot
- Syväoppiminen

## Use Cases

- Kuvantunnistusjärjestelmät
- Luonnollisen kielen käsittelymallit
- Ennakoiva analytiikka

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)
```

## Related Terms

- [neuron (neuroni)](/en/terms/neuron-neuroni/)
- [backpropagation (takaisinpropagaatio)](/en/terms/backpropagation-takaisinpropagaatio/)
- [activation_function (aktivointifunktio)](/en/terms/activation_function-aktivointifunktio/)
- [deep_learning (syväoppiminen)](/en/terms/deep_learning-syväoppiminen/)
