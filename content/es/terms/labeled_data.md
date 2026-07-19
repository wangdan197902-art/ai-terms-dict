---
title: Datos etiquetados
term_id: labeled_data
category: basic_concepts
subcategory: ''
tags:
- data
- Supervised Learning
- fundamentals
difficulty: 1
weight: 1
slug: labeled_data
date: '2026-07-18T10:57:10.137018Z'
lastmod: '2026-07-18T11:44:44.824296Z'
draft: false
source: agnes_llm
status: published
language: es
description: Datos en los que se proporciona el valor de salida o objetivo correcto
  junto con las características de entrada.
---
## Definition

Los datos etiquetados consisten en muestras de entrada emparejadas con sus etiquetas de verdad fundamental correspondientes, sirviendo como base para el aprendizaje automático supervisado. Permiten a los algoritmos aprender la relación entre la entrada y la salida esperada.

### Summary

Datos en los que se proporciona el valor de salida o objetivo correcto junto con las características de entrada.

## Key Concepts

- Aprendizaje supervisado
- Verdad fundamental
- Anotación
- Variable objetivo

## Use Cases

- Entrenamiento de clasificadores de imágenes
- Desarrollo de sistemas de reconocimiento de voz
- Modelado predictivo en finanzas

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (datos sin etiquetar)](/en/terms/unlabeled_data-datos-sin-etiquetar/)
- [supervised_learning (aprendizaje supervisado)](/en/terms/supervised_learning-aprendizaje-supervisado/)
- [data_annotation (anotación de datos)](/en/terms/data_annotation-anotación-de-datos/)
- [training_set (conjunto de entrenamiento)](/en/terms/training_set-conjunto-de-entrenamiento/)
