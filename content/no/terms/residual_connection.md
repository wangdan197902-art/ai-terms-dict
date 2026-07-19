---
title: Restforbindelse
term_id: residual_connection
category: basic_concepts
subcategory: ''
tags:
- architecture
- Optimization
- Deep Learning
difficulty: 3
weight: 1
slug: residual_connection
date: '2026-07-18T15:38:34.878744Z'
lastmod: '2026-07-18T16:38:06.962281Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En mekanisme som legger til input direkte på utgangen av et lag for å
  lette gradientflyt i dype nettverk.
---
## Definition

Restforbindelser, også kjent som hoppforbindelser (skip connections), lar gradienter fly gjennom et nettverk ved å legge til en input direkte på utgangen av et påfølgende lag. Denne arkitekturen løser problemet med forsvinnende gradienter (vanishing gradient problem) og muliggjør trening av svært dype neurale nettverk.

### Summary

En mekanisme som legger til input direkte på utgangen av et lag for å lette gradientflyt i dype nettverk.

## Key Concepts

- Hoppforbindelser
- Problemet med forsvinnende gradienter
- Dyp residuell læring
- Gradientflyt

## Use Cases

- Trening av dype konvolusjonelle neurale nettverk
- Transformer-arkitekturer
- Modeller for bildeklassifisering

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (hoppforbindelse)](/en/terms/skip_connection-hoppforbindelse/)
- [vanishing_gradient (forsvinnende gradient)](/en/terms/vanishing_gradient-forsvinnende-gradient/)
- [deep_learning (dyp læring)](/en/terms/deep_learning-dyp-læring/)
- [resnet (Residual Network)](/en/terms/resnet-residual-network/)
