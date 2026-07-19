---
title: Tanh
term_id: tanh
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- mathematics
difficulty: 2
weight: 1
slug: tanh
date: '2026-07-18T16:19:39.378041Z'
lastmod: '2026-07-18T17:15:09.205430Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Tanh, neboli hyperbolický tangens, je aktivační funkce, která mapuje
  vstupní hodnoty do rozsahu mezi -1 a 1.
---
## Definition

Funkce hyperbolického tangensu (Tanh) je nelineární aktivační funkce běžně používaná v neuronových sítích. Stlačuje vstupní hodnoty do intervalu (-1, 1), což poskytuje výstupy se středem v nule, což usn

### Summary

Tanh, neboli hyperbolický tangens, je aktivační funkce, která mapuje vstupní hodnoty do rozsahu mezi -1 a 1.

## Key Concepts

- Aktivační funkce
- Nelinearita
- Výstup se středem v nule
- Zpětná propagace

## Use Cases

- Rekurentní neuronové sítě
- Brány buněk LSTM
- Skryté vrstvy v MLP

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (sigmoidní funkce)](/en/terms/sigmoid-sigmoidní-funkce/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (neuronové sítě)](/en/terms/neural_networks-neuronové-sítě/)
