---
title: Ajuste de instrucciones (Prompt Tuning)
term_id: prompt_tuning
category: training_techniques
subcategory: ''
tags:
- LLM
- Optimization
- efficiency
difficulty: 3
weight: 1
slug: prompt_tuning
date: '2026-07-18T11:04:59.321444Z'
lastmod: '2026-07-18T11:44:44.845888Z'
draft: false
source: agnes_llm
status: published
language: es
description: Un método de ajuste fino eficiente en parámetros que optimiza incrustaciones
  de entrada continuas en lugar de actualizar todos los pesos del modelo.
---
## Definition

El ajuste de instrucciones implica agregar 'instrucciones suaves' entrenables (vectores continuos) a la capa de entrada de un modelo de lenguaje preentrenado, manteniendo congelados los parámetros subyacentes del modelo. Este enfoque permite adaptar modelos grandes a tareas específicas con una fracción mínima de parámetros adicionales, reduciendo significativamente el costo computacional y el riesgo de sobreajuste en comparación con el ajuste fino tradicional.

### Summary

Un método de ajuste fino eficiente en parámetros que optimiza incrustaciones de entrada continuas en lugar de actualizar todos los pesos del modelo.

## Key Concepts

- instrucciones suaves
- eficiencia de parámetros
- pesos congelados
- aprendizaje few-shot

## Use Cases

- Adaptación de LLMs para dominios específicos
- Ajuste fino con recursos limitados
- Optimización del aprendizaje multitarea

## Related Terms

- [PEFT (Técnicas de Ajuste Fino Eficientes en Parámetros)](/en/terms/peft-técnicas-de-ajuste-fino-eficientes-en-parámetros/)
- [LoRA (Adaptadores de Rango Bajo)](/en/terms/lora-adaptadores-de-rango-bajo/)
- [aprendizaje en contexto](/en/terms/aprendizaje-en-contexto/)
- [ajuste fino](/en/terms/ajuste-fino/)
