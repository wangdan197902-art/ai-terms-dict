---
title: "Colapso de representación"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /es/terms/representation_collapse/
date: "2026-07-18T11:06:39.654905Z"
lastmod: "2026-07-18T11:44:44.850418Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Un modo de fallo en el aprendizaje autosupervisado donde el modelo produce representaciones idénticas para todas las entradas, perdiendo poder discriminativo."
---

## Definition

El colapso de representación ocurre cuando una red neuronal, particularmente en marcos de aprendizaje contrastivo autosupervisado, aprende a mapear todos los puntos de datos de entrada al mismo vector de salida fijo. Esta solución trivial elimina la utilidad de las características aprendidas para distinguir entre diferentes muestras.

### Summary

Un modo de fallo en el aprendizaje autosupervisado donde el modelo produce representaciones idénticas para todas las entradas, perdiendo poder discriminativo.

## Key Concepts

- Aprendizaje Autosupervisado
- Pérdida Contrastiva
- Soluciones Triviales
- Aprendizaje de Características

## Use Cases

- Depuración de modelos SimCLR o MoCo
- Mejora de Funciones de Pérdida Contrastiva
- Análisis de la Convergencia del Modelo

## Related Terms

- [Contrastive Learning (Aprendizaje Contrastivo)](/en/terms/contrastive-learning-aprendizaje-contrastivo/)
- [Batch Normalization (Normalización por Lote)](/en/terms/batch-normalization-normalización-por-lote/)
- [Momentum Encoder (Codificador con Momento)](/en/terms/momentum-encoder-codificador-con-momento/)
- [Feature Extraction (Extracción de Características)](/en/terms/feature-extraction-extracción-de-características/)
