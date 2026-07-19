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
date: '2026-07-18T15:38:50.937203Z'
lastmod: '2026-07-18T17:15:09.093890Z'
draft: false
source: agnes_llm
status: published
language: cs
description: Matematická funkce, která převádí vektor libovolných reálných skóre na
  pravděpodobnostní rozdělení.
---
## Definition

Softmax je široce používán ve výstupní vrstvě neuronových sítí pro úlohy víceklasifikace. Přijímá vektor surových logitů a normalizuje je tak, že každý prvek představuje pravděpodobnost příslušnosti k dané třídě.

### Summary

Matematická funkce, která převádí vektor libovolných reálných skóre na pravděpodobnostní rozdělení.

## Key Concepts

- Pravděpodobnostní rozdělení
- Logity
- Normalizace
- Víceklasifikace

## Use Cases

- Výstupní vrstvy pro klasaci obrázků
- Predikce tokenů v jazykových modelech
- Kategorizace více štítků

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (funkce pro nalezení indexu maximální hodnoty)](/en/terms/argmax-funkce-pro-nalezení-indexu-maximální-hodnoty/)
- [Cross-Entropy Loss (křížová entropie jako funkce ztráty)](/en/terms/cross-entropy-loss-křížová-entropie-jako-funkce-ztráty/)
- [Logits (surové ne-normalizované výstupy modelu)](/en/terms/logits-surové-ne-normalizované-výstupy-modelu/)
- [Neural Network (neuronová síť)](/en/terms/neural-network-neuronová-síť/)
