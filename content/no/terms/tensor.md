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
date: '2026-07-18T16:18:22.970357Z'
lastmod: '2026-07-18T16:38:07.052341Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En flerdimensjonal matrise som fungerer som den grunnleggende datastrukturen
  i rammeverk for dyp læring.
---
## Definition

Innen datavitenskap og dyp læring er en tensor et matematisk objekt som generaliserer skalarer, vektorer og matriser til høyere dimensjoner. Den er karakterisert ved sin rang (antall dimensjoner) og form.

### Summary

En flerdimensjonal matrise som fungerer som den grunnleggende datastrukturen i rammeverk for dyp læring.

## Key Concepts

- Rang
- Form
- Dimensjonalitet
- Broadcasting (Automatisk utvidelse av dimensjoner)

## Use Cases

- Bildebehandling (4D-tensorer)
- Lagring av vekter i nevrale nettverk
- Inndata i batcher

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrise (To-dimensjonalt array)](/en/terms/matrise-to-dimensjonalt-array/)
- [Vektor (En-dimensjonalt array)](/en/terms/vektor-en-dimensjonalt-array/)
- [Dyp læring (Underfelt av maskinlæring)](/en/terms/dyp-læring-underfelt-av-maskinlæring/)
- [NumPy (Python-bibliotek for numeriske beregninger)](/en/terms/numpy-python-bibliotek-for-numeriske-beregninger/)
