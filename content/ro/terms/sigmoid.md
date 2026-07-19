---
title: "Sigmoid"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:20:36.161081Z"
lastmod: "2026-07-18T17:15:09.702063Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "O funcție matematică care mapează orice număr cu valoare reală într-o valoare cuprinsă între zero și unu, formând o curbă în formă de S."
---
## Definition

Funcția sigmoid, definită ca σ(z) = 1 / (1 + e^-z), este utilizată pe scară largă în învățarea automată pentru modelarea probabilităților. Aceasta comprima valorile de intrare în intervalul (0, 1), fiind potrivită pentru clasificarea binară.

### Summary

O funcție matematică care mapează orice număr cu valoare reală într-o valoare cuprinsă între zero și unu, formând o curbă în formă de S.

## Key Concepts

- Funcție logistică
- Mapare probabilistică
- Gradient dispărut
- Neliniaritate

## Use Cases

- Ieșirea clasificării binare
- Regresie logistică
- Activare în rețele neuronale superficiale

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Regresie Logistică](/en/terms/regresie-logistică/)
- [Funcție de activare](/en/terms/funcție-de-activare/)
