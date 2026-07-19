---
title: Softmax
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T15:37:11.703998Z'
lastmod: '2026-07-18T17:15:08.837185Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Funkcja matematyczna przekształcająca wektor dowolnych wartości rzeczywistych
  w rozkład prawdopodobieństwa.
---
## Definition

Softmax jest szeroko stosowany w warstwie wyjściowej sieci neuronowych do zadań klasyfikacji wieloklasowej. Przyjmuje wektor surowych logitów i normalizuje je tak, aby każdy element reprezentował prawdopodobieństwo.

### Summary

Funkcja matematyczna przekształcająca wektor dowolnych wartości rzeczywistych w rozkład prawdopodobieństwa.

## Key Concepts

- Rozkład prawdopodobieństwa
- Logity
- Normalizacja
- Klasyfikacja wieloklasowa

## Use Cases

- Warstwy wyjściowe klasyfikacji obrazów
- Przewidywanie tokenów w modelach językowych
- Kategoryzacja wieloetykietkowa

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (argument maksymalny)](/en/terms/argmax-argument-maksymalny/)
- [Cross-Entropy Loss (funkcja straty entropii krzyżowej)](/en/terms/cross-entropy-loss-funkcja-straty-entropii-krzyżowej/)
- [Logits (surowe oceny/logity)](/en/terms/logits-surowe-oceny-logity/)
- [Neural Network (sieć neuronowa)](/en/terms/neural-network-sieć-neuronowa/)
