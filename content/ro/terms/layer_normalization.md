---
title: Normalizare pe straturi
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
date: '2026-07-18T16:07:50.475066Z'
lastmod: '2026-07-18T17:15:09.673450Z'
draft: false
source: agnes_llm
status: published
language: ro
description: O tehnică care normalizează activările unui strat de rețea neuronală
  de-a lungul dimensiunii caracteristicilor pentru fiecare eșantion individual.
---
## Definition

Normalizarea pe straturi stabilizează antrenamentul reducând schimbarea covarianței interne, fiind particular eficientă în arhitecturile recurente și transformator. Spre deosebire de Normalizarea pe loturi, care depinde de statisticile lotului, aceasta calculează media și varianța pentru fiecare eșantimon în parte.

### Summary

O tehnică care normalizează activările unui strat de rețea neuronală de-a lungul dimensiunii caracteristicilor pentru fiecare eșantion individual.

## Key Concepts

- Normalizare
- Schimbarea covarianței interne
- Modele Transformator
- RNN-uri

## Use Cases

- Antrenarea modelelor Transformator precum BERT
- Stabilizarea antrenamentului RNN/LSTM
- Învățarea profundă cu dimensiuni mici de lot

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization (normalizare pe loturi)](/en/terms/batch_normalization-normalizare-pe-loturi/)
- [transformer (transformator)](/en/terms/transformer-transformator/)
- [normalization (normalizare)](/en/terms/normalization-normalizare/)
- [deep_learning (învățare profundă)](/en/terms/deep_learning-învățare-profundă/)
