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
  - /nl/terms/softmax/
date: "2026-07-18T15:39:02.757998Z"
lastmod: "2026-07-18T17:15:08.709145Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een wiskundige functie die een vector van willekeurige reële scores omzet in een waarschijnlijkheidsverdeling."
---

## Definition

Softmax wordt veelvuldig gebruikt in de uitvoerlaag van neurale netwerken voor meerclassificatietaken. Het neemt een vector van ruwe logit-waarden en normaliseert deze zodat elk element een waarschijnlijkheid vertegenwoordigt.

### Summary

Een wiskundige functie die een vector van willekeurige reële scores omzet in een waarschijnlijkheidsverdeling.

## Key Concepts

- Waarschijnlijkheidsverdeling
- Logits
- Normalisatie
- Meerclassificatie

## Use Cases

- Uitvoerlagen voor beeldclassificatie
- Tokenvoorspelling in taalmodellen
- Multilabel-categorisering

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (de index van het maximumelement)](/en/terms/argmax-de-index-van-het-maximumelement/)
- [Cross-Entropy Loss (kruisentropieverliesfunctie)](/en/terms/cross-entropy-loss-kruisentropieverliesfunctie/)
- [Logits (ruwe ongenormaliseerde voorspellingen)](/en/terms/logits-ruwe-ongenormaliseerde-voorspellingen/)
- [Neural Network (neuraal netwerk)](/en/terms/neural-network-neuraal-netwerk/)
