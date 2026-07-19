---
title: auto-supervisado
term_id: self_supervised
category: training_techniques
subcategory: ''
tags:
- Learning Paradigms
- NLP
- scalability
difficulty: 4
weight: 1
slug: self_supervised
date: '2026-07-18T10:29:07.319241Z'
lastmod: '2026-07-18T11:44:44.759064Z'
draft: false
source: agnes_llm
status: published
language: es
description: El aprendizaje auto-supervisado es una técnica en la que el modelo genera
  sus propias etiquetas a partir de los datos de entrada para aprender representaciones
  sin anotación humana.
---
## Definition

El aprendizaje auto-supervisado es un subconjunto del aprendizaje automático donde la señal de supervisión se deriva automáticamente de los propios datos, eliminando la necesidad de etiquetado manual. El modelo típicamente resuelve tareas pretext (como predecir palabras faltantes o rotaciones de imagen) para aprender representaciones útiles que luego pueden transferirse a otras tareas.

### Summary

El aprendizaje auto-supervisado es una técnica en la que el modelo genera sus propias etiquetas a partir de los datos de entrada para aprender representaciones sin anotación humana.

## Key Concepts

- Tareas pretext
- Modelado enmascarado
- Datos no etiquetados
- Aprendizaje de representaciones

## Use Cases

- Entrenar BERT mediante modelado de lenguaje enmascarado
- Aprendizaje contrastivo para incrustaciones de imágenes
- Predicción de los siguientes tokens en grandes modelos de lenguaje

## Related Terms

- [unsupervised (no supervisado)](/en/terms/unsupervised-no-supervisado/)
- [contrastive_learning (aprendizaje contrastivo)](/en/terms/contrastive_learning-aprendizaje-contrastivo/)
- [masked_language_modeling (modelado de lenguaje enmascarado)](/en/terms/masked_language_modeling-modelado-de-lenguaje-enmascarado/)
- [representation_learning (aprendizaje de representaciones)](/en/terms/representation_learning-aprendizaje-de-representaciones/)
