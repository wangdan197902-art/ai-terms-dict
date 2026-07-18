---
title: "Aumento de Datos"
term_id: "data_augmentation"
category: "training_techniques"
subcategory: ""
tags: ["machine_learning", "preprocessing", "cv"]
difficulty: 2
weight: 1
slug: "data_augmentation"
aliases:
  - /es/terms/data_augmentation/
date: "2026-07-18T10:41:37.051958Z"
lastmod: "2026-07-18T11:44:44.791390Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "El aumento de datos es una técnica utilizada para aumentar la diversidad y el tamaño de los conjuntos de datos de entrenamiento aplicando transformaciones a los puntos de datos existentes."
---

## Definition

Este método expande artificialmente el conjunto de datos de entrenamiento creando versiones modificadas de las muestras existentes, como rotar imágenes, añadir ruido al audio o reemplazar sinónimos en texto. Ayuda a prevenir

### Summary

El aumento de datos es una técnica utilizada para aumentar la diversidad y el tamaño de los conjuntos de datos de entrenamiento aplicando transformaciones a los puntos de datos existentes.

## Key Concepts

- Prevención del Sobreajuste
- Expansión del Conjunto de Datos
- Generalización
- Transformaciones

## Use Cases

- Mejorar la robustez de los modelos de visión por computadora
- Mejorar el rendimiento de los modelos de PLN con texto limitado
- Equilibrar conjuntos de datos desbalanceados

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularización (Regularization)](/en/terms/regularización-regularization/)
- [Datos Sintéticos (Synthetic Data)](/en/terms/datos-sintéticos-synthetic-data/)
- [Aprendizaje por Transferencia (Transfer Learning)](/en/terms/aprendizaje-por-transferencia-transfer-learning/)
- [Sobreajuste (Overfitting)](/en/terms/sobreajuste-overfitting/)
