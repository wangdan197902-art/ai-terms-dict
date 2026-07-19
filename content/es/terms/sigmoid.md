---
title: "Sigmoide"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T11:07:47.558864Z"
lastmod: "2026-07-18T11:44:44.853907Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Una función matemática que mapea cualquier número de valor real a un valor entre cero y uno, formando una curva en forma de S."
---
## Definition

La función sigmoide, definida como σ(z) = 1 / (1 + e^-z), se utiliza ampliamente en el aprendizaje automático para modelar probabilidades. Comprime los valores de entrada en el rango (0, 1), lo que la hace adecuada para la clasificación binaria y como función de activación en redes neuronales.

### Summary

Una función matemática que mapea cualquier número de valor real a un valor entre cero y uno, formando una curva en forma de S.

## Key Concepts

- Función logística
- Mapeo de probabilidad
- Desvanecimiento del gradiente
- No linealidad

## Use Cases

- Salida de clasificación binaria
- Regresión logística
- Activación en redes neuronales poco profundas

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Logistic Regression (Regresión Logística)](/en/terms/logistic-regression-regresión-logística/)
- [Activation Function (Función de Activación)](/en/terms/activation-function-función-de-activación/)
