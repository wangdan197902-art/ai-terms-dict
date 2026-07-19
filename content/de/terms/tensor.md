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
date: '2026-07-18T11:36:08.024244Z'
lastmod: '2026-07-18T11:44:44.991677Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein mehrdimensionales Array, das als grundlegende Datenstruktur für Deep-Learning-Frameworks
  dient.
---
## Definition

In der Informatik und im Deep Learning ist ein Tensor ein mathematisches Objekt, das Skalare, Vektoren und Matrizen auf höhere Dimensionen verallgemeinert. Es wird durch seinen Rang (Anzahl der Dimensionen) charakterisiert.

### Summary

Ein mehrdimensionales Array, das als grundlegende Datenstruktur für Deep-Learning-Frameworks dient.

## Key Concepts

- Rang
- Form
- Dimensionalität
- Broadcasting

## Use Cases

- Bildverarbeitung (4D-Tensoren)
- Speicherung von neuronalen Netzwerkgewichten
- Eingabe batchverarbeiteter Daten

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix](/en/terms/matrix/)
- [Vector](/en/terms/vector/)
- [Deep Learning](/en/terms/deep-learning/)
- [NumPy](/en/terms/numpy/)
