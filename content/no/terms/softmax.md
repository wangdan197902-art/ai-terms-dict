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
date: '2026-07-18T15:38:52.976074Z'
lastmod: '2026-07-18T16:38:06.962900Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: En matematisk funksjon som konverterer en vektor med vilkårlige reelle
  verdier til en sannsynlighetsfordeling.
---
## Definition

Softmax brukes mye i utlagret av nevrale nettverk for flerklasses klassifiseringsoppgaver. Den tar en vektor med rå logitter og normaliserer dem slik at hvert element representerer en sannsynlighet for at klassen er riktig.

### Summary

En matematisk funksjon som konverterer en vektor med vilkårlige reelle verdier til en sannsynlighetsfordeling.

## Key Concepts

- Sannsynlighetsfordeling
- Logitter
- Normalisering
- Flerklasses klassifisering

## Use Cases

- Utgangslag for bildeklassifisering
- Tokenprediksjon i språkmodeller
- Multiklasse-kategorisering

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (funksjon for å finne indeksen til maksimumsverdien)](/en/terms/argmax-funksjon-for-å-finne-indeksen-til-maksimumsverdien/)
- [Kryssentropitap (måling av forskjellen mellom to sannsynlighetsfordelinger)](/en/terms/kryssentropitap-måling-av-forskjellen-mellom-to-sannsynlighetsfordelinger/)
- [Logitter (ubehandlede prediksjoner fra et nettverk)](/en/terms/logitter-ubehandlede-prediksjoner-fra-et-nettverk/)
- [Nevralt nettverk (datamodell inspirert av biologiske nerver)](/en/terms/nevralt-nettverk-datamodell-inspirert-av-biologiske-nerver/)
