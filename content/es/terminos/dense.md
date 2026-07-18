---
title: "Denso"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /es/terms/dense/
date: "2026-07-18T10:43:45.709878Z"
lastmod: "2026-07-18T11:44:44.797567Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Una capa o tensor en el que cada elemento está conectado a todos los elementos de la capa o dimensión anterior."
---

## Definition

En las redes neuronales, 'denso' se refiere a capas completamente conectadas donde cada neurona recibe entrada de todas las neuronas de la capa precedente. Esto contrasta con las conexiones dispersas encontradas en las capas convolucionales o...

### Summary

Una capa o tensor en el que cada elemento está conectado a todos los elementos de la capa o dimensión anterior.

## Key Concepts

- Completamente Conectado
- Matriz de Pesos
- Función de Activación
- Integración de Características

## Use Cases

- Capas de clasificación final en MLPs
- Fusión de características en modelos híbridos
- Tareas simples de regresión

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Red Neuronal Feedforward (Red neuronal de alimentación hacia adelante)](/en/terms/red-neuronal-feedforward-red-neuronal-de-alimentación-hacia-adelante/)
- [Backpropagation (Retropropagación del error)](/en/terms/backpropagation-retropropagación-del-error/)
- [ReLU (Función de activación lineal rectificada)](/en/terms/relu-función-de-activación-lineal-rectificada/)
- [Bias Term (Término de sesgo)](/en/terms/bias-term-término-de-sesgo/)
