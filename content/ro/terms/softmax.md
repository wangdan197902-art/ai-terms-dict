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
date: '2026-07-18T15:38:35.785290Z'
lastmod: '2026-07-18T17:15:09.619032Z'
draft: false
source: agnes_llm
status: published
language: ro
description: O funcție matematică care convertește un vector de scoruri reale arbitrare
  într-o distribuție de probabilitate.
---
## Definition

Softmax este utilizat pe scară largă în stratul de ieșire al rețelelor neuronale pentru sarcini de clasificare multi-clasă. Preia un vector de logaritmi brute (logits) și îi normalizează astfel încât fiecare element să reprezinte o probabilitate.

### Summary

O funcție matematică care convertește un vector de scoruri reale arbitrare într-o distribuție de probabilitate.

## Key Concepts

- Distribuție de probabilitate
- Logaritmi (Logits)
- Normalizare
- Clasificare multi-clasă

## Use Cases

- Straturi de ieșire pentru clasificarea imaginilor
- Predicția tokenurilor în modelele lingvistice
- Categorizarea multi-etichetă

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (funcția care returnează indexul valorii maxime)](/en/terms/argmax-funcția-care-returnează-indexul-valorii-maxime/)
- [Pierderea entropiei încrucișate (Cross-Entropy Loss)](/en/terms/pierderea-entropiei-încrucișate-cross-entropy-loss/)
- [Logaritmi (Logits)](/en/terms/logaritmi-logits/)
- [Rețea neuronală (Neural Network)](/en/terms/rețea-neuronală-neural-network/)
