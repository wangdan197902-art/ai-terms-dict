---
title: Ajuste por prefijo
term_id: prefix_tuning
category: training_techniques
subcategory: ''
tags:
- Fine-Tuning
- efficiency
- transformers
difficulty: 4
weight: 1
slug: prefix_tuning
date: '2026-07-18T11:04:18.184633Z'
lastmod: '2026-07-18T11:44:44.844178Z'
draft: false
source: agnes_llm
status: published
language: es
description: Un método de ajuste fino eficiente en parámetros que añade vectores continuos
  entrenables a la entrada de las capas del transformador.
---
## Definition

El ajuste por prefijo es una técnica de adaptación eficiente en parámetros para transformadores preentrenados. En lugar de actualizar todos los pesos del modelo, se antepone una secuencia de vectores continuos entrenables (el prefijo) a las entradas de las capas del transformador. Esto permite adaptar el comportamiento del modelo a nuevas tareas con una fracción mínima de parámetros adicionales, manteniendo congelada la arquitectura base.

### Summary

Un método de ajuste fino eficiente en parámetros que añade vectores continuos entrenables a la entrada de las capas del transformador.

## Key Concepts

- Ajuste fino eficiente en parámetros
- Indicadores suaves (soft prompts)
- Capas del transformador
- Columna vertebral congelada

## Use Cases

- Adaptación para aprendizaje con pocos ejemplos
- Aprendizaje multitarea con recursos limitados
- Personalización de grandes modelos de lenguaje para dominios específicos

## Related Terms

- [prompt_tuning (ajuste de indicadores)](/en/terms/prompt_tuning-ajuste-de-indicadores/)
- [p_tuning (ajuste P)](/en/terms/p_tuning-ajuste-p/)
- [adapter_modules (módulos adaptadores)](/en/terms/adapter_modules-módulos-adaptadores/)
- [peft (técnicas de ajuste fino eficiente en parámetros)](/en/terms/peft-técnicas-de-ajuste-fino-eficiente-en-parámetros/)
