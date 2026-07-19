---
title: "Sigmoid"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:17:18.468440Z"
lastmod: "2026-07-18T17:15:09.200291Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Matematická funkce, která mapuje jakékoli reálné číslo na hodnotu mezi nulou a jedničkou, čímž vytváří S-tvarovou křivku."
---
## Definition

Sigmoidní funkce, definovaná jako σ(z) = 1 / (1 + e^-z), je široce používána ve strojovém učení k modelování pravděpodobností. Stlačuje vstupní hodnoty do rozsahu (0, 1), což ji činí vhodnou pro binární klasifikaci a výstupní vrstvy neuronových sítí.

### Summary

Matematická funkce, která mapuje jakékoli reálné číslo na hodnotu mezi nulou a jedničkou, čímž vytváří S-tvarovou křivku.

## Key Concepts

- Logistická funkce
- Mapování pravděpodobnosti
- Mizející gradient
- Nelinearita

## Use Cases

- Výstup binární klasifikace
- Logistická regrese
- Aktivační funkce v mělkých neuronových sítích

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Logistická regrese](/en/terms/logistická-regrese/)
- [Aktivační funkce](/en/terms/aktivační-funkce/)
