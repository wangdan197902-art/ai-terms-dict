---
title: "Sigmoid"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:21:06.478569Z"
lastmod: "2026-07-18T17:15:08.668474Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Una funzione matematica che mappa qualsiasi numero reale in un valore compreso tra zero e uno, formando una curva a forma di S."
---
## Definition

La funzione sigmoide, definita come σ(z) = 1 / (1 + e^-z), è ampiamente utilizzata nell'apprendimento automatico per modellare le probabilità. Comprime i valori di input nell'intervallo (0, 1), rendendola adatta per l'output di classificazione binaria e come funzione di attivazione nelle reti neurali.

### Summary

Una funzione matematica che mappa qualsiasi numero reale in un valore compreso tra zero e uno, formando una curva a forma di S.

## Key Concepts

- Funzione logistica
- Mappatura probabilistica
- Gradiente evanescente
- Non linearità

## Use Cases

- Output di classificazione binaria
- Regressione logistica
- Attivazione nelle reti neurali superficiali

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Regressione Logistica](/en/terms/regressione-logistica/)
- [Funzione di Attivazione](/en/terms/funzione-di-attivazione/)
