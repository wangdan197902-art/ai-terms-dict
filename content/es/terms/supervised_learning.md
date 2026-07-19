---
title: Aprendizaje Supervisado
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T10:32:20.236499Z'
lastmod: '2026-07-18T11:44:44.767576Z'
draft: false
source: agnes_llm
status: published
language: es
description: Un paradigma de aprendizaje automático donde un modelo aprende a mapear
  entradas a salidas basándose en ejemplos de entrenamiento etiquetados.
---
## Definition

En el aprendizaje supervisado, el algoritmo se entrena con un conjunto de datos etiquetados, lo que significa que cada ejemplo de entrada está emparejado con la salida correcta. El objetivo es que el modelo aprenda la relación subyacente entre las entradas y las salidas.

### Summary

Un paradigma de aprendizaje automático donde un modelo aprende a mapear entradas a salidas basándose en ejemplos de entrenamiento etiquetados.

## Key Concepts

- Datos Etiquetados
- Mapeo Entrada-Salida
- Clasificación
- Regresión

## Use Cases

- Detección de correo no deseado
- Predicción de precios de viviendas
- Reconocimiento de imágenes

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Aprendizaje No Supervisado (Sin etiquetas)](/en/terms/aprendizaje-no-supervisado-sin-etiquetas/)
- [Conjunto de Entrenamiento (Datos para aprender)](/en/terms/conjunto-de-entrenamiento-datos-para-aprender/)
- [Conjunto de Validación (Datos para ajustar hiperparámetros)](/en/terms/conjunto-de-validación-datos-para-ajustar-hiperparámetros/)
- [Precisión del Modelo (Métrica de rendimiento)](/en/terms/precisión-del-modelo-métrica-de-rendimiento/)
