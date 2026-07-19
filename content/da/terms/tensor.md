---
title: Tensor
term_id: tensor
category: basic_concepts
subcategory: ''
tags:
- math
- Data Structures
- pytorch
difficulty: 2
weight: 1
slug: tensor
date: '2026-07-18T16:22:10.770731Z'
lastmod: '2026-07-18T17:15:09.336298Z'
draft: false
source: agnes_llm
status: published
language: da
description: En multidimensionel matrix, der fungerer som den grundlæggende datastruktur
  for dyrlæringsrammer.
---
## Definition

Informatik og dyrlæring: En tensor er et matematisk objekt, der generaliserer skalarer, vektorer og matricer til højere dimensioner. Den er kendetegnet ved sin rang (antal dimensioner) og form.

### Summary

En multidimensionel matrix, der fungerer som den grundlæggende datastruktur for dyrlæringsrammer.

## Key Concepts

- Rank
- Form
- Dimensionalitet
- Broadcasting

## Use Cases

- Billedebehandling (4D-tensorer)
- Opbevaring af neurale netværksvægte
- Batch-inddata

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix (Matrix)](/en/terms/matrix-matrix/)
- [Vector (Vektor)](/en/terms/vector-vektor/)
- [Deep Learning (Dyrlæring)](/en/terms/deep-learning-dyrlæring/)
- [NumPy (NumPy-bibliotek)](/en/terms/numpy-numpy-bibliotek/)
