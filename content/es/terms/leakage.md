---
title: Fuga de datos
term_id: leakage
category: basic_concepts
subcategory: ''
tags:
- Data Integrity
- evaluation
- Best Practices
difficulty: 3
weight: 1
slug: leakage
date: '2026-07-18T10:57:23.388497Z'
lastmod: '2026-07-18T11:44:44.824973Z'
draft: false
source: agnes_llm
status: published
language: es
description: La fuga de datos ocurre cuando información externa al conjunto de entrenamiento
  influye inadvertidamente en el modelo, lo que lleva a estimaciones de rendimiento
  excesivamente optimistas.
---
## Definition

La fuga de datos es un error crítico en el aprendizaje automático donde el modelo accede a información durante el entrenamiento que no estaría disponible en el momento de la predicción. Esto suele ocurrir debido a una división inadecuada de los datos o a la inclusión de características que contienen información futura o del objetivo.

### Summary

La fuga de datos ocurre cuando información externa al conjunto de entrenamiento influye inadvertidamente en el modelo, lo que lleva a estimaciones de rendimiento excesivamente optimistas.

## Key Concepts

- Fuga del objetivo
- Contaminación entre entrenamiento y prueba
- División adecuada de datos

## Use Cases

- Depuración del sobreajuste del modelo
- Validación de pipelines de ingeniería de características
- Garantizar una evaluación robusta del modelo

## Related Terms

- [Sobreajuste (Overfitting)](/en/terms/sobreajuste-overfitting/)
- [Validación cruzada (Cross-validation)](/en/terms/validación-cruzada-cross-validation/)
- [Ingeniería de características (Feature engineering)](/en/terms/ingeniería-de-características-feature-engineering/)
