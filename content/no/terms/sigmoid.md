---
title: "Sigmoidfunksjon"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:15:54.365643Z"
lastmod: "2026-07-18T16:38:07.046488Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En matematisk funksjon som avbilder ethvert reelt tall til en verdi mellom null og én, og danner en S-formet kurve."
---
## Definition

Sigmoidfunksjonen, definert som σ(z) = 1 / (1 + e^-z), er mye brukt i maskinlæring for å modellere sannsynligheter. Den komprimerer inndataverdier inn i intervallet (0, 1), noe som gjør den egnet for binær klassifisering.

### Summary

En matematisk funksjon som avbilder ethvert reelt tall til en verdi mellom null og én, og danner en S-formet kurve.

## Key Concepts

- Logistisk funksjon
- Sannsynlighetskartlegging
- Utslående gradient
- Ikke-linearitet

## Use Cases

- Utdata for binær klassifisering
- Logistisk regresjon
- Aktivering i flate nevrale nettverk

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Logistisk regresjon](/en/terms/logistisk-regresjon/)
- [Aktiveringsfunksjon](/en/terms/aktiveringsfunksjon/)
