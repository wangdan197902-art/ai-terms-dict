---
title: Lagsnormalisering
term_id: layer_normalization
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Optimization
- architecture
difficulty: 3
weight: 1
slug: layer_normalization
date: '2026-07-18T16:02:08.005844Z'
lastmod: '2026-07-18T16:38:07.017821Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En teknikk som normaliserer aktivitetene til et nevralt nettverkslag
  over dimensjonen for funksjoner for hver enkelt prøve.
---
## Definition

Lagsnormalisering stabiliserer treningen ved å redusere intern kovariansforskyvning, spesielt effektiv i rekurrente og transformerarkitekturer. I motsetning til batchnormalisering, som avhenger av batchstat

### Summary

En teknikk som normaliserer aktivitetene til et nevralt nettverkslag over dimensjonen for funksjoner for hver enkelt prøve.

## Key Concepts

- Normalisering
- Intern kovariansforskyvning
- Transformermodeller
- RNN-er

## Use Cases

- Trening av Transformer-modeller som BERT
- Stabilisering av RNN/LSTM-trening
- Dyp læring med små batchstørrelser

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization (batchnormalisering)](/en/terms/batch_normalization-batchnormalisering/)
- [transformer (transformer)](/en/terms/transformer-transformer/)
- [normalization (normalisering)](/en/terms/normalization-normalisering/)
- [deep_learning (dyp læring)](/en/terms/deep_learning-dyp-læring/)
