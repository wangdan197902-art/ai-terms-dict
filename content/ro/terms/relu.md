---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /ro/terms/relu/
date: "2026-07-18T15:37:49.357728Z"
lastmod: "2026-07-18T17:15:09.617999Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Unitatea Linară Rectificată este o funcție de activare care returnează intrarea direct dacă este pozitivă, în caz contrar zero."
---

## Definition

ReLU este utilizată pe scară largă în rețelele neuronale de învățare profundă datorită eficienței sale computaționale și capacității de a atenua problema gradientului care dispare. Definită matematic ca f(x) = max(0, x), introduce non-linearitate în rețea permițând învățarea de reprezentări complexe.

### Summary

Unitatea Linară Rectificată este o funcție de activare care returnează intrarea direct dacă este pozitivă, în caz contrar zero.

## Key Concepts

- Non-linearitate
- Funcție de activare
- Gradient care dispare
- Piecewise linear (liniar pe porțiuni)

## Use Cases

- Straturi ascunse în rețelele convoluționale (CNN)
- Rețele de alimentare profundă (Deep Feedforward Networks)
- Modele de recunoaștere a imaginilor

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (o funcție de activare s-shaped)](/en/terms/sigmoid-o-funcție-de-activare-s-shaped/)
- [Tanh (funcția tangenta hiperbolică)](/en/terms/tanh-funcția-tangenta-hiperbolică/)
- [Leaky ReLU (o variantă a ReLU care permite un gradient mic negativ)](/en/terms/leaky-relu-o-variantă-a-relu-care-permite-un-gradient-mic-negativ/)
- [Neural Network (rețea neuronală)](/en/terms/neural-network-rețea-neuronală/)
