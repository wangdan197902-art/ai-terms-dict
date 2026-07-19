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
date: '2026-07-18T16:18:05.557523Z'
lastmod: '2026-07-18T16:38:07.052019Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: Tanh, eller hyperbolsk tangens, er en aktiveringsfunksjon som kartlegger
  input-verdier til et intervall mellom -1 og 1.
---
## Definition

Den hyperbolske tangens-funksjonen (Tanh) er en ikke-lineær aktiveringsfunksjon som ofte brukes i nevrale nettverk. Den presser input-verdier inn i intervallet (-1, 1), og gir nullsentrerte utganger som c

### Summary

Tanh, eller hyperbolsk tangens, er en aktiveringsfunksjon som kartlegger input-verdier til et intervall mellom -1 og 1.

## Key Concepts

- Aktiveringsfunksjon
- Ikke-linearitet
- Nullsentrert utgang
- Tilbakepropagering

## Use Cases

- Rekursive nevrale nettverk
- LSTM-celleporter
- Skjulte lag i MLPs

## Code Example

```python
import numpy as np
def tanh(x):
    return np.tanh(x)
```

## Related Terms

- [sigmoid (sigmoidfunksjon)](/en/terms/sigmoid-sigmoidfunksjon/)
- [relu (ReLU)](/en/terms/relu-relu/)
- [neural_networks (nevrale nettverk)](/en/terms/neural_networks-nevrale-nettverk/)
