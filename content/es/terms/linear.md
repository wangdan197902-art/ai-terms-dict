---
title: "Lineal"
term_id: "linear"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Foundations"]
difficulty: 2
weight: 1
slug: "linear"
date: "2026-07-18T10:24:12.554795Z"
lastmod: "2026-07-18T11:44:44.744176Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Describe operaciones o relaciones donde la salida es directamente proporcional a la entrada, formando la base de las transformaciones afines en las capas neuronales."
---
## Definition

Las operaciones lineales implican multiplicación y adición sin activaciones no lineales. En las redes neuronales, las capas lineales (o densas) aplican una transformación de matriz de pesos a los vectores de entrada. Aunque lo

### Summary

Describe operaciones o relaciones donde la salida es directamente proporcional a la entrada, formando la base de las transformaciones afines en las capas neuronales.

## Key Concepts

- Matriz de Pesos
- Transformación Afín
- Producto Escalar
- Superposición

## Use Cases

- Proyección de Características
- Regresión Logística
- Mecanismos de Atención

## Code Example

```python
import torch.nn as nn
layer = nn.Linear(10, 5)
output = layer(input_tensor)
```

## Related Terms

- [Función de Activación](/en/terms/función-de-activación/)
- [Capa Densa](/en/terms/capa-densa/)
- [Multiplicación de Matrices](/en/terms/multiplicación-de-matrices/)
