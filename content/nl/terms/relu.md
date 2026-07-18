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
  - /nl/terms/relu/
date: "2026-07-18T15:38:35.775040Z"
lastmod: "2026-07-18T17:15:08.708241Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Rectified Linear Unit is een activatiefunctie die de invoer direct uitvoert als deze positief is, anders nul."
---

## Definition

ReLU wordt veel gebruikt in neurale netwerken voor deep learning vanwege zijn rekenkundige efficiëntie en vermogen om het probleem van vervagende gradiënten te verzachten. Wiskundig gedefinieerd als f(x) = max(0, x), introduceert het niet-lineariteit.

### Summary

Rectified Linear Unit is een activatiefunctie die de invoer direct uitvoert als deze positief is, anders nul.

## Key Concepts

- Niet-lineariteit
- Activatiefunctie
- Vervagende gradiënt
- Stuksgewijs lineair

## Use Cases

- Verborgen lagen in CNN's
- Diepe feedforward-netwerken
- Modellen voor beeldherkenning

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (sigmoidfunctie)](/en/terms/sigmoid-sigmoidfunctie/)
- [Tanh (hyperbolische tangens)](/en/terms/tanh-hyperbolische-tangens/)
- [Leaky ReLU (lekke rectified linear unit)](/en/terms/leaky-relu-lekke-rectified-linear-unit/)
- [Neural Network (neuraal netwerk)](/en/terms/neural-network-neuraal-netwerk/)
