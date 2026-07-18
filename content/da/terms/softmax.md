---
title: "Softmax"
term_id: "softmax"
category: "basic_concepts"
subcategory: ""
tags: ["math", "neural-networks", "classification"]
difficulty: 2
weight: 1
slug: "softmax"
aliases:
  - /da/terms/softmax/
date: "2026-07-18T15:37:59.426711Z"
lastmod: "2026-07-18T17:15:09.250147Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En matematisk funktion, der konverterer en vektor af vilkårlige reelle værdier til en sandsynlighedsfordeling."
---

## Definition

Softmax bruges bredt i outputlaget af neurale netværk til opgaver med klassificering af flere klasser. Den tager en vektor af rå logit-værdier og normaliserer dem, så hvert element repræsenterer en sandsynlighed for den pågældende klasse.

### Summary

En matematisk funktion, der konverterer en vektor af vilkårlige reelle værdier til en sandsynlighedsfordeling.

## Key Concepts

- Sandsynlighedsfordeling
- Logits
- Normalisering
- Klassificering af flere klasser

## Use Cases

- Outputlag til billedklassificering
- Token-prediktion i sprogmodeller
- Kategorisering med flere etiketter

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (funktion til at finde indekset for maksimumsværdien)](/en/terms/argmax-funktion-til-at-finde-indekset-for-maksimumsværdien/)
- [Cross-Entropy Loss (tabfunktion til klassificering)](/en/terms/cross-entropy-loss-tabfunktion-til-klassificering/)
- [Logits (ur-normaliserede outputværdier)](/en/terms/logits-ur-normaliserede-outputværdier/)
- [Neural Network (neuronetværk)](/en/terms/neural-network-neuronetværk/)
