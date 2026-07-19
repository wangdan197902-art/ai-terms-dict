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
date: '2026-07-18T15:38:32.319980Z'
lastmod: '2026-07-18T17:15:09.375270Z'
draft: false
source: agnes_llm
status: published
language: fi
description: Matemaattinen funktio, joka muuntaa mielivaltaisten reaalilukuarvojen
  vektorin todennäköisyysjakaumaksi.
---
## Definition

Softmaxia käytetään laajasti moniluokkaiseen luokitteluun tarkoitettujen neuroverkkojen ulostulokerroksessa. Se ottaa raakojen logit-arvojen vektorin ja normalisoi ne siten, että kukin alkio edustaa todennäköisyyttä.

### Summary

Matemaattinen funktio, joka muuntaa mielivaltaisten reaalilukuarvojen vektorin todennäköisyysjakaumaksi.

## Key Concepts

- Todennäköisyysjakauma
- Logitit
- Normalisointi
- Moniluokkainen luokittelu

## Use Cases

- Kuvien luokittelun ulostulokerrokset
- Kieliomallien token-ennusteet
- Monilabeliluokitus

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (maksimiarvon indeksi)](/en/terms/argmax-maksimiarvon-indeksi/)
- [Risti-entropiahäviö](/en/terms/risti-entropiahäviö/)
- [Logitit](/en/terms/logitit/)
- [Neuroverkko](/en/terms/neuroverkko/)
